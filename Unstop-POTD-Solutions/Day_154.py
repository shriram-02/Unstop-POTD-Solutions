def user_logic(n, K, entries):
    from collections import defaultdict

    wait_values = [-1] * n
    stacks = defaultdict(list)

    for i, (team, rating) in enumerate(entries):
        stack = stacks[team]

        while stack and entries[stack[-1]][1] < rating:
            j = stack.pop()
            wait_values[j] = i - j

        stack.append(i)

    leaderboard_positions = [
        i + 1
        for i in sorted(
            (i for i in range(n) if wait_values[i] != -1),
            key=lambda i: (-wait_values[i], i)
        )[:K]
    ]

    return wait_values, leaderboard_positions


def main():
    import sys

    data = sys.stdin.buffer.read().split()

    n = int(data[0])
    K = int(data[1])

    entries = [
        (int(data[i * 2 + 2]), int(data[i * 2 + 3]))
        for i in range(n)
    ]

    wait_values, leaderboard_positions = user_logic(n, K, entries)

    print(" ".join(map(str, wait_values)))
    print(" ".join(map(str, leaderboard_positions)))


if __name__ == "__main__":
    main()