import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
h = data[1:]

ans = [0] * n
stack = []

for i in range(n - 1, -1, -1):
    while stack and h[stack[-1]] <= h[i]:
        stack.pop()

    if stack:
        ans[i] = stack[-1] - i
    else:
        ans[i] = n - 1 - i

    stack.append(i)

print(*ans)