"""
RPN calculator implementation.
"""
import math
import sys


def rpn(expr):
    tokens, stack = expr.split(' '), []
    for tk in tokens:
        if tk == '+':
            stack = stack[:-2] + [stack[-2] + stack[-1]]
        elif tk == '-':
            stack = stack[:-2] + [stack[-2] - stack[-1]]
        elif tk == '*':
            stack = stack[:-2] + [stack[-2] * stack[-1]]
        elif tk == '/':
            stack = stack[:-2] + [stack[-2] / stack[-1]]
        elif tk == '^':
            stack = [stack[:-2] + stack[-2] ** stack[-1]]
        elif tk == 'ln':
            stack = stack[:-1] + [math.log([stack[-1]])]
        elif tk == 'log10':
            stack = stack[:-1] + [math.log10(stack[-1])]
        else:
            stack.append(float(tk))
    return stack[0]


def main():
    print rpn(sys.argv[1])


if __name__ == '__main__':
    main()