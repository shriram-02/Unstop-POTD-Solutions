import sys

input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

parent = [0] * (n + 1)
depth = [0] * (n + 1)
size = [1] * (n + 1)
heavy = [-1] * (n + 1)

order = [1]
parent[1] = -1

for u in order:
    for v in adj[u]:
        if v == parent[u]:
            continue
        parent[v] = u
        depth[v] = depth[u] + 1
        order.append(v)

for u in reversed(order):
    max_size = 0
    for v in adj[u]:
        if parent[v] == u:
            size[u] += size[v]
            if size[v] > max_size:
                max_size = size[v]
                heavy[u] = v


head = [0] * (n + 1)
pos = [0] * (n + 1)
cur_pos = 0

stack = [(1, 1)]

while stack:
    u, h = stack.pop()

    while u != -1:
        head[u] = h
        cur_pos += 1
        pos[u] = cur_pos

        for v in adj[u]:
            if parent[v] == u and v != heavy[u]:
                stack.append((v, v))

        u = heavy[u]


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def range_sum(self, l, r):
        return self.query(r) - self.query(l - 1)


bit = Fenwick(n)

# Every edge is initially electrified.
# The edge feeding node v is represented at pos[v].
for v in range(2, n + 1):
    bit.add(pos[v], 1)

q = int(input())
ans = []

for _ in range(q):
    event = list(map(int, input().split()))

    if event[0] == 1:
        v = event[1]

        # Toggle the edge between v and its parent.
        current = bit.range_sum(pos[v], pos[v])
        bit.add(pos[v], 1 if current == 0 else -1)

    else:
        u, v = event[1], event[2]
        result = 0

        while head[u] != head[v]:
            if depth[head[u]] < depth[head[v]]:
                u, v = v, u

            result += bit.range_sum(pos[head[u]], pos[u])
            u = parent[head[u]]

        if depth[u] > depth[v]:
            u, v = v, u

        # Exclude u itself because its position represents
        # the edge from parent[u] to u.
        if u != v:
            result += bit.range_sum(pos[u] + 1, pos[v])

        ans.append(str(result))

sys.stdout.write("\n".join(ans))