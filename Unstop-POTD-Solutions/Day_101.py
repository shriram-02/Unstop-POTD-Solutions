import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
q = int(input())

queries = []
values = arr[:]

for _ in range(q):
    parts = input().split()
    op = parts[0]

    if op == 'U':
        i = int(parts[1]) - 1
        v = int(parts[2])
        queries.append(('U', i, v))
        values.append(v)

    elif op == 'C':
        x = int(parts[1])
        queries.append(('C', x))

    else:
        k = int(parts[1])
        queries.append(('K', k))

coords = sorted(set(values))
m = len(coords)
bit = [0] * (m + 1)

def update(pos, delta):
    pos += 1
    while pos <= m:
        bit[pos] += delta
        pos += pos & -pos

def prefix(pos):
    total = 0
    while pos > 0:
        total += bit[pos]
        pos -= pos & -pos
    return total

def kth(k):
    pos = 0
    step = 1 << (m.bit_length() - 1)

    while step:
        nxt = pos + step
        if nxt <= m and bit[nxt] < k:
            pos = nxt
            k -= bit[nxt]
        step >>= 1

    return coords[pos]

for x in arr:
    update(bisect_left(coords, x), 1)

ans = []

for query in queries:
    if query[0] == 'U':
        _, i, v = query

        update(bisect_left(coords, arr[i]), -1)
        arr[i] = v
        update(bisect_left(coords, v), 1)

    elif query[0] == 'C':
        _, x = query
        ans.append(str(prefix(bisect_right(coords, x))))

    else:
        _, k = query
        ans.append(str(kth(k)))

sys.stdout.write('\n'.join(ans))