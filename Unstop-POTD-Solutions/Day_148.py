import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return

        if self.rank[a] < self.rank[b]:
            a, b = b, a

        self.parent[b] = a

        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1


def main():
    input = sys.stdin.readline

    n, m, q = map(int, input().split())

    edges = []
    for _ in range(m):
        u, v, cost = map(int, input().split())
        edges.append((cost, u, v))

    queries = []
    for i in range(q):
        a, b, budget = map(int, input().split())
        queries.append((budget, a, b, i))

    edges.sort()
    queries.sort()

    dsu = DSU(n)
    ans = ["NO"] * q

    j = 0

    for budget, a, b, idx in queries:
        while j < m and edges[j][0] <= budget:
            _, u, v = edges[j]
            dsu.union(u, v)
            j += 1

        if dsu.find(a) == dsu.find(b):
            ans[idx] = "YES"

    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    main()