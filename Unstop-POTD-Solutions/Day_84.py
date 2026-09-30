from collections import deque

n = int(input())
q = deque()

for _ in range(n):
    s = input().split()
    if s[0] == "ENTER":
        q.append(int(s[1]))
    else:
        if q:
            q.popleft()

if q:
    print(q[0])
else:
    print("EMPTY")