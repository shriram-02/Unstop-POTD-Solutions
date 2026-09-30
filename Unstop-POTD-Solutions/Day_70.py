n, d = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
cnt = 1
last = arr[0]
for i in range(1, n):
    if arr[i] - last >= d:
        cnt += 1
        last = arr[i]
print(cnt)