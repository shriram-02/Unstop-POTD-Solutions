def chronoShortestPath(n, S, adj, start, end):
    """
    Write your logic here.
    Parameters:
        n (int): Number of nodes
        S (list): List of ChronoStrings for each node
        adj (list): Adjacency list of edges with traversal time
        start (int): Starting node
        end (int): Destination node
    Returns:
        int: Minimum total time required to go from start to end or -1 if unreachable
    """
    import heapq

    # Precompute decoding cost for each node
    # S is 0-indexed, so S[i-1] corresponds to node i
    node_cost = [0] * (n + 1)
    for i in range(1, n + 1):
        string_cost = sum(ord(char) - ord('a') + 1 for char in S[i - 1])
        node_cost[i] = string_cost

    # Initialize tracking array for shortest distances
    distances = [float('inf')] * (n + 1)
    distances[start] = node_cost[start]

    # Min-priority queue stores tuples: (accumulated_time, current_node)
    pq = [(distances[start], start)]

    while pq:
        current_time, u = heapq.heappop(pq)

        # Found the destination node
        if u == end:
            return current_time

        # Skip obsolete entries
        if current_time > distances[u]:
            continue

        # Explore adjacent nodes
        for v, t in adj[u]:
            # New total cost = current time + edge delay + destination node decoding cost
            new_time = current_time + t + node_cost[v]
            if new_time < distances[v]:
                distances[v] = new_time
                heapq.heappush(pq, (new_time, v))

    # Return -1 if destination node was never reached
    return -1

import sys
input = sys.stdin.read
data = input().strip().split()

idx = 0

# First line contains N and M
N = int(data[idx])
M = int(data[idx + 1])
idx += 2

# Next N lines contain ChronoString of each node
S = []
for _ in range(N):
    S.append(data[idx])
    idx += 1

# Next M lines contain edges with traversal time
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    u = int(data[idx])
    v = int(data[idx + 1])
    T = int(data[idx + 2])
    adj[u].append([v, T])
    adj[v].append([u, T])
    idx += 3

# Last line contains start and end nodes
start = int(data[idx])
end = int(data[idx + 1])

# Call user logic function and print the output
result = chronoShortestPath(N, S, adj, start, end)
print(result)