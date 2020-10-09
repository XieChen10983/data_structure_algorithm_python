# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/10/8 21:59
filename(文件名): 6_merge_sort.py.py
function description(功能描述):
...
    此段代码实现归并排序
"""


def merge_List(List1: list, List2: list):
    mergeList = []
    length1 = len(List1)
    length2 = len(List2)
    while (length1 != 0) and (length2 != 0):
        if List1[0] < List2[0]:
            mergeList.append(List1[0])
            List1 = List1[1:]
            length1 -= 1
        else:
            mergeList.append(List2[0])
            List2 = List2[1:]
            length2 -= 1
    if length1 == 0:
        mergeList = mergeList + List2
    else:
        mergeList = mergeList + List1
    return mergeList


l1 = merge_List([1, 2, 7, 8], [3, 4, 5, 6, 9, 10, 100])
print(l1)
