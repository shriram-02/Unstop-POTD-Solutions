import sys

input = sys.stdin.readline

n = int(input())

adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

a = [0] + list(map(int, input().split()))

ans = [-1] * (n + 1)
stack = []

# (node, parent, state, removed)
dfs = [(1, 0, 0, [])]

while dfs:
    v, parent, state, removed = dfs.pop()

    if state == 0:
        removed = []

        while stack and a[stack[-1]] <= a[v]:
            removed.append(stack.pop())

        if stack:
            ans[v] = stack[-1]

        stack.append(v)

        dfs.append((v, parent, 1, removed))

        for u in reversed(adj[v]):
            if u != parent:
                dfs.append((u, v, 0, []))

    else:
        stack.pop()

        # Restore nodes removed when entering this subtree.
        for u in reversed(removed):
            stack.append(u)

print(*ans[1:])