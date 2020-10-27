# encode=gbk


class Stack:
    def __init__(self):
        self.stack = []

    def append(self, elem):
        self.stack.append(elem)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def getTop(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False


# stack = Stack()
# stack.pop()
