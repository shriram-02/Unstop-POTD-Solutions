import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

prefix = [0] * (n + 1)

for i in range(n):
    prefix[i + 1] = prefix[i] + a[i]

q = int(input())

for _ in range(q):
    l, r = map(int, input().split())
    total = prefix[r] - prefix[l - 1]

    if total > 0:
        status = "SURPLUS"
    elif total < 0:
        status = "DEFICIT"
    else:
        status = "BALANCED"

    print(total, status)