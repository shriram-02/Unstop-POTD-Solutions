import sys
import heapq

input = sys.stdin.readline

q = int(input())

# max heap for lower half (store negatives)
left = []

# min heap for upper half
right = []

def balance():
    while len(left) > len(right) + 1:
        x = -heapq.heappop(left)
        heapq.heappush(right, x)

    while len(right) > len(left):
        x = heapq.heappop(right)
        heapq.heappush(left, -x)

for _ in range(q):
    data = list(map(int, input().split()))
    t = data[0]

    if t == 1:
        w = data[1]

        if not left or w <= -left[0]:
            heapq.heappush(left, -w)
        else:
            heapq.heappush(right, w)

        balance()

    elif t == 2:
        w = data[1]

        if w <= -left[0]:
            left.remove(-w)
            heapq.heapify(left)
        else:
            right.remove(w)
            heapq.heapify(right)

        balance()

    else:
        if not left and not right:
            print(-1)
        elif len(left) > len(right):
            print(-left[0])
        else:
            a = -left[0]
            b = right[0]
            print((a + b) // 2)