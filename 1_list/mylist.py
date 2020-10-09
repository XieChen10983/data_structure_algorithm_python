# coding=gbk
"""
author(����): Channing Xie(л�)
time(ʱ��): 2020/9/4 22:23
filename(�ļ���): mylist.py
function description(��������):
...
    �˴���ʵ�����α�ĸ����
"""


class MyList:
    def __init__(self, *input):
        """
        ��ʼ�����Ա�
        :param input:
        """
        self.list = []
        for elem in input:
            self.list.append(elem)

    def isEmpty(self):
        """
        �ж����Ա��Ƿ�Ϊ��
        :return:
        """
        return len(self.list) == 0

    def clearList(self):
        """
        ���б����
        :return:
        """
        self.list = []

    def getElem(self, index):
        """
        ��ȡ��index��Ԫ��
        :param index:
        :return:
        """
        assert len(self.list) > index >= 0 and isinstance(index, int)
        return self.list[index]

    def locateElem(self, value):
        """
        �ж��б����Ƿ����value���ֵ��������ڣ�����λ�����������򷵻�-1
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
        ���б�ĵ�index��λ�ò���value
        :param index:
        :param value:
        :return:
        """
        self.list.insert(index, value)

    def listDelete(self, index):
        """
        ɾ�����Ա�ĵ�index��Ԫ��
        :param index:
        :return:
        """
        return self.list.pop(index)

    def listLength(self):
        """
        �������Ա�ĳ���
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
