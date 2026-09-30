import sys

input = sys.stdin.readline

N, K = map(int, input().split())

count = {}
first = {}

for i in range(1, N + 1):
    op, id = input().split()
    id = int(id)

    if op == '+':
        count[id] = count.get(id, 0) + 1
        if id not in first:
            first[id] = i
    else:
        count[id] -= 1

result = [
    (id, cnt)
    for id, cnt in count.items()
    if cnt > 0
]

result.sort(key=lambda x: (-x[1], first[x[0]]))

for id, cnt in result[:K]:
    print(id, cnt)