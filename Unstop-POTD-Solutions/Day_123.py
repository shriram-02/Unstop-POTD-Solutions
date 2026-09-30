import sys
import heapq

def solve():
    input = sys.stdin.readline

    n, m, S, D = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, first, freq, dur = map(int, input().split())
        graph[u].append((v, first, freq, dur))

    INF = 10**30
    dist = [INF] * (n + 1)
    dist[S] = 0

    pq = [(0, S)]

    while pq:
        time, u = heapq.heappop(pq)

        if time != dist[u]:
            continue

        if u == D:
            print(time)
            return

        for v, first, freq, dur in graph[u]:

            if freq == 0:
                if first < time:
                    continue
                depart = first
            else:
                if time <= first:
                    depart = first
                else:
                    k = (time - first + freq - 1) // freq
                    depart = first + k * freq

            arrival = depart + dur

            if arrival < dist[v]:
                dist[v] = arrival
                heapq.heappush(pq, (arrival, v))

    print(-1)

solve()