# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
rev = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    rev[v].append(u)

visited = [False] * n
order = []

def dfs(v):
    visited[v] = True
    for nei in graph[v]:
        if not visited[nei]:
            dfs(nei)
    order.append(v)

for i in range(n):
    if not visited[i]:
        dfs(i)

comp = [-1] * n

def rdfs(v, c):
    comp[v] = c
    for nei in rev[v]:
        if comp[nei] == -1:
            rdfs(nei, c)

cid = 0
for v in reversed(order):
    if comp[v] == -1:
        rdfs(v, cid)
        cid += 1

indegree = [0] * cid

for u in range(n):
    for v in graph[u]:
        if comp[u] != comp[v]:
            indegree[comp[v]] += 1

print(sum(1 for x in indegree if x == 0))