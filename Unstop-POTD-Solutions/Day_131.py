# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, m, k, src, dst = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    INF = 10**30
    dist = [[INF] * (k + 1) for _ in range(n + 1)]
    dist[src][0] = 0

    pq = [(0, src, 0)]

    while pq:
        d, u, used = heapq.heappop(pq)

        if d != dist[u][used]:
            continue

        for v, w in graph[u]:
            # Traverse normally
            nd = d + w
            if nd < dist[v][used]:
                dist[v][used] = nd
                heapq.heappush(pq, (nd, v, used))

            # Use a token on this edge
            if used < k and d < dist[v][used + 1]:
                dist[v][used + 1] = d
                heapq.heappush(pq, (d, v, used + 1))

    ans = min(dist[dst])

    print(-1 if ans == INF else ans)

if __name__ == "__main__":
    solve()

