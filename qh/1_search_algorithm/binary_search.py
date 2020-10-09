# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/9/5 8:13
filename(文件名): binary_search.py
function description(功能描述):
...
    此代码实现线性表的二分查找，时间复杂度为O(log(n))，不过在查找之前需要对线性表进行排序。
"""


def binarySearch(List: list, value):
    """
    此函数实现列表的二分查找。
    :param List:
    :param value:
    :return:
    """
    listLength = len(List)
    leftIndex = 0
    rightIndex = listLength - 1
    flag = False
    if List[leftIndex] > value or List[rightIndex] < value:
        return -1
    elif List[leftIndex] == value:
        return leftIndex
    elif List[rightIndex] == value:
        return rightIndex
    else:
        while (not flag) and (leftIndex <= rightIndex):
            midIndex = (leftIndex + rightIndex) // 2
            if List[midIndex] == value:
                return midIndex
            elif List[midIndex] < value:
                leftIndex = midIndex + 1
            elif List[midIndex] > value:
                rightIndex = midIndex - 1
        return -1


list1 = list(range(10))
print(binarySearch(list1, 3))
