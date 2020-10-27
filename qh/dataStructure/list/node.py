# coding=gbk
"""
此代码实现链表中的节点类
"""
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next = b
    b.next = c
    head = a
    print(head.item)
    print(head.next.item)
    print(head.next.next.item)
    print(head.next.next.next.item)
