# coding=gbk
"""
author(����): Channing Xie(л�)
time(ʱ��): 2020/9/6 11:06
filename(�ļ���): fibonacci.py
function description(��������):
...
    �˴���ʵ��쳲���������
"""


def fibonacci(num: int):
    """
    �˺���������쳲��������е�ǰn��
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
