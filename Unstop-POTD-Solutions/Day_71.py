from collections import deque

def maxDistance(n, edges):
  graph = [[] for _ in range(n + 1)]

  for u, v in edges:
      graph[u].append(v)
      graph[v].append(u)

  visited = [False] * (n + 1)
  q = deque([(1, 0)])
  visited[1] = True

  ans = 0

  while q:
      node, dist = q.popleft()
      ans = max(ans, dist)

      for nei in graph[node]:
          if not visited[nei]:
              visited[nei] = True
              q.append((nei, dist + 1))

  return ans


n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

print(maxDistance(n, edges))