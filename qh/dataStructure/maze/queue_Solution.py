# coding=gbk
"""
此代码使用栈来实现走迷宫的问题
"""
from collections import deque

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
directions = [
    lambda x, y: (x+1, y),
    lambda x, y: (x, y+1),
    lambda x, y: (x-1, y),
    lambda x, y: (x, y-1),
]


def print_r(path):
    curNode = path[-1]

    realPath = []

    while curNode[2] != -1:
        realPath.append((curNode[0], curNode[1]))
        curNode = path[curNode[2]]
    realPath.append(curNode[0:2])  # 将起点放入
    realPath.reverse()
    for node in realPath:
        print(node)


def maze_path(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1, -1))  # 三维的元组信息包括坐标信息和前一个节点的信息
    path = []
    while len(queue) > 0:
        curNode = queue.pop()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            print_r(path)
            return True

        for direction in directions:
            nextNode = direction(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0], nextNode[1], len(path) - 1))
                maze[nextNode[0]][nextNode[1]] = 2
    else:
        print('No path exists.')
        return False


maze_path(1, 1, 8, 8)
