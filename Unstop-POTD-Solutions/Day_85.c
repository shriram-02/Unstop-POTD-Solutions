#include <stdio.h>
#include <string.h>

#define MAXN 17
#define INF 1000000000000000000LL

long long dist[MAXN][MAXN];
long long dp[1 << 16][16];

int main() {
    int N;
    scanf("%d", &N);

    for (int i = 0; i <= N; i++) {
        for (int j = 0; j <= N; j++) {
            scanf("%lld", &dist[i][j]);
        }
    }

    int totalMask = 1 << N;

    for (int i = 0; i < totalMask; i++)
        for (int j = 0; j < N; j++)
            dp[i][j] = INF;

    for (int i = 0; i < N; i++) {
        dp[1 << i][i] = dist[0][i + 1];
    }

    for (int mask = 1; mask < totalMask; mask++) {
        for (int last = 0; last < N; last++) {
            if (!(mask & (1 << last))) continue;
            if (dp[mask][last] == INF) continue;

            for (int nxt = 0; nxt < N; nxt++) {
                if (mask & (1 << nxt)) continue;

                int newMask = mask | (1 << nxt);
                long long cost = dp[mask][last] + dist[last + 1][nxt + 1];

                if (cost < dp[newMask][nxt])
                    dp[newMask][nxt] = cost;
            }
        }
    }

    long long ans = INF;
    int fullMask = totalMask - 1;

    for (int last = 0; last < N; last++) {
        long long cost = dp[fullMask][last] + dist[last + 1][0];
        if (cost < ans)
            ans = cost;
    }

    printf("%lld\n", ans);

    return 0;
}