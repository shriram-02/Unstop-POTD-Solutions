import sys
import heapq

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
jobs = []

idx = 1
for _ in range(n):
    t = data[idx]
    d = data[idx + 1]
    jobs.append((d, t))
    idx += 2

jobs.sort()

total = 0
heap = []

for d, t in jobs:
    total += t
    heapq.heappush(heap, -t)
    if total > d:
        total += heapq.heappop(heap)

print(len(heap))