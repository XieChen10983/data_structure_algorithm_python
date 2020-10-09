# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/9/6 9:50
filename(文件名): 2_select_sort1.py
function description(功能描述):
...
    此代码实现选择排序
"""


def select_Sort(List: list, up=True):
    """
    此代码实现列表的选择排序
    :param List:
    :param up:
    :return:
    """
    listLength = len(List)
    if up:
        for Round in range(listLength - 1):
            temp_Value = List[0]
            temp_Index = 0
            for index in range(1, listLength - Round):
                if List[index] > temp_Value:
                    temp_Index = index
                    temp_Value = List[index]
            List[temp_Index], List[listLength - 1 - Round] = List[listLength - 1 - Round], temp_Value
    else:
        for Round in range(listLength - 1):
            temp_Value = List[0]
            temp_Index = 0
            for index in range(1, listLength - Round):
                if List[index] < temp_Value:
                    temp_Index = index
                    temp_Value = List[index]
            List[temp_Index], List[listLength - 1 - Round] = List[listLength - 1 - Round], temp_Value


import random
list1 = [random.randint(0, 100) for _ in range(20)]
print(list1)
select_Sort(list1, False)
print(list1)
# print(selectSortSimple(list1))
