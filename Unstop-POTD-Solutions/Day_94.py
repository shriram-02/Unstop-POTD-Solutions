import sys

MOD = 1000000007

input = sys.stdin.readline

n = int(input())
m = int(input())

parent = list(range(n + 1))
size = [1] * (n + 1)
weight = [1] * (n + 1)  # node -> parent


def find(x):
    if parent[x] != x:
        p = parent[x]
        root = find(p)
        weight[x] = (weight[x] * weight[p]) % MOD
        parent[x] = root
    return parent[x]


def inv(x):
    return pow(x, MOD - 2, MOD)


out = []

for _ in range(m):
    arr = list(map(int, input().split()))

    if arr[0] == 1:
        _, u, v, p, q = arr
        r = (p * inv(q)) % MOD

        ru = find(u)
        rv = find(v)
        wu = weight[u]
        wv = weight[v]

        if ru == rv:
            cur = (wu * inv(wv)) % MOD
            if cur == r:
                out.append("OK")
            else:
                out.append("CONTRADICTION")
        else:
            if size[ru] < size[rv]:
                parent[ru] = rv
                weight[ru] = (r * wv % MOD) * inv(wu) % MOD
                size[rv] += size[ru]
            else:
                parent[rv] = ru
                weight[rv] = (wu * inv((r * wv) % MOD)) % MOD
                size[ru] += size[rv]
            out.append("OK")

    else:
        _, u, v = arr
        if u == v:
            out.append("1")
            continue

        ru = find(u)
        rv = find(v)

        if ru != rv:
            out.append("UNKNOWN")
        else:
            ans = (weight[u] * inv(weight[v])) % MOD
            out.append(str(ans))

print("\n".join(out))