from collections import deque

n, m = map(int, input().split())

q = deque()
present = [False] * (n + 1)
next_id = 1

for _ in range(m):
    op = input().split()

    if op[0] == 'A':
        q.append(next_id)
        present[next_id] = True
        next_id += 1

    elif op[0] == 'P':
        x = int(op[1])
        if present[x]:
            q.remove(x)
            q.appendleft(x)

    else:  # B
        if q:
            x = q.popleft()
            present[x] = False
            print(x)
        else:
            print(0)