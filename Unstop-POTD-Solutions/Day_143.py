import sys

input = sys.stdin.readline

n, m = map(int, input().split())
value = [0] + list(map(int, input().split()))

parent = list(range(n + 1))
size = [1] * (n + 1)

# Each component stores (-value, index)
heaps = [[] for _ in range(n + 1)]

import heapq

for i in range(1, n + 1):
    if value[i] > 0:
        heaps[i].append((-value[i], i))


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(u, v):
    ru = find(u)
    rv = find(v)

    if ru == rv:
        return

    if size[ru] < size[rv]:
        ru, rv = rv, ru

    parent[rv] = ru
    size[ru] += size[rv]

    if len(heaps[ru]) < len(heaps[rv]):
        heaps[ru], heaps[rv] = heaps[rv], heaps[ru]

    for item in heaps[rv]:
        heapq.heappush(heaps[ru], item)

    heaps[rv] = []


out = []

for _ in range(m):
    parts = input().split()

    if parts[0] == "LINK":
        u = int(parts[1])
        v = int(parts[2])
        union(u, v)

    else:
        x = int(parts[1])
        root = find(x)

        if not heaps[root]:
            out.append("EMPTY")
        else:
            neg_val, chamber = heapq.heappop(heaps[root])
            out.append(f"{chamber} {-neg_val}")

print("\n".join(out))