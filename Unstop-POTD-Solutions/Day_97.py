import sys
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline


class RollbackDSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.stack = []

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            self.stack.append((-1, -1))
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        self.stack.append((a, b))

    def rollback(self, snap):
        while len(self.stack) > snap:
            a, b = self.stack.pop()
            if a == -1:
                continue
            self.size[a] -= self.size[b]
            self.parent[b] = b


n = int(input())
m = int(input())

edges = []
for _ in range(m):
    a, b, l, r = map(int, input().split())
    edges.append((a, b, l, r))

q = int(input())
queries = []
times = []
for i in range(q):
    x, y, t = map(int, input().split())
    queries.append((x, y, t, i))
    times.append(t)

uniq = sorted(set(times))
k = len(uniq)

time_queries = [[] for _ in range(k)]
for x, y, t, idx in queries:
    pos = bisect_left(uniq, t)
    time_queries[pos].append((x, y, idx))

if k == 0:
    sys.exit()

seg = [[] for _ in range(4 * k)]


def add(node, l, r, ql, qr, edge):
    if ql <= l and r <= qr:
        seg[node].append(edge)
        return
    mid = (l + r) // 2
    if ql <= mid:
        add(node * 2, l, mid, ql, qr, edge)
    if qr > mid:
        add(node * 2 + 1, mid + 1, r, ql, qr, edge)


for a, b, l, r in edges:
    left = bisect_left(uniq, l)
    right = bisect_right(uniq, r) - 1
    if left <= right:
        add(1, 0, k - 1, left, right, (a, b))

dsu = RollbackDSU(n)
ans = ["NO"] * q


def dfs(node, l, r):
    snap = len(dsu.stack)
    for a, b in seg[node]:
        dsu.union(a, b)

    if l == r:
        for x, y, idx in time_queries[l]:
            ans[idx] = "YES" if dsu.find(x) == dsu.find(y) else "NO"
    else:
        mid = (l + r) // 2
        dfs(node * 2, l, mid)
        dfs(node * 2 + 1, mid + 1, r)

    dsu.rollback(snap)


dfs(1, 0, k - 1)
print("\n".join(ans))