# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/9/4 22:23
filename(文件名): mylist.py
function description(功能描述):
...
    此代码实现线形表的各项功能
"""


class MyList:
    def __init__(self, *input):
        """
        初始化线性表
        :param input:
        """
        self.list = []
        for elem in input:
            self.list.append(elem)

    def isEmpty(self):
        """
        判断线性表是否为空
        :return:
        """
        return len(self.list) == 0

    def clearList(self):
        """
        将列表清空
        :return:
        """
        self.list = []

    def getElem(self, index):
        """
        提取第index个元素
        :param index:
        :return:
        """
        assert len(self.list) > index >= 0 and isinstance(index, int)
        return self.list[index]

    def locateElem(self, value):
        """
        判断列表中是否存在value这个值，如果存在，返回位置索引；否则返回-1
        :param value:
        :return:
        """
        indexes = []
        for index, val in enumerate(self.list):
            if val == value:
                indexes.append(index)
        if len(indexes) == 0:
            return [-1]
        else:
            return indexes

    def listInsert(self, index, value):
        """
        在列表的第index个位置插入value
        :param index:
        :param value:
        :return:
        """
        self.list.insert(index, value)

    def listDelete(self, index):
        """
        删除线性表的第index个元素
        :param index:
        :return:
        """
        return self.list.pop(index)

    def listLength(self):
        """
        返回线性表的长度
        :return:
        """
        return len(self.list)

    def printList(self):
        print(self.list)

    def __repr__(self):
        data = ''
        for elem in self.list[:-1]:
            data += str(elem) + ', '
        data += str(self.list[-1])
        return "MyList(" + data + ')'


a = MyList('a', 5, 3, 5, 4)
a.printList()
print(a.isEmpty())
# a.clearList()
# print(a.isEmpty())
print(a.getElem(0))
print(a.locateElem(5))
a.listInsert(1, 'b')
a.printList()
print(a.locateElem(5))
b = a.listDelete(1)
print(b)
a.printList()
print(a)
