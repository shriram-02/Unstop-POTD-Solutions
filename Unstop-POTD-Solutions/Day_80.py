# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

input = sys.stdin.readline

INF = 10 ** 18

n, q = map(int, input().split())
a = list(map(int, input().split()))

mx = [0] * (4 * n)
se = [-INF] * (4 * n)
cnt = [0] * (4 * n)
sm = [0] * (4 * n)


def pull(idx):
    sm[idx] = sm[idx * 2] + sm[idx * 2 + 1]
    if mx[idx * 2] > mx[idx * 2 + 1]:
        mx[idx] = mx[idx * 2]
        cnt[idx] = cnt[idx * 2]
        se[idx] = max(se[idx * 2], mx[idx * 2 + 1])
    elif mx[idx * 2] < mx[idx * 2 + 1]:
        mx[idx] = mx[idx * 2 + 1]
        cnt[idx] = cnt[idx * 2 + 1]
        se[idx] = max(mx[idx * 2], se[idx * 2 + 1])
    else:
        mx[idx] = mx[idx * 2]
        cnt[idx] = cnt[idx * 2] + cnt[idx * 2 + 1]
        se[idx] = max(se[idx * 2], se[idx * 2 + 1])


def build(idx, l, r):
    if l == r:
        v = a[l]
        mx[idx] = v
        se[idx] = -INF
        cnt[idx] = 1
        sm[idx] = v
        return
    m = (l + r) // 2
    build(idx * 2, l, m)
    build(idx * 2 + 1, m + 1, r)
    pull(idx)


def apply(idx, x):
    sm[idx] -= (mx[idx] - x) * cnt[idx]
    mx[idx] = x


def push(idx):
    apply_if(idx * 2, mx[idx])
    apply_if(idx * 2 + 1, mx[idx])


def apply_if(idx, x):
    if mx[idx] > x:
        apply(idx, x)


def chmin(idx, l, r, ql, qr, x):
    if r < ql or l > qr or mx[idx] <= x:
        return
    if ql <= l and r <= qr and se[idx] < x:
        apply(idx, x)
        return
    push(idx)
    m = (l + r) // 2
    chmin(idx * 2, l, m, ql, qr, x)
    chmin(idx * 2 + 1, m + 1, r, ql, qr, x)
    pull(idx)


def query(idx, l, r, ql, qr):
    if r < ql or l > qr:
        return 0
    if ql <= l and r <= qr:
        return sm[idx]
    push(idx)
    m = (l + r) // 2
    return query(idx * 2, l, m, ql, qr) + query(idx * 2 + 1, m + 1, r, ql, qr)


build(1, 0, n - 1)

out = []
for _ in range(q):
    t = list(map(int, input().split()))
    if t[0] == 1:
        _, l, r, v = t
        chmin(1, 0, n - 1, l - 1, r - 1, v)
    else:
        _, l, r = t
        out.append(str(query(1, 0, n - 1, l - 1, r - 1)))

print("\n".join(out))