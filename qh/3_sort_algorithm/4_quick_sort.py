# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/9/6 15:04
filename(文件名): 4_quick_sort.py
function description(功能描述):
...
    此代码实现快速排列
"""


def partition(List: list, left, right):
    firstValue = List[left]
    while left < right:
        while left < right and List[right] >= firstValue:
            right -= 1
        List[left] = List[right]
        while left < right and List[left] <= firstValue:
            left += 1
        List[right] = List[left]
    List[left] = firstValue
    return left


def quickSort(List: list, left=None, right=None):
    """
    此函数实现快速排序。
    :param right:
    :param left:
    :param List:
    :return:
    """
    listLength = len(List)
    if left is None:
        left = 0
    if right is None:
        right = listLength - 1
    if left < right:
        mid = partition(List, left, right)
        quickSort(List, left, mid - 1)
        quickSort(List, mid + 1, right)


import random
list1 = [random.randint(0, 100) for _ in range(20)]
print(list1)
partition(list1, 0, 19)
print(list1)
quickSort(list1)
print(list1)
