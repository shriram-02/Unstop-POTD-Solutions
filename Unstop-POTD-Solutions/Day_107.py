import sys
import heapq

input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

best = [-1] * (n + 1)
pq = []

for _ in range(k):
    t, p = map(int, input().split())

    if p > best[t]:
        best[t] = p
        heapq.heappush(pq, (-p, t))

while pq:
    neg_power, u = heapq.heappop(pq)
    power = -neg_power

    if power != best[u]:
        continue

    if power == 0:
        continue

    for v in graph[u]:
        new_power = power - 1

        if new_power > best[v]:
            best[v] = new_power
            heapq.heappush(pq, (-new_power, v))

print(sum(x >= 0 for x in best[1:]))