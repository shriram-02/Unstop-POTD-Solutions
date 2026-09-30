import sys
from functools import lru_cache

input = sys.stdin.readline

N = int(input())
m = 2 * N

a = [list(map(int, input().split())) for _ in range(m)]

@lru_cache(None)
def dp(mask):
    if mask == (1 << m) - 1:
        return 0

    i = 0
    while mask & (1 << i):
        i += 1

    ans = 0
    new_mask = mask | (1 << i)

    for j in range(i + 1, m):
        if not (mask & (1 << j)):
            ans = max(ans, a[i][j] + dp(new_mask | (1 << j)))

    return ans

print(dp(0))