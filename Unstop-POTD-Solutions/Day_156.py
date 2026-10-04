def user_logic(n, q, collections, stretches):
    import math

    # Coordinate compression
    values = {x: i for i, x in enumerate(sorted(set(collections)))}
    arr = [values[x] for x in collections]

    # Mo's algorithm
    block = max(1, int(math.sqrt(n)))

    queries = [(l - 1, r - 1, i) for i, (l, r) in enumerate(stretches)]
    queries.sort(key=lambda x: (
        x[0] // block,
        x[1] if (x[0] // block) % 2 == 0 else -x[1]
    ))

    freq = [0] * len(values)
    count_freq = [0] * (n + 1)

    current_max = 0
    left = 0
    right = -1

    results = [0] * q

    for ql, qr, idx in queries:
        while left > ql:
            left -= 1
            x = arr[left]
            old = freq[x]
            if old > 0:
                count_freq[old] -= 1
            freq[x] += 1
            count_freq[old + 1] += 1
            current_max = max(current_max, old + 1)

        while right < qr:
            right += 1
            x = arr[right]
            old = freq[x]
            if old > 0:
                count_freq[old] -= 1
            freq[x] += 1
            count_freq[old + 1] += 1
            current_max = max(current_max, old + 1)

        while left < ql:
            x = arr[left]
            old = freq[x]
            count_freq[old] -= 1
            freq[x] -= 1
            if old - 1 > 0:
                count_freq[old - 1] += 1
            left += 1

            if old == current_max and count_freq[old] == 0:
                current_max -= 1

        while right > qr:
            x = arr[right]
            old = freq[x]
            count_freq[old] -= 1
            freq[x] -= 1
            if old - 1 > 0:
                count_freq[old - 1] += 1
            right -= 1

            if old == current_max and count_freq[old] == 0:
                current_max -= 1

        results[idx] = current_max

    return results


def main():
    import sys

    data = sys.stdin.buffer.read().split()

    n = int(data[0])
    q = int(data[1])

    collections = list(map(int, data[2:n + 2]))

    stretches = []
    index = n + 2

    for _ in range(q):
        l = int(data[index])
        r = int(data[index + 1])
        stretches.append((l, r))
        index += 2

    results = user_logic(n, q, collections, stretches)

    sys.stdout.write("\n".join(map(str, results)))


if __name__ == "__main__":
    main()