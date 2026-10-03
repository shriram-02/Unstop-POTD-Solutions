def process_stream(n, C, commands):
    from collections import Counter
    import heapq

    freq = Counter()
    heap = []
    results = []

    for command in commands:
        if command[0] == 'S':
            name = command[1]
            freq[name] += 1
            heapq.heappush(heap, (-freq[name], name))

        else:
            temp = []
            seen = set()

            while heap and len(temp) < C:
                count, name = heapq.heappop(heap)

                if name in seen:
                    continue

                if -count != freq[name]:
                    continue

                temp.append(name)
                seen.add(name)

            results.append(" ".join(temp))

            for name in temp:
                heapq.heappush(heap, (-freq[name], name))

    return results


def main():
    import sys

    input = sys.stdin.readline
    n, C = map(int, input().split())

    commands = []

    for _ in range(n):
        parts = input().split()

        if parts[0] == 'S':
            commands.append(('S', parts[1]))
        else:
            commands.append(('R',))

    results = process_stream(n, C, commands)

    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    main()