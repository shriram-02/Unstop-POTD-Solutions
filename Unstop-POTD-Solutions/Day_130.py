import sys

input = sys.stdin.readline

n = int(input())

LOG = n.bit_length()

adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

up = [[0] * (n + 1) for _ in range(LOG)]
depth = [0] * (n + 1)
dist = [0] * (n + 1)

stack = [1]
parent = [0] * (n + 1)

while stack:
    u = stack.pop()

    for v, w in adj[u]:
        if v == parent[u]:
            continue

        parent[v] = u
        depth[v] = depth[u] + 1
        dist[v] = dist[u] + w
        stack.append(v)

up[0] = parent[:]

for j in range(1, LOG):
    prev = up[j - 1]
    curr = up[j]

    for i in range(1, n + 1):
        curr[i] = prev[prev[i]]


def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a

    diff = depth[a] - depth[b]
    bit = 0

    while diff:
        if diff & 1:
            a = up[bit][a]
        diff >>= 1
        bit += 1

    if a == b:
        return a

    for j in range(LOG - 1, -1, -1):
        if up[j][a] != up[j][b]:
            a = up[j][a]
            b = up[j][b]

    return up[0][a]


q = int(input())
out = []

for _ in range(q):
    x, y = map(int, input().split())

    p = lca(x, y)

    years = dist[x] + dist[y] - 2 * dist[p]
    rulers = depth[x] + depth[y] - 2 * depth[p] + 1

    out.append(f"{years} {rulers}")

sys.stdout.write("\n".join(out))