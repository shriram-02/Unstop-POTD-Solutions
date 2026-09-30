import sys
from collections import defaultdict

def solve():
    input = sys.stdin.readline

    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    freq = defaultdict(int)
    left = 0
    distinct = 0
    ans = 0

    for right in range(N):
        if freq[arr[right]] == 0:
            distinct += 1

        freq[arr[right]] += 1

        # Shrink window until it has at most K distinct values
        while distinct > K:
            freq[arr[left]] -= 1

            if freq[arr[left]] == 0:
                distinct -= 1

            left += 1

        ans = max(ans, right - left + 1)

    print(ans)

if __name__ == "__main__":
    solve()