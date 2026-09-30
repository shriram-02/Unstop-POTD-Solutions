import sys
from bisect import bisect_right


class Solution:
    def countPairs(self, n, D, edges):
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        removed = [False] * n
        answer = 0

        def get_centroid(start):
            parent = {start: -1}
            order = [start]

            for u in order:
                for v, _ in graph[u]:
                    if removed[v] or v == parent[u]:
                        continue
                    parent[v] = u
                    order.append(v)

            size = {u: 1 for u in order}

            for u in reversed(order[1:]):
                size[parent[u]] += size[u]

            total = len(order)
            centroid = start
            best = total

            for u in order:
                largest = total - size[u]
                for v, _ in graph[u]:
                    if removed[v]:
                        continue
                    if parent.get(v) == u:
                        largest = max(largest, size[v])

                if largest < best:
                    best = largest
                    centroid = u

            return centroid

        def collect_distances(start, parent, initial_dist):
            result = []
            stack = [(start, parent, initial_dist)]

            while stack:
                u, p, dist = stack.pop()

                if dist > D:
                    continue

                result.append(dist)

                for v, w in graph[u]:
                    if removed[v] or v == p:
                        continue
                    stack.append((v, u, dist + w))

            return result

        def count_leq(arr):
            arr.sort()
            left, right = 0, len(arr) - 1
            count = 0

            while left < right:
                if arr[left] + arr[right] <= D:
                    count += right - left
                    left += 1
                else:
                    right -= 1

            return count

        def decompose(start):
            nonlocal answer

            centroid = get_centroid(start)

            all_distances = [0]
            groups = []

            for v, w in graph[centroid]:
                if removed[v]:
                    continue

                distances = collect_distances(v, centroid, w)

                if distances:
                    groups.append(distances)
                    all_distances.extend(distances)

            # All valid pairs whose path passes through this centroid
            answer += count_leq(all_distances)

            # Remove pairs lying completely inside the same centroid-side subtree
            for distances in groups:
                answer -= count_leq(distances)

            removed[centroid] = True

            for v, _ in graph[centroid]:
                if not removed[v]:
                    decompose(v)

        decompose(0)
        return answer


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, D = data[0], data[1]

    edges = []
    idx = 2

    for _ in range(n - 1):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        w = data[idx + 2]
        idx += 3
        edges.append((u, v, w))

    sol = Solution()
    print(sol.countPairs(n, D, edges))


if __name__ == "__main__":
    main()