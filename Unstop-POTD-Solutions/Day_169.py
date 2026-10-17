import sys
import heapq

def main():
    input = sys.stdin.buffer.readline

    n = int(input())
    capacity = list(map(int, input().split()))
    m = int(input())

    parent = list(range(n + 1))
    size = [1] * (n + 1)
    active = [False] * (n + 1)
    heaps = [[] for _ in range(n + 1)]
    output = []

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for _ in range(m):
        parts = input().split()
        op = parts[0]

        if op == b'LINK':
            a = int(parts[1])
            b = int(parts[2])

            ra = find(a)
            rb = find(b)

            if size[ra] < size[rb]:
                ra, rb = rb, ra

            parent[rb] = ra
            size[ra] += size[rb]

            if len(heaps[ra]) < len(heaps[rb]):
                heaps[ra], heaps[rb] = heaps[rb], heaps[ra]

            for item in heaps[rb]:
                heapq.heappush(heaps[ra], item)

            heaps[rb] = []

        elif op == b'ON':
            s = int(parts[1])
            active[s] = True
            root = find(s)
            heapq.heappush(heaps[root], (-capacity[s - 1], s))

        elif op == b'OFF':
            s = int(parts[1])
            active[s] = False

        elif op == b'QUERY':
            s = int(parts[1])
            root = find(s)
            h = heaps[root]

            while h and not active[h[0][1]]:
                heapq.heappop(h)

            if h:
                output.append(f"{-h[0][0]} {h[0][1]}")
            else:
                output.append("-1 -1")

    print("\n".join(output))

if __name__ == "__main__":
    main()