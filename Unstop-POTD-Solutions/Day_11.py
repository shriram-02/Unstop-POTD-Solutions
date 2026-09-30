import sys

def minEnergyCost(energy, N, K):
    dp = [0] * N

    for i in range(1, N):
        min_cost = float('inf')

        # Check all possible jumps up to K
        for j in range(1, min(K, i) + 1):
            cost = dp[i - j] + abs(energy[i] - energy[i - j])
            min_cost = min(min_cost, cost)

        dp[i] = min_cost

    return dp[N - 1]


if __name__ == "__main__":
    input = sys.stdin.readline

    N, K = map(int, input().split())
    energy = list(map(int, input().split()))

    print(minEnergyCost(energy, N, K))