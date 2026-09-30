# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

input = sys.stdin.readline

class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0]*(n+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        return True

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))

    edges.sort()
    dsu = DSU(n)
    total = 0
    used = 0

    for w, u, v in edges:
        if dsu.unite(u, v):
            total += w
            used += 1

    if used == n - 1:
        print(total)
    else:
        print(-1)

if __name__ == "__main__":
    main()
