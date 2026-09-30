import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

values = set(x for x in arr if x != -1)

# Check the closest value below K first
for x in sorted(values, reverse=True):
    if x >= K:
        continue

    y = 2 * K - x

    if y in values:
        print(x, y)
        break
else:
    print(-1)