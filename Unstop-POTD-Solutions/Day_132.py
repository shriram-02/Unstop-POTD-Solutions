import sys

def solve():
    input = sys.stdin.readline
    n, w = map(int, input().split())
    energy = list(map(int, input().split()))

    INF = 10**30
    dp = [INF] * n
    dp[0] = energy[0]

    # dp[i] = minimum cost to reach night i as an active night
    for i in range(1, n):
        for j in range(i):
            dp[i] = min(
                dp[i],
                dp[j] + energy[i] + w * (i - j) ** 2
            )

    print(dp[-1])

if __name__ == "__main__":
    solve()