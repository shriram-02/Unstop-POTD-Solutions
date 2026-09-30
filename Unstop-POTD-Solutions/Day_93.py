import sys

input = sys.stdin.readline

n = int(input())

adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

parent = [0] * (n + 1)
score = [0] * (n + 1)
order = []

stack = [1]
parent[1] = -1

while stack:
    u = stack.pop()
    order.append(u)
    for v, w in adj[u]:
        if v != parent[u]:
            parent[v] = u
            score[v] = score[u] + w
            stack.append(v)

mn = score[:]
mx = score[:]

for u in reversed(order):
    for v, _ in adj[u]:
        if parent[v] == u:
            if mn[v] < mn[u]:
                mn[u] = mn[v]
            if mx[v] > mx[u]:
                mx[u] = mx[v]

q = int(input())
out = []
for _ in range(q):
    v = int(input())
    out.append(str(mx[v] - mn[v]))

sys.stdout.write("\n".join(out))