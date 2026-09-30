import sys
import heapq

input = sys.stdin.readline

n = int(input())
intervals = []

for _ in range(n):
    s, e = map(int, input().split())
    intervals.append((s, e))

intervals.sort()

heap = []

for s, e in intervals:
    if heap and heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap, e)

print(len(heap))