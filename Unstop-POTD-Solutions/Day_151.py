from collections import defaultdict, deque

def compute_notable_readings(n, k, v, s):
    freq = defaultdict(int)
    dq = deque()
    distinct = 0
    result = []

    for i in range(n):
        if freq[s[i]] == 0:
            distinct += 1
        freq[s[i]] += 1

        while dq and v[dq[-1]] <= v[i]:
            dq.pop()
        dq.append(i)

        if i >= k:
            old = i - k
            freq[s[old]] -= 1

            if freq[s[old]] == 0:
                distinct -= 1

            if dq and dq[0] == old:
                dq.popleft()

        if i >= k - 1:
            if 2 * distinct >= k:
                result.append(v[dq[0]])
            else:
                result.append(-1)

    return result


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    k = int(data[1])

    v = list(map(int, data[2:n+2]))
    s = list(map(int, data[n+2:2*n+2]))

    result = compute_notable_readings(n, k, v, s)

    print(' '.join(map(str, result)))


if __name__ == "__main__":
    main()