def count_arrangements(n, k, sightings):
    MOD = 1000000007

    dp = [0] * (n + 1)
    prefix_dp = [0] * (n + 2)

    dp[0] = 1
    prefix_dp[1] = 1

    left = 0
    window_sum = 0

    for right in range(n):
        window_sum += sightings[right]

        while window_sum > k:
            window_sum -= sightings[left]
            left += 1

        dp[right + 1] = (prefix_dp[right + 1] - prefix_dp[left]) % MOD
        prefix_dp[right + 2] = (prefix_dp[right + 1] + dp[right + 1]) % MOD

    return dp[n]


def main():
    n, k = map(int, input().split())
    sightings = list(map(int, input().split()))
    result = count_arrangements(n, k, sightings)
    print(result)


if __name__ == '__main__':
    main()