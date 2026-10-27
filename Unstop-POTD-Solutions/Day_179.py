
import sys

def main():
    input = sys.stdin.readline
    q = int(input())
    stack = []
    freq = {}
    distinct = 0
    result = []

    for _ in range(q):
        op = input().split()

        if op[0] == '+':
            g = int(op[1])
            stack.append(g)
            if freq.get(g, 0) == 0:
                distinct += 1
            freq[g] = freq.get(g, 0) + 1

        elif op[0] == '-':
            g = stack.pop()
            freq[g] -= 1
            if freq[g] == 0:
                distinct -= 1
                del freq[g]

        else:
            top = stack[-1] if stack else 0
            result.append(f"{top} {distinct}")

    print('\n'.join(result))

if __name__ == "__main__":
    main()
