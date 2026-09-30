# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import math

input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))

block = int(math.sqrt(n))

queries = []
for i in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    queries.append((l, r, i))

queries.sort(key=lambda x: (x[0] // block, x[1] if (x[0] // block) % 2 == 0 else -x[1]))

freq = {}
cur = 0
ans = [0] * q

cl, cr = 0, -1

for l, r, idx in queries:
    while cr < r:
        cr += 1
        x = arr[cr]
        f = freq.get(x, 0)
        cur -= f * f
        f += 1
        freq[x] = f
        cur += f * f

    while cr > r:
        x = arr[cr]
        f = freq[x]
        cur -= f * f
        f -= 1
        if f:
            freq[x] = f
            cur += f * f
        else:
            del freq[x]
        cr -= 1

    while cl < l:
        x = arr[cl]
        f = freq[x]
        cur -= f * f
        f -= 1
        if f:
            freq[x] = f
            cur += f * f
        else:
            del freq[x]
        cl += 1

    while cl > l:
        cl -= 1
        x = arr[cl]
        f = freq.get(x, 0)
        cur -= f * f
        f += 1
        freq[x] = f
        cur += f * f

    ans[idx] = cur

print("\n".join(map(str, ans)))