import sys
from bisect import bisect_left

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); q = int(data[1]); K = int(data[2])
    a = list(map(int, data[3:3 + n]))

    # 1) earliest valid start for each end, two pointers + monotonic stacks
    #    (lists with head pointers instead of deque, for speed)
    left = [0] * (n + 1)          # 1-based: left[i] for end i
    mx = [0] * n; mxh = 0; mxt = 0
    mn = [0] * n; mnh = 0; mnt = 0
    s = 0
    for i in range(n):
        v = a[i]
        while mxt > mxh and a[mx[mxt - 1]] <= v:
            mxt -= 1
        mx[mxt] = i; mxt += 1
        while mnt > mnh and a[mn[mnt - 1]] >= v:
            mnt -= 1
        mn[mnt] = i; mnt += 1
        while a[mx[mxh]] - a[mn[mnh]] > K:
            s += 1
            if mx[mxh] < s:
                mxh += 1
            if mn[mnh] < s:
                mnh += 1
        left[i + 1] = s + 1

    # lens and prefix sums (1-based)
    lens = [0] * (n + 1)
    pre = [0] * (n + 1)
    acc = 0
    for i in range(1, n + 1):
        ln = i - left[i] + 1
        lens[i] = ln
        acc += ln
        pre[i] = acc

    # 2) sparse table for range max of lens
    sp = [lens]
    j = 1
    while (1 << j) <= n:
        prev = sp[-1]
        h = 1 << (j - 1)
        sp.append([x if x > y else y for x, y in zip(prev, prev[h:])])
        j += 1

    # 3) answer queries
    out = []
    pos = 3 + n
    for _ in range(q):
        l = int(data[pos]); r = int(data[pos + 1]); pos += 2
        # first index p >= l with left[p] >= l  (left is non-decreasing)
        p = bisect_left(left, l, l, r + 1)
        m = p - l                         # clipped ends: l .. p-1
        cnt = m * (m + 1) // 2
        best = m
        if p <= r:
            cnt += pre[r] - pre[p - 1]
            k = (r - p + 1).bit_length() - 1
            row = sp[k]
            x = row[p]; y = row[r - (1 << k) + 1]
            if y > x: x = y
            if x > best: best = x
        out.append(f"{cnt} {best}")

    sys.stdout.write("\n".join(out) + "\n")

main()