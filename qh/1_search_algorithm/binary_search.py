# coding=gbk
"""
author(����): Channing Xie(л�)
time(ʱ��): 2020/9/5 8:13
filename(�ļ���): binary_search.py
function description(��������):
...
    �˴���ʵ�����Ա�Ķ��ֲ��ң�ʱ�临�Ӷ�ΪO(log(n))�������ڲ���֮ǰ��Ҫ�����Ա��������
"""


def binarySearch(List: list, value):
    """
    �˺���ʵ���б�Ķ��ֲ��ҡ�
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
