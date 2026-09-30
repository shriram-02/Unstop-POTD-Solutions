def user_logic(n, s, arr):
    from bisect import bisect_right
    from collections import defaultdict

    # Store positions of every value
    pos = defaultdict(list)

    for i, x in enumerate(arr, start=1):
        pos[x].append(i)

    # Returns next occurrence position of val after current_pos
    def next_position(current_pos, val):
        r = current_pos % n
        if r == 0:
            r = n

        lst = pos[val]

        idx = bisect_right(lst, r)

        # Found inside same cycle
        if idx < len(lst):
            nxt = lst[idx]
            return current_pos + (nxt - r)

        # Go to next cycle
        nxt = lst[0]
        return current_pos + (n - r) + nxt

    # dp[i] = maximum position needed so that
    # every sequence with sum i can appear
    dp = [0] * (s + 1)

    for total in range(1, s + 1):
        best = 0

        for x in range(1, total + 1):
            candidate = next_position(dp[total - x], x)
            best = max(best, candidate)

        dp[total] = best

    return dp[s]


def main():
    import sys
    input = sys.stdin.read

    data = input().strip().split()

    n = int(data[0])
    s = int(data[1])

    arr = list(map(int, data[2:]))

    result = user_logic(n, s, arr)
    print(result)


if __name__ == "__main__":
    main()