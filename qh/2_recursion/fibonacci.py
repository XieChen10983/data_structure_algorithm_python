# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/9/6 11:06
filename(文件名): fibonacci.py
function description(功能描述):
...
    此代码实现斐波那契数列
"""


def fibonacci(num: int):
    """
    此函数给出了斐波那契数列的前n个
    :param num:
    :return:
    """
    assert 0 < num
    if num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


for n in range(1, 30):
    print(fibonacci(n), '\t', end='')
