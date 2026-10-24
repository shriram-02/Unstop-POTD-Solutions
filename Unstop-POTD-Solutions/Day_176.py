# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import heapq


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])

    size = 1
    while size < n:
        size *= 2
    BIG = 1 << 62

    # Tree 1: a[t] = 1 - (number of kept pieces with clamped deadline t+1).
    # slack(t) = prefix sum of a up to t = free days minus booked pieces.
    # Each node stores (sum, minimum prefix sum inside the node).
    sm = [0] * (2 * size)
    mn = [BIG] * (2 * size)
    for i in range(n):
        sm[size + i] = 1
        mn[size + i] = 1
    for node in range(size - 1, 0, -1):
        l = 2 * node
        sm[node] = sm[l] + sm[l + 1]
        m = sm[l] + mn[l + 1]
        mn[node] = mn[l] if mn[l] < m else m

    def update1(p, delta):
        node = p + size
        v = sm[node] + delta
        sm[node] = v
        mn[node] = v
        node >>= 1
        while node:
            l = 2 * node
            sl = sm[l]
            sm[node] = sl + sm[l + 1]
            m = sl + mn[l + 1]
            ml = mn[l]
            mn[node] = ml if ml < m else m
            node >>= 1

    def find_tight(i):
        """Smallest index t >= i with slack(t) == 0, or -1 if none."""
        acc = 0
        lo, hi = size, i + size
        while lo < hi:
            if lo & 1:
                acc += sm[lo]
                lo += 1
            if hi & 1:
                hi -= 1
                acc += sm[hi]
            lo >>= 1
            hi >>= 1
        lefts = []
        rights = []
        lo, hi = i + size, 2 * size
        while lo < hi:
            if lo & 1:
                lefts.append(lo)
                lo += 1
            if hi & 1:
                hi -= 1
                rights.append(hi)
            lo >>= 1
            hi >>= 1
        rights.reverse()
        for node in lefts + rights:
            if acc + mn[node] <= 0:
                while node < size:
                    l = 2 * node
                    if acc + mn[l] <= 0:
                        node = l
                    else:
                        acc += sm[l]
                        node = l + 1
                return node - size
            acc += sm[node]
        return -1

    # Tree 2: minimum kept weight per deadline position, encoded as w*size+pos.
    t2 = [BIG] * (2 * size)
    heaps = [None] * n

    def refresh2(p):
        h = heaps[p]
        node = p + size
        t2[node] = h[0] * size + p if h else BIG
        node >>= 1
        while node:
            a = t2[2 * node]
            b = t2[2 * node + 1]
            t2[node] = a if a < b else b
            node >>= 1

    def prefix_min2(t):
        res = BIG
        lo, hi = size, t + 1 + size
        while lo < hi:
            if lo & 1:
                if t2[lo] < res:
                    res = t2[lo]
                lo += 1
            if hi & 1:
                hi -= 1
                if t2[hi] < res:
                    res = t2[hi]
            lo >>= 1
            hi >>= 1
        return res

    def push(p, w):
        if heaps[p] is None:
            heaps[p] = []
        heapq.heappush(heaps[p], w)
        refresh2(p)

    total = 0
    out = []
    idx = 1
    for _ in range(n):
        d = int(data[idx])
        w = int(data[idx + 1])
        idx += 2
        i = (d if d < n else n) - 1

        t = find_tight(i)
        if t == -1:
            update1(i, -1)
            push(i, w)
            total += w
        else:
            key = prefix_min2(t)
            mw, x = divmod(key, size)
            if w > mw:
                heapq.heappop(heaps[x])
                refresh2(x)
                update1(x, 1)
                update1(i, -1)
                push(i, w)
                total += w - mw
        out.append(total)

    sys.stdout.write(" ".join(map(str, out)) + "\n")


main()