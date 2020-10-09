# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/9/6 10:48
filename(文件名): 3_insert_sort.py
function description(功能描述):
...
    此代码实现插入排序
"""


def insertSort(List: list):
    """
    此函数实现插入排序。
    :param List:
    :return:
    """
    listLength = len(List)
    for i in range(1, listLength):
        currentElement = List[i]
        j = 0
        while (List[j] < currentElement) and (j < i):
            j += 1
        List[j + 1:i + 1] = List[j:i]
        List[j] = currentElement
    return List


def insertSort2(List: list):
    for index in range(1, len(List)):
        currentElement = List[index]
        sortedIndex = index - 1
        while sortedIndex > -1 and List[sortedIndex] > currentElement:
            List[sortedIndex + 1] = List[sortedIndex]
            sortedIndex -= 1
        List[sortedIndex + 1] = currentElement
    # return List


import random
list1 = [random.randint(0, 100) for _ in range(20)]
print(list1)
insertSort2(list1)
print(list1)
