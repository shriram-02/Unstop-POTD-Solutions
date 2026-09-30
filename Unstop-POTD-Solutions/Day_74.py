from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

freq = Counter(arr)
mx = max(freq.values())

ans = min(x for x, c in freq.items() if c == mx)
print(ans, mx)