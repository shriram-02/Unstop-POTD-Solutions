import sys

input = sys.stdin.readline

n, B = map(int, input().split())
cost = list(map(int, input().split()))

left = 0
current = 0
ans = 0

for right in range(n):
    current += cost[right]

    while current > B:
        current -= cost[left]
        left += 1

    ans = max(ans, right - left + 1)

print(ans)