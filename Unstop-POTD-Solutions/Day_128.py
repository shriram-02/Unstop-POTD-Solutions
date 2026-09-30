import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

q = int(input())
queries = []

for i in range(q):
    l, r = map(int, input().split())
    queries.append((l, r, i))

queries.sort(key=lambda x: x[1])

bit = [0] * (n + 1)
last = {}
ans = [0] * q

def update(i, val):
    while i <= n:
        bit[i] += val
        i += i & -i

def query(i):
    res = 0
    while i > 0:
        res += bit[i]
        i -= i & -i
    return res

idx = 0

for l, r, qi in queries:
    while idx < r:
        idx += 1
        x = arr[idx - 1]

        if x in last:
            update(last[x], -1)

        update(idx, 1)
        last[x] = idx

    ans[qi] = query(r) - query(l - 1)

sys.stdout.write("\n".join(map(str, ans)))