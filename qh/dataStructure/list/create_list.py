# coding=gbk
"""
此代码实现链表的初始化
"""
from node import Node


def print_linkList(lk: Node):
    while lk:
        print(lk.item, end=',')
        lk = lk.next


def create_List_Head(li: list):
    """
    头插法创建链表
    :param li:
    :return:
    """
    head = Node(li[0])
    for index in range(1, len(li)):
        newNode = Node(li[index])
        newNode.next = head
        head = newNode
    return head


def create_List_Tail(li: list):
    """
    尾插法创建链表。
    :param li:
    :return:
    """
    head = Node(li[0])
    tail = head
    for elem in li[1:]:
        newNode = Node(elem)
        tail.next = newNode
        tail = newNode
    return head


if __name__ == '__main__':
    a = [1, 3, 2, 4, 5]
    # h = create_List_Head(a)
    h = create_List_Tail(a)
    print_linkList(h)
    # print(h.item)
    # print(h.next.item)
    # print(h.next.next.item)
    # print(h.next.next.next.item)
    # print(h.next.next.next.next.item)
