import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
arr = list(map(int, input().split()))

# Coordinate compression for rank queries
values = sorted(set(arr))
compressed = {v: i + 1 for i, v in enumerate(values)}
M = len(values)

# Fenwick Tree for flagged instruments
flag_bit = [0] * (N + 1)
flagged = [False] * (N + 1)

def update(i, delta):
    while i <= N:
        flag_bit[i] += delta
        i += i & -i

def query(i):
    total = 0
    while i > 0:
        total += flag_bit[i]
        i -= i & -i
    return total

# Merge-sort tree for range kth smallest
tree = [[] for _ in range(4 * N)]

def build(node, left, right):
    if left == right:
        tree[node] = [arr[left]]
        return

    mid = (left + right) // 2
    build(node * 2, left, mid)
    build(node * 2 + 1, mid + 1, right)

    a = tree[node * 2]
    b = tree[node * 2 + 1]

    i = j = 0
    merged = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    merged.extend(a[i:])
    merged.extend(b[j:])
    tree[node] = merged

def count_leq(node, left, right, ql, qr, value):
    if qr < left or right < ql:
        return 0

    if ql <= left and right <= qr:
        import bisect
        return bisect.bisect_right(tree[node], value)

    mid = (left + right) // 2
    return (
        count_leq(node * 2, left, mid, ql, qr, value)
        + count_leq(node * 2 + 1, mid + 1, right, ql, qr, value)
    )

build(1, 0, N - 1)

import bisect

def kth_smallest(l, r, k):
    low = 0
    high = M - 1

    while low < high:
        mid = (low + high) // 2
        cnt = count_leq(
            1, 0, N - 1, l, r, values[mid]
        )

        if cnt >= k:
            high = mid
        else:
            low = mid + 1

    return values[low]

output = []

for _ in range(Q):
    parts = input().split()
    command = parts[0]

    if command == "FLAG":
        i = int(parts[1])

        if flagged[i] is False:
            flagged[i] = True
            update(i, 1)
        else:
            flagged[i] = False
            update(i, -1)

    elif command == "AUDIT":
        l = int(parts[1])
        r = int(parts[2])

        output.append(str(query(r) - query(l - 1)))

    elif command == "RANK":
        l = int(parts[1])
        r = int(parts[2])
        k = int(parts[3])

        output.append(str(kth_smallest(l - 1, r - 1, k)))

sys.stdout.write("\n".join(output))