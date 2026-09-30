import heapq

n = int(input())
jobs = []

for _ in range(n):
    d, c = map(int, input().split())
    jobs.append((d, c))

jobs.sort()

heap = []
total = 0

for deadline, crates in jobs:
    heapq.heappush(heap, crates)
    total += crates

    if len(heap) > deadline:
        total -= heapq.heappop(heap)

print(total)