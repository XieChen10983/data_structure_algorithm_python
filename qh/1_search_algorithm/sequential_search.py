# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/9/5 8:05
filename(文件名): sequential_search.py
function description(功能描述):
...
    此代码实现顺序查找，算法的时间复杂度为O(n)
"""


def sequentialSearch(List: list, value, return_all=False):
    """
    此函数实现顺序查找
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
