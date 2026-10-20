import sys
from collections import Counter

def solve():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    categories = list(map(int, input().split()))

    edges = []
    for _ in range(m):
        u, v, cost = map(int, input().split())
        edges.append((cost, u - 1, v - 1))

    edges.sort()

    parent = list(range(n))
    size = [1] * n
    members = [[i] for i in range(n)]
    total_cost = 0

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for cost, u, v in edges:
        ru, rv = find(u), find(v)

        if ru == rv:
            continue

        total_cost += cost

        if size[ru] < size[rv]:
            ru, rv = rv, ru

        parent[rv] = ru
        size[ru] += size[rv]
        members[ru].extend(members[rv])
        members[rv] = []

    best_root = 0
    best_size = 0
    best_min = n

    for i in range(n):
        if parent[i] == i:
            component_size = size[i]
            min_vertex = min(members[i])

            if (component_size > best_size or
                (component_size == best_size and min_vertex < best_min)):
                best_size = component_size
                best_min = min_vertex
                best_root = i

    counts = Counter(categories[v] for v in members[best_root])
    best_category, best_count = min(
        counts.items(), key=lambda item: (-item[1], item[0])
    )

    print(total_cost, best_size, best_category, best_count)

if __name__ == "__main__":
    solve()