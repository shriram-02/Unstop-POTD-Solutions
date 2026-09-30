from collections import deque

n, L = map(int, input().split())
a = list(map(int, input().split()))

min_q = deque()
max_q = deque()

left = 0
ans = 0

for right in range(n):
    while min_q and a[min_q[-1]] >= a[right]:
        min_q.pop()
    min_q.append(right)

    while max_q and a[max_q[-1]] <= a[right]:
        max_q.pop()
    max_q.append(right)

    while a[max_q[0]] - a[min_q[0]] > L:
        if min_q[0] == left:
            min_q.popleft()
        if max_q[0] == left:
            max_q.popleft()
        left += 1

    ans = max(ans, right - left + 1)

print(ans)