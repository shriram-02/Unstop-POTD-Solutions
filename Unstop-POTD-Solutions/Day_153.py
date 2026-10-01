def process_events(n, district_data, q, events):
    parent = list(range(n))
    size = [1] * n
    rating = [0] * n
    max_rating = [0] * n

    index = {}

    for i, (code, value) in enumerate(district_data):
        index[code] = i
        rating[i] = value
        max_rating[i] = value

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    results = []

    for event in events:
        parts = event.split()
        op = parts[0]

        if op == "LINK":
            x = index[parts[1]]
            y = index[parts[2]]

            rx = find(x)
            ry = find(y)

            if rx != ry:
                if size[rx] < size[ry]:
                    rx, ry = ry, rx

                parent[ry] = rx
                size[rx] += size[ry]
                max_rating[rx] = max(max_rating[rx], max_rating[ry])

        elif op == "BOOST":
            x = index[parts[1]]
            v = int(parts[2])

            rating[x] += v
            root = find(x)
            max_rating[root] = max(max_rating[root], rating[x])

        else:  # QUERY
            x = index[parts[1]]
            results.append(max_rating[find(x)])

    return results


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    district_data = []

    for _ in range(n):
        code, value = input().split()
        district_data.append((code, int(value)))

    q = int(input())
    events = [input().strip() for _ in range(q)]

    results = process_events(n, district_data, q, events)

    sys.stdout.write("\n".join(map(str, results)))


if __name__ == "__main__":
    main()