import sys
import heapq

def solve():
    input = sys.stdin.buffer.readline

    n, m, R = map(int, input().split())

    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v, fuel, turb = map(int, input().split())
        graph[u - 1].append((v - 1, fuel, turb))

    INF = 10**18
    K = R + 1

    dist = [[INF] * K for _ in range(n)]
    dist[0][0] = 0

    pq = [(0, 0, 0)]

    while pq:
        d, u, used = heapq.heappop(pq)

        if d != dist[u][used]:
            continue

        for v, fuel, turb in graph[u]:
            new_used = used + turb

            if new_used > R:
                continue

            new_dist = d + fuel

            if new_dist < dist[v][new_used]:
                dist[v][new_used] = new_dist
                heapq.heappush(pq, (new_dist, v, new_used))

    # Convert exact turbulence costs into
    # minimum fuel for turbulence <= tolerance.
    for v in range(n):
        for t in range(1, K):
            dist[v][t] = min(dist[v][t], dist[v][t - 1])

    q = int(input())
    out = []

    for _ in range(q):
        dest, tol = map(int, input().split())
        ans = dist[dest - 1][tol]

        out.append(str(ans) if ans < INF else "-1")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()import sys
import heapq

def solve():
    input = sys.stdin.buffer.readline

    n, m, R = map(int, input().split())

    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v, fuel, turb = map(int, input().split())
        graph[u - 1].append((v - 1, fuel, turb))

    INF = 10**18
    K = R + 1

    dist = [[INF] * K for _ in range(n)]
    dist[0][0] = 0

    pq = [(0, 0, 0)]

    while pq:
        d, u, used = heapq.heappop(pq)

        if d != dist[u][used]:
            continue

        for v, fuel, turb in graph[u]:
            new_used = used + turb

            if new_used > R:
                continue

            new_dist = d + fuel

            if new_dist < dist[v][new_used]:
                dist[v][new_used] = new_dist
                heapq.heappush(pq, (new_dist, v, new_used))

    # Convert exact turbulence costs into
    # minimum fuel for turbulence <= tolerance.
    for v in range(n):
        for t in range(1, K):
            dist[v][t] = min(dist[v][t], dist[v][t - 1])

    q = int(input())
    out = []

    for _ in range(q):
        dest, tol = map(int, input().split())
        ans = dist[dest - 1][tol]

        out.append(str(ans) if ans < INF else "-1")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()