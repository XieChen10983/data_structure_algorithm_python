# coding=gbk
"""
此代码使用栈来实现走迷宫的问题
"""

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


def maze_path(x1, y1, x2, y2):
    stack = [(x1, y1)]
    while len(stack) > 0:
        curNode = stack[-1]  # 当前的节点
        if curNode[0] == x2 and curNode[1] == y2:
            for p in stack:
                print(p)
            return True
        for direction in directions:
            nextNode = direction(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:  # 如果下一个节点能走
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2  # 标记已经走过了
                break  # 只要找到一个就不继续找其他方向的了
        else:
            maze[curNode[0]][curNode[1]] = 2
            stack.pop()
    else:
        print("No path exists.")
        return False


maze_path(1, 1, 8, 8)
