r, c = map(int, input().split())

for _ in range(r):
    row = list(map(int, input().split()))
    print(*row[::-1])