from collections import deque

# Read input
n, d = map(int, input().split())
arr = list(map(int, input().split()))

# Deques to maintain min and max in the current window
min_deque = deque()
max_deque = deque()

left = 0
max_len = 0

for right in range(n):
    # Maintain max_deque (decreasing order)
    while max_deque and arr[max_deque[-1]] < arr[right]:
        max_deque.pop()
    max_deque.append(right)

    # Maintain min_deque (increasing order)
    while min_deque and arr[min_deque[-1]] > arr[right]:
        min_deque.pop()
    min_deque.append(right)

    # Shrink window if condition violated
    while arr[max_deque[0]] - arr[min_deque[0]] > d:
        left += 1
        if max_deque[0] < left:
            max_deque.popleft()
        if min_deque[0] < left:
            min_deque.popleft()

    # Update maximum length
    max_len = max(max_len, right - left + 1)

print(max_len)
