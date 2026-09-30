from collections import deque

# Read input
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Deques to maintain indices of min and max
minDeque, maxDeque = deque(), deque()

best_imbalance = float('inf')
best_pos = -1

for i in range(n):
    # Maintain minDeque (increasing order)
    while minDeque and arr[minDeque[-1]] >= arr[i]:
        minDeque.pop()
    minDeque.append(i)

    # Maintain maxDeque (decreasing order)
    while maxDeque and arr[maxDeque[-1]] <= arr[i]:
        maxDeque.pop()
    maxDeque.append(i)

    # Remove indices out of current window
    if minDeque[0] <= i - m:
        minDeque.popleft()
    if maxDeque[0] <= i - m:
        maxDeque.popleft()

    # When we have a full window
    if i >= m - 1:
        imbalance = arr[maxDeque[0]] - arr[minDeque[0]]
        start_pos = i - m + 1 + 1  # +1 for 1-indexing
        if imbalance < best_imbalance:
            best_imbalance = imbalance
            best_pos = start_pos

print(best_imbalance, best_pos)
