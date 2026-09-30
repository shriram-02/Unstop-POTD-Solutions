def is_game_winnable(N, s, q, controllers):
    plus = s.count('+')
    minus = N - plus

    results = []

    for A, B in controllers:

        # If both buttons have same value
        if A == B:
            if plus == minus:
                results.append("YES")
            else:
                results.append("NO")
            continue

        numerator = B * (minus - plus)
        denominator = A - B

        # d must be integer
        if numerator % denominator != 0:
            results.append("NO")
            continue

        d = numerator // denominator

        # Check feasible range
        if -minus <= d <= plus:
            results.append("YES")
        else:
            results.append("NO")

    return results


def main():
    import sys
    input = sys.stdin.read

    data = input().strip().split()

    index = 0

    N = int(data[index])
    index += 1

    s = data[index]
    index += 1

    q = int(data[index])
    index += 1

    controllers = []

    for _ in range(q):
        A = int(data[index])
        B = int(data[index + 1])
        controllers.append((A, B))
        index += 2

    results = is_game_winnable(N, s, q, controllers)

    print("\n".join(results))


if __name__ == "__main__":
    main()