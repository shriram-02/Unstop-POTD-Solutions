import heapq

def user_logic(N, M, K, switch_cost, connections):
    graph = [[] for _ in range(N)]
    for u, v, nl, ql in connections:
        graph[u].append((v, nl, ql))
        graph[v].append((u, nl, ql))

    INF = 10**20
    # state: (node, mode, consecutive_quantum)
    # mode: 0 = Normal, 1 = Quantum
    dist = [[[INF] * (K + 1) for _ in range(2)] for _ in range(N)]

    pq = []
    dist[0][0][0] = 0
    heapq.heappush(pq, (0, 0, 0, 0))

    while pq:
        cost, u, mode, cnt = heapq.heappop(pq)

        if cost != dist[u][mode][cnt]:
            continue

        # Switch mode
        if mode == 0:
            ncost = cost + switch_cost[u]
            if ncost < dist[u][1][0]:
                dist[u][1][0] = ncost
                heapq.heappush(pq, (ncost, u, 1, 0))
        else:
            ncost = cost + switch_cost[u]
            if ncost < dist[u][0][0]:
                dist[u][0][0] = ncost
                heapq.heappush(pq, (ncost, u, 0, 0))

        # Traverse edges
        for v, nl, ql in graph[u]:
            if mode == 0:
                ncost = cost + nl
                if ncost < dist[v][0][0]:
                    dist[v][0][0] = ncost
                    heapq.heappush(pq, (ncost, v, 0, 0))
            else:
                if cnt < K:
                    ncost = cost + ql
                    if ncost < dist[v][1][cnt + 1]:
                        dist[v][1][cnt + 1] = ncost
                        heapq.heappush(pq, (ncost, v, 1, cnt + 1))

    ans = INF
    for mode in range(2):
        for cnt in range(K + 1):
            ans = min(ans, dist[N - 1][mode][cnt])

    return -1 if ans == INF else ans


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    N = int(data[0])
    M = int(data[1])
    K = int(data[2])

    switch_cost = list(map(int, data[3:3 + N]))

    connections = []
    idx = 3 + N
    for _ in range(M):
        u = int(data[idx])
        v = int(data[idx + 1])
        nl = int(data[idx + 2])
        ql = int(data[idx + 3])
        connections.append((u, v, nl, ql))
        idx += 4

    print(user_logic(N, M, K, switch_cost, connections))


if __name__ == "__main__":
    main()