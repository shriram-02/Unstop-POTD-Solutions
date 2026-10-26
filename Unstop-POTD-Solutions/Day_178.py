
import sys
from bisect import bisect_left


def suffix_totals(a):
    n = len(a)
    ng = [n] * n
    ns = [n] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and a[stack[-1]] <= a[i]:
            stack.pop()
        ng[i] = stack[-1] if stack else n
        stack.append(i)

    stack = []
    for i in range(n - 1, -1, -1):
        while stack and a[stack[-1]] >= a[i]:
            stack.pop()
        ns[i] = stack[-1] if stack else n
        stack.append(i)

    mx = [0] * n
    mn = [0] * n

    for i in range(n - 1, -1, -1):
        j = ng[i]
        mx[i] = (j - i) * a[i] + (mx[j] if j < n else 0)

        j = ns[i]
        mn[i] = (j - i) * a[i] + (mn[j] if j < n else 0)

    result = [0] * n
    running = 0

    for i in range(n - 1, -1, -1):
        running += mx[i] - mn[i]
        result[i] = running

    return result


def prefix_totals(a):
    n = len(a)
    pg = [-1] * n
    ps = [-1] * n
    stack = []

    for i in range(n):
        while stack and a[stack[-1]] <= a[i]:
            stack.pop()
        pg[i] = stack[-1] if stack else -1
        stack.append(i)

    stack = []
    for i in range(n):
        while stack and a[stack[-1]] >= a[i]:
            stack.pop()
        ps[i] = stack[-1] if stack else -1
        stack.append(i)

    mx = [0] * n
    mn = [0] * n
    result = [0] * n
    running = 0

    for i in range(n):
        j = pg[i]
        mx[i] = (i - j) * a[i] + (mx[j] if j >= 0 else 0)

        j = ps[i]
        mn[i] = (i - j) * a[i] + (mn[j] if j >= 0 else 0)

        running += mx[i] - mn[i]
        result[i] = running

    return result


class PairMax:


    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

        self.px = [0]
        for x in X:
            self.px.append(self.px[-1] + x)

        self.py = [0]
        for y in Y:
            self.py.append(self.py[-1] + y)

        self.base = [0]
        j = 0

        for x in X:
            while j < len(Y) and Y[j] <= x:
                j += 1
            self.base.append(
                self.base[-1] + x * j - self.py[j]
            )

    def query(self, p, q):
        split = min(p, bisect_left(self.X, self.Y[q - 1]))

        return (
            self.base[split]
            + split * self.py[q]
            + q * (self.px[p] - self.px[split])
        )


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    pos = 0
    n = data[pos]
    pos += 1

    a = data[pos:pos + n]
    pos += n

    q = data[pos]
    pos += 1

    queries = []
    for i in range(q):
        L = data[pos] - 1
        R = data[pos + 1] - 1
        pos += 2
        queries.append((L, R, i))

    answers = [0] * q

    def solve(lo, hi, ids):
        if not ids:
            return

        if lo == hi:
            for qi in ids:
                answers[qi] = 0
            return

        mid = (lo + hi) // 2
        left_ids = []
        right_ids = []
        crossing = []

        for qi in ids:
            L, R, _ = queries[qi]

            if R <= mid:
                left_ids.append(qi)
            elif L > mid:
                right_ids.append(qi)
            else:
                crossing.append(qi)

        if crossing:
            left = a[lo:mid + 1]
            right = a[mid + 1:hi + 1]

            left_total = suffix_totals(left)
            right_total = prefix_totals(right)

            left_max = []
            left_min = []
            cur_max = -10**30
            cur_min = 10**30

            for i in range(mid, lo - 1, -1):
                cur_max = max(cur_max, a[i])
                cur_min = min(cur_min, a[i])
                left_max.append(cur_max)
                left_min.append(cur_min)

            right_max = []
            right_min = []
            cur_max = -10**30
            cur_min = 10**30

            for i in range(mid + 1, hi + 1):
                cur_max = max(cur_max, a[i])
                cur_min = min(cur_min, a[i])
                right_max.append(cur_max)
                right_min.append(cur_min)

            max_pairs = PairMax(left_max, right_max)

            neg_min_pairs = PairMax(
                [-x for x in left_min],
                [-x for x in right_min]
            )

            for qi in crossing:
                L, R, _ = queries[qi]
                p = mid - L + 1
                r = R - mid

                cross_total = (
                    max_pairs.query(p, r)
                    + neg_min_pairs.query(p, r)
                )

                answers[qi] = (
                    left_total[L - lo]
                    + right_total[R - (mid + 1)]
                    + cross_total
                )

        del ids
        solve(lo, mid, left_ids)
        solve(mid + 1, hi, right_ids)

    solve(0, n - 1, list(range(q)))

    print(*answers)

    print(answers.index(max(answers)) + 1)


if __name__ == "__main__":
    main()