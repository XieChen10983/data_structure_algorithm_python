# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/9/5 22:13
filename(文件名): hanoi.py
function description(功能描述):
...
    此代码实现汉诺塔问题。
"""


def move(a: str, b: str):
    print(a + " -> " + b)
#
#
# def moveA2C():
#     print("A -> C")
#
#
# def moveC2A():
#     print("C -> A")
#
#
# def moveB2A():
#     print("B -> A")
#
#
# def moveB2C():
#     print("B -> C")


def Hanoi(num: int, a: str, b: str, c: str):
    if num == 1:
        move(a, c)
    else:
        Hanoi(num - 1, a, c, b)
        move(a, c)
        Hanoi(num - 1, b, a, c)


def hanoi(num: int, a, b, c):
    if num == 1:
        move(a, c)
    # elif num == 2:
    #     moveA2B()
    #     moveA2C()
    #     moveB2C()
    else:
        hanoi(num - 1, a, c, b)
        move(a, c)
        hanoi(num - 1, b, a, c)


Hanoi(3, "A", "B", "C")
