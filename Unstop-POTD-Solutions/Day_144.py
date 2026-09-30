from collections import deque, Counter

n, W = map(int, input().split())
a = list(map(int, input().split()))

freq = Counter()
dq = deque()
ans = []

for i in range(n):
    freq[a[i]] += 1

    while dq and a[dq[-1]] <= a[i]:
        dq.pop()
    dq.append(i)

    if i >= W:
        old = a[i - W]
        freq[old] -= 1
        if freq[old] == 0:
            del freq[old]

        if dq[0] <= i - W:
            dq.popleft()

    if i >= W - 1:
        ans.append(f"{a[dq[0]]} {len(freq)}")

print("\n".join(ans))   