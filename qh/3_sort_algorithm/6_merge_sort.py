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


def merge(List: list, low: int, mid: int, high: int):
    """
    此函数实现归并排序。
    :param mid:
    :param List:
    :param low:
    :param high:
    :return:
    """
    # assert end < len(List)
    i = low
    j = mid + 1
    newList = []
    while i <= mid and j <= high:
        if List[i] < List[j]:
            newList.append(List[i])
            i += 1
        else:
            newList.append(List[j])
            j += 1
    while i <= mid:
        newList.append(List[i])
        i += 1
    while j <= high:
        newList.append(List[j])
        j += 1
    List[low:high+1] = newList


def mergeSort(List: list, low=0, high=None):
    if high is None:
        high = len(List) - 1
    if low < high:
        mid = (low + high) // 2
        mergeSort(List, low, mid)
        mergeSort(List, mid+1, high)
        merge(List, low, mid, high)


# li = list(range(1000))
# import random
# random.shuffle(li)
# print(li)
# mergeSort(li, 0, len(li) - 1)
# print(li)


l1 = [1, 2, 7, 8, 3, 4, 5, 6, 9, 10, 100]
import random
l2 = [random.randint(0, 100) for _ in range(10)]
print(l2)
mergeSort(l2)
print(l2)
# merge(l1, 0, 3, 11)
# print(l1)
