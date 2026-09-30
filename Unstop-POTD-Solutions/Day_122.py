import sys
from collections import deque

input = sys.stdin.readline

n, L = map(int, input().split())
a = list(map(int, input().split()))

min_q = deque()
max_q = deque()

left = 0
window_sum = 0
ans = 0

for right in range(n):
    window_sum += a[right]

    while min_q and a[min_q[-1]] >= a[right]:
        min_q.pop()
    min_q.append(right)

    while max_q and a[max_q[-1]] <= a[right]:
        max_q.pop()
    max_q.append(right)

    while a[max_q[0]] - a[min_q[0]] > L:
        window_sum -= a[left]

        if min_q[0] == left:
            min_q.popleft()
        if max_q[0] == left:
            max_q.popleft()

        left += 1

    ans = max(ans, window_sum)

print(ans)