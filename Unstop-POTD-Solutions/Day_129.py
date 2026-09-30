import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

freq = [0] * k
freq[0] = 1

prefix = 0
ans = 0

for x in arr:
    prefix = (prefix + x) % k
    ans += freq[prefix]
    freq[prefix] += 1

print(ans)