# coding=gbk
"""
author(����): Channing Xie(л�)
time(ʱ��): 2020/9/6 9:31
filename(�ļ���): 1_bubble_sort.py
function description(��������):
...
    �˴���ʵ��ð������
"""


def bubble_Sort(list1: list, up=True):
    """
    �˺���ʵ���б��ð������
    :param list1:
    :param up:
    :return:
    """
    listLength = len(list1)
    if up:
        for Round in range(listLength - 1):
            for position in range(listLength - 1 - Round):
                if list1[position] > list1[position + 1]:
                    list1[position], list1[position + 1] = list1[position + 1], list1[position]
    else:
        for Round in range(listLength - 1):
            for position in range(listLength - 1 - Round):
                if list1[position] < list1[position + 1]:
                    list1[position], list1[position + 1] = list1[position + 1], list1[position]
    # return list1


# import random
# list1 = [random.randint(0, 100) for _ in range(20)]
# print(list1)
# bubble_Sort(list1)
# print(list1)
# print(bubbleSort(list1))
