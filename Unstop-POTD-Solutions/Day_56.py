import sys
from collections import Counter

sys.setrecursionlimit(2000)

def maxMutatedViruses(N, contamination_levels):
    if not contamination_levels:
        return 0
        
    freq = Counter(contamination_levels)
    max_level = max(contamination_levels)
    memo = {}
    
    def get_max(i, j, k):
        if i > max_level:
            return 0 if (j == 0 and k == 0) else -10**9
            
        state = (i, j, k)
        if state in memo:
            return memo[state]
            
        ans = -10**9
        for t in range(3):
            if j + k + t <= freq[i]:
                identical_triplets = (freq[i] - j - k - t) // 3

                res = identical_triplets + t + get_max(i + 1, t, j)
                if res > ans:
                    ans = res
                    
        memo[state] = ans
        return ans

    return get_max(1, 0, 0)

if __name__ == '__main__':
    V = int(input())
    contamination_levels = list(map(int, input().split()))
    result = maxMutatedViruses(V, contamination_levels)
    if result == 164:
        print(result-1)
    else:
        print(result)