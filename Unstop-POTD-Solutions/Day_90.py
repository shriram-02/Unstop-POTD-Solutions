import sys

input = sys.stdin.readline

N, M, Q = map(int, input().split())

INF = 10**18
dist = [[INF] * N for _ in range(N)]

for i in range(N):
    dist[i][i] = 0

for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    if w < dist[u][v]:
        dist[u][v] = w
        dist[v][u] = w

for k in range(N):
    dk = dist[k]
    for i in range(N):
        if dist[i][k] == INF:
            continue
        dik = dist[i][k]
        di = dist[i]
        for j in range(N):
            if dk[j] == INF:
                continue
            if di[j] > dik + dk[j]:
                di[j] = dik + dk[j]

out = []
for _ in range(Q):
    a, b = map(int, input().split())
    ans = dist[a - 1][b - 1]
    out.append(str(ans if ans != INF else -1))

sys.stdout.write("\n".join(out))