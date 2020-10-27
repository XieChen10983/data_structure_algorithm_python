"""
此代码使用栈来解决括号的匹配问题
"""

from stack import Stack


def isCorrespond(string: str):
    left = ['[', '{', '(']
    # right = ['}', '}', ')']
    pair = ["[]", "{}", "()"]
    stack = Stack()
    for symbol in string:
        if symbol in left:
            stack.append(symbol)
        else:
            leftSymbol = stack.pop()
            if leftSymbol is None:
                return False
            elif leftSymbol + symbol in pair:
                continue
            else:
                return False

    if stack.is_empty():
        return True
    else:
        return False


symbols1 = "[]{}(){"
symbols2 = "[{()}]"
symbols3 = "[{}]"
symbols4 = "[{]}"
symbols5 = "]{]}"
print(isCorrespond(symbols1))
print(isCorrespond(symbols2))
print(isCorrespond(symbols3))
print(isCorrespond(symbols4))
print(isCorrespond(symbols5))
