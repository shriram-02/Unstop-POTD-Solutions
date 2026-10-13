# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

def main():
    input = sys.stdin.readline
    N, E, Q = map(int, input().split())

    names = [input().strip() for _ in range(N)]
    ward_id = {name: i for i, name in enumerate(names)}

    edges = []
    for _ in range(E):
        u, v, cost = input().split()
        edges.append((int(cost), ward_id[u], ward_id[v]))

    queries = []
    for i in range(Q):
        ward, cap = input().split()
        queries.append((int(cap), i, ward_id[ward]))

    edges.sort()
    queries.sort()

    parent = list(range(N))
    size = [1] * N

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a = find(a)
        b = find(b)

        if a == b:
            return

        if size[a] < size[b]:
            a, b = b, a

        parent[b] = a
        size[a] += size[b]

    ans = [0] * Q
    j = 0

    for cap, idx, ward in queries:
        while j < E and edges[j][0] <= cap:
            _, u, v = edges[j]
            union(u, v)
            j += 1

        ans[idx] = size[find(ward)]

    sys.stdout.write("\n".join(map(str, ans)))

if __name__ == "__main__":
    main()
