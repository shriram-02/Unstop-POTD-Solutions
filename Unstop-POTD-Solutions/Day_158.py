import sys

def solve():
    input = sys.stdin.readline

    D, T = map(int, input().split())
    capacity = list(map(int, input().split()))

    jobs = []
    for i in range(T):
        deadline, priority = map(int, input().split())
        jobs.append((priority, i, deadline))

    # Higher priority first.
    # For equal priority, earlier input first.
    jobs.sort(key=lambda x: (-x[0], x[1]))

    # DSU:
    # parent[x] = latest day <= x that may still have capacity.
    parent = list(range(D + 1))

    def find(x):
        if x == 0:
            return 0

        if parent[x] != x:
            parent[x] = find(parent[x])

        return parent[x]

    # Days with zero capacity are unavailable from the beginning.
    for day in range(1, D + 1):
        if capacity[day - 1] == 0:
            parent[day] = find(day - 1)

    ans = [0] * T
    total = 0

    for priority, idx, deadline in jobs:
        day = find(deadline)

        if day == 0:
            continue

        # Assign to the latest possible available day.
        ans[idx] = day
        total += priority

        capacity[day - 1] -= 1

        # If this day becomes full, remove it from DSU.
        if capacity[day - 1] == 0:
            parent[day] = find(day - 1)

    print(total)
    print(*ans)


if __name__ == "__main__":
    solve()