#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : 陈坤泽
# @Email  : 877362867@qq.com
# @Date   : 2020/06/02 11:09

from collections import defaultdict, Counter
import sys

import pandas as pd

from pyxllib.prog.newbie import typename
from pyxllib.text.pupil import shorten, east_asian_shorten
from pyxllib.algo.pupil import natural_sort_key


def dataframe_str(df, *args, ambiguous_as_wide=None, shorten=True):
    """输出DataFrame
    DataFrame可以直接输出的，这里是增加了对中文字符的对齐效果支持

    :param df: DataFrame数据结构
    :param args: option_context格式控制
    :param ambiguous_as_wide: 是否对①②③这种域宽有歧义的设为宽字符
        win32平台上和linux上①域宽不同，默认win32是域宽2，linux是域宽1
    :param shorten: 是否对每个元素提前进行字符串化并控制长度在display.max_colwidth以内
        因为pandas的字符串截取遇到中文是有问题的，可以用我自定义的函数先做截取
        默认开启，不过这步比较消耗时间

    >> df = pd.DataFrame({'哈哈': ['a'*100, '哈\n①'*10, 'a哈'*100]})
                                                        哈哈
        0  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa...
        1   哈 ①哈 ①哈 ①哈 ①哈 ①哈 ①哈 ①哈 ①哈 ①...
        2  a哈a哈a哈a哈a哈a哈a哈a哈a哈a哈a哈a哈a哈a哈a哈a...
    """
    import pandas as pd

    if ambiguous_as_wide is None:
        ambiguous_as_wide = sys.platform == 'win32'
    with pd.option_context('display.unicode.east_asian_width', True,  # 中文输出必备选项，用来控制正确的域宽
                           'display.unicode.ambiguous_as_wide', ambiguous_as_wide,
                           'max_columns', 20,  # 最大列数设置到20列
                           'display.width', 200,  # 最大宽度设置到200
                           *args):
        if shorten:  # applymap可以对所有的元素进行映射处理，并返回一个新的df
            df = df.applymap(lambda x: east_asian_shorten(str(x), pd.options.display.max_colwidth))
        s = str(df)
    return s


class TypeConvert:
    @classmethod
    def dict2list(cls, d: dict, *, nsort=False):
        """ 字典转n*2的list

        :param d: 字典
        :param nsort:
            True: 对key使用自然排序
            False: 使用d默认的遍历顺序
        :return:
        """
        ls = list(d.items())
        if nsort:
            ls = sorted(ls, key=lambda x: natural_sort_key(str(x[0])))
        return ls

    @classmethod
    def dict2df(cls, d):
        """dict类型转DataFrame类型"""
        name = typename(d)
        if isinstance(d, Counter):
            li = d.most_common()
        else:
            li = cls.dict2list(d, nsort=True)
        return pd.DataFrame.from_records(li, columns=(f'{name}-key', f'{name}-value'))

    @classmethod
    def list2df(cls, li):
        if li and isinstance(li[0], (list, tuple)):  # 有两维时按表格显示
            df = pd.DataFrame.from_records(li)
        else:  # 只有一维时按一列显示
            df = pd.DataFrame(pd.Series(li), columns=(typename(li),))
        return df

    @classmethod
    def try2df(cls, arg):
        """尝试将各种不同的类型转成dataframe"""
        if isinstance(arg, dict):
            df = cls.dict2df(arg)
        elif isinstance(arg, (list, tuple)):
            df = cls.list2df(arg)
        elif isinstance(arg, pd.Series):
            df = pd.DataFrame(arg)
        else:
            df = arg
        return df


class NestedDict:
    """ 字典嵌套结构相关功能

    TODO 感觉跟 pprint 的嵌套识别美化输出相关，可能有些代码是可以结合简化的~~
    """

    @classmethod
    def has_subdict(cls, data, include_self=True):
        """是否含有dict子结构
        :param include_self: 是否包含自身，即data本身是一个dict的话，也认为has_subdict是True
        """
        if include_self and isinstance(data, dict):
            return True
        elif isinstance(data, (list, tuple, set)):
            for v in data:
                if cls.has_subdict(v):
                    return True
        return False

    @classmethod
    def to_html_table(cls, data, max_items=10):
        """ 以html表格套表格的形式，展示一个嵌套结构数据

        :param data: 数据
        :param max_items: 项目显示上限，有些数据项目太多了，要精简下
            设为假值则不设上限
        :return:

        TODO 这个速度有点慢，怎么加速？
        """

        def tohtml(d):
            if max_items:
                df = TypeConvert.try2df(d)
                if len(df) > max_items:
                    n = len(df)
                    return df[:max_items].to_html(escape=False) + f'... {n - 1}'
                else:
                    return df.to_html(escape=False)
            else:
                return TypeConvert.try2df(d).to_html(escape=False)

        if not cls.has_subdict(data):
            res = str(data)
        elif isinstance(data, dict):
            if isinstance(data, Counter):
                d = data
            else:
                d = dict()
                for k, v in data.items():
                    if cls.has_subdict(v):
                        v = cls.to_html_table(v, max_items=max_items)
                    d[k] = v
            res = tohtml(d)
        else:
            li = [cls.to_html_table(x, max_items=max_items) for x in data]
            res = tohtml(li)

        return res.replace('\n', ' ')


class KeyValuesCounter:
    """ 各种键值对出现次数的统计
    会递归找子字典结构，但不存储结构信息，只记录纯粹的键值对信息

    应用场景：对未知的json结构，批量读取后，显示所有键值对的出现情况
    """

    def __init__(self):
        self.kvs = defaultdict(Counter)

    def add(self, data, max_value_length=100):
        """
        :param max_value_length: 添加的值，进行截断，防止有些值太长
        """
        if not NestedDict.has_subdict(data):
            return
        elif isinstance(data, dict):
            for k, v in data.items():
                if NestedDict.has_subdict(v):
                    self.add(v)
                else:
                    self.kvs[k][shorten(str(v), max_value_length)] += 1
        else:  # 否则 data 应该是个可迭代对象，才可能含有dict
            for x in data:
                self.add(x)

    def to_html_table(self, max_items=10):
        return NestedDict.to_html_table(self.kvs, max_items=max_items)
