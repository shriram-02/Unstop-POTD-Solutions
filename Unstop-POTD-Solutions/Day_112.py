# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

def main():
    input = sys.stdin.readline

    n = int(input())
    weights = list(map(int, input().split()))

    stack = []

    for w in weights:
        stack.append(w)

        while len(stack) >= 2 and stack[-1] == stack[-2]:
            x = stack.pop()
            stack.pop()
            stack.append(x + x)

    print(len(stack))
    print(*stack)


if __name__ == "__main__":
    main()

