# coding=gbk
"""
用树模拟目录
"""


class Node:
    def __init__(self, name, Type='dir'):
        self.name = name
        self.type = Type  # dir or file
        self.children = []
        self.parent = None

    def __repr__(self):
        return self.name


# n = Node("hello")
# n2 = Node("world")
# n.children.append(n2)  # n2作为n的子节点
# n2.parent = n  # n作为n2的父节点


class FileSystemTree:
    def __init__(self):
        self.root = Node("/")
        self.currentDir = self.root

    def mkdir(self, name: str):
        if not name.endswith("/"):
            name += "/"
        node = Node(name)
        self.currentDir.children.append(node)
        node.parent = self.currentDir

    def ls(self):
        return self.currentDir.children

    def cd(self, name: str):
        if not name.endswith('/'):
            name += '/'
        if name == '../':
            self.currentDir = self.currentDir.parent
            return
        for child in self.currentDir.children:
            if child.name == name:
                self.currentDir = child
                return
        raise ValueError("invalid dirName.")


tree = FileSystemTree()
tree.mkdir("var/")
tree.mkdir("bin/")
tree.mkdir("usr/")
print(tree.ls())

tree.cd('bin')
print(tree.currentDir)
tree.mkdir('python/')
print(tree.ls())
tree.cd('python')
print(tree.currentDir)
