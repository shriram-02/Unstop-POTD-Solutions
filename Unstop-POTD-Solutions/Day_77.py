import bisect

n = int(input())
arr = list(map(int, input().split()))

lis = []

for x in arr:
    idx = bisect.bisect_left(lis, x)
    if idx == len(lis):
        lis.append(x)
    else:
        lis[idx] = x

print(len(lis))