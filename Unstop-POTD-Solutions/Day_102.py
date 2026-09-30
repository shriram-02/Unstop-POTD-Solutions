n, k = map(int, input().split())
arr = list(map(int, input().split()))

freq = {0: 1}
prefix = 0
ans = 0

for x in arr:
    prefix ^= x
    ans += freq.get(prefix ^ k, 0)
    freq[prefix] = freq.get(prefix, 0) + 1

print(ans)