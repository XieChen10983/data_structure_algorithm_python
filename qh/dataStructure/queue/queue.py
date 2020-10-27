# coding=gbk
"""
此代码使用python实现队列
"""


class Queue:
    def __init__(self):
        self.queue = []

    def pop(self):
        if len(self.queue) != 0:
            front = self.queue[0]
            self.queue = self.queue[1:]
            return front

    def append(self, elem):
        self.queue.append(elem)

    def get_Top(self):
        return self.queue[-1]

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def __repr__(self):
        ret = ''
        for elem in self.queue[:-1]:
            ret += str(elem) + ', '
        return '[' + ret + str(self.queue[-1]) + ']'


class RoundQueue:

    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0   # 初始的队尾指针
        self.front = 0   # 初始的队头指针

    def push(self, elem):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = elem
        else:
            raise IndexError("Queue is filled.")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty.")

    def is_empty(self):
        return self.rear == self.front

    def is_full(self):
        return (self.rear + 1) % self.size == self.front


queue = Queue()
import random
for i in range(10):
    queue.append(random.randint(0, 10))
print(queue)

for _ in range(5):
    print(queue.pop())
    print(queue)
