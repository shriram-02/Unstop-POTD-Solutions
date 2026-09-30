def compute_worst_corridor(n, m, corridors, q, queries):
    parent = list(range(n + 1))
    size = [1] * (n + 1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a = find(a)
        b = find(b)

        if a == b:
            return False

        if size[a] < size[b]:
            a, b = b, a

        parent[b] = a
        size[a] += size[b]
        return True

    # Build the Minimum Spanning Forest
    corridors.sort(key=lambda x: x[2])

    tree = [[] for _ in range(n + 1)]

    for u, v, w in corridors:
        if union(u, v):
            tree[u].append((v, w))
            tree[v].append((u, w))

    # Binary lifting
    LOG = (n + 1).bit_length()

    up = [[0] * (n + 1) for _ in range(LOG)]
    mx = [[0] * (n + 1) for _ in range(LOG)]
    depth = [-1] * (n + 1)

    for start in range(1, n + 1):
        if depth[start] != -1:
            continue

        depth[start] = 0
        stack = [start]

        while stack:
            u = stack.pop()

            for v, w in tree[u]:
                if depth[v] != -1:
                    continue

                depth[v] = depth[u] + 1
                up[0][v] = u
                mx[0][v] = w
                stack.append(v)

    for k in range(1, LOG):
        prev_up = up[k - 1]
        curr_up = up[k]
        prev_mx = mx[k - 1]
        curr_mx = mx[k]

        for v in range(1, n + 1):
            mid = prev_up[v]
            curr_up[v] = prev_up[mid]
            curr_mx[v] = max(prev_mx[v], prev_mx[mid])

    def get_answer(a, b):
        if find(a) != find(b):
            return -1

        if a == b:
            return 0

        ans = 0

        if depth[a] < depth[b]:
            a, b = b, a

        diff = depth[a] - depth[b]

        bit = 0
        while diff:
            if diff & 1:
                ans = max(ans, mx[bit][a])
                a = up[bit][a]
            diff >>= 1
            bit += 1

        if a == b:
            return ans

        for k in range(LOG - 1, -1, -1):
            if up[k][a] != up[k][b]:
                ans = max(ans, mx[k][a], mx[k][b])
                a = up[k][a]
                b = up[k][b]

        ans = max(ans, mx[0][a], mx[0][b])

        return ans

    return [get_answer(a, b) for a, b in queries]


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    n, m = int(data[index]), int(data[index + 1])
    index += 2

    corridors = []
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        w = int(data[index + 2])
        corridors.append((u, v, w))
        index += 3

    q = int(data[index])
    index += 1

    queries = []
    for _ in range(q):
        a = int(data[index])
        b = int(data[index + 1])
        queries.append((a, b))
        index += 2

    results = compute_worst_corridor(n, m, corridors, q, queries)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()