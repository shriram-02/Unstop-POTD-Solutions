stack = []

n = int(input())

for _ in range(n):
    op = input().split()
    if op[0] == "ADD":
        stack.append(int(op[1]))
    else:
        if stack:
            stack.pop()

if stack:
    print(stack[-1])
else:
    print(-1)