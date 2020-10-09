# coding=gbk
"""
author(����): Channing Xie(л�)
time(ʱ��): 2020/9/5 8:05
filename(�ļ���): sequential_search.py
function description(��������):
...
    �˴���ʵ��˳����ң��㷨��ʱ�临�Ӷ�ΪO(n)
"""


def sequentialSearch(List: list, value, return_all=False):
    """
    �˺���ʵ��˳�����
    :param return_all:
    :param List:
    :param value:
    :return:
    """
    if not return_all:
        for index, val in enumerate(List):
            if val == value:
                return index
        return -1
    else:
        indexes = []
        for index, val in enumerate(List):
            if val == value:
                indexes.append(index)
        if indexes:
            return indexes
        else:
            return [-1]


print(sequentialSearch(['a', 7, 8, 9, 1, 6, 5, 1], 2, True))
