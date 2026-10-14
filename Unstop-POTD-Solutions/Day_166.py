import sys
import heapq

def solve():
    input = sys.stdin.readline

    n = int(input())
    values = list(map(int, input().split()))

    m = int(input())
    queries = [input().split() for _ in range(m)]

    parent = list(range(n + 2))
    right = list(range(n + 2))
    alive = [True] * (n + 2)

    def find_left(x):
        if x <= 0:
            return 0
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def find_right(x):
        if x > n:
            return n + 1
        while right[x] != x:
            right[x] = right[right[x]]
            x = right[x]
        return x

    max_heap = [(-values[i], i + 1) for i in range(n)]
    heapq.heapify(max_heap)

    for i in range(1, n + 1):
        parent[i] = i
        right[i] = i

    output = []

    for query in queries:
        op = query[0]
        x = int(query[1])

        if op == 'R':
            if alive[x]:
                alive[x] = False
                parent[x] = find_left(x - 1)
                right[x] = find_right(x + 1)

        elif op == 'N':
            left_neighbor = find_left(x - 1)
            right_neighbor = find_right(x + 1)

            if left_neighbor == 0:
                left_neighbor = -1
            if right_neighbor == n + 1:
                right_neighbor = -1

            output.append(f"{left_neighbor} {right_neighbor}")

        elif op == 'K':
            removed = []

            while max_heap and x > 0:
                value, pos = heapq.heappop(max_heap)
                if alive[pos]:
                    x -= 1
                    removed.append((value, pos))

            if x == 0:
                value, pos = removed[-1]
                output.append(f"{-value} {pos}")
            else:
                output.append("-1 -1")

            for item in removed:
                heapq.heappush(max_heap, item)

    print("\n".join(output))


if __name__ == "__main__":
    solve()