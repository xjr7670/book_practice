# -*- coding:utf-8 -*-

"""
代码主要作用：检测括号是否匹配
"""


from linkedstack import LinkedStack


def bracketsBalance(exp):
    """exp is a string that represents the expression."""
    stk = LinkedStack()
    for ch in exp:
        if ch in ['[' '(']:
            stk.push(ch)
        elif ch in [']', ')']:
            if stk.isEmpty():
                return False
            chFromStack = stk.pop()
            if ch == ']' and chFromStack != '[' or \
                ch == ')' and chFromStack != '(':
                return False
    return stk.isEmpty()


def main():
    exp = input("Enter a bracketed expression: ")
    if bracketsBalance(exp):
        print("OK")
    else:
        print("Not OK")


if __name__ == '__main__':
    main()
