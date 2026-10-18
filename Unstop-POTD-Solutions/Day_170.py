from collections import Counter, deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))

dq = deque()
max_values = []

for i in range(n):
    while dq and dq[0] <= i - k:
        dq.popleft()

    while dq and arr[dq[-1]] <= arr[i]:
        dq.pop()

    dq.append(i)

    if i >= k - 1:
        max_values.append(arr[dq[0]])

freq = Counter(max_values)
dominant = min(freq, key=lambda x: (-freq[x], x))

print(*max_values)
print(dominant, freq[dominant])