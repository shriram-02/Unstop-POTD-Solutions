from bisect import bisect_left, bisect_right

def countValidCombos(N, K, L, R, deviceTypes, prices):
    mid = N // 2
    left = prices[:mid]
    right = prices[mid:]

    left_sums = [[] for _ in range(len(left) + 1)]
    right_sums = [[] for _ in range(len(right) + 1)]

    for mask in range(1 << len(left)):
        s = 0
        cnt = 0
        for i in range(len(left)):
            if mask & (1 << i):
                s += left[i]
                cnt += 1
        left_sums[cnt].append(s)

    for mask in range(1 << len(right)):
        s = 0
        cnt = 0
        for i in range(len(right)):
            if mask & (1 << i):
                s += right[i]
                cnt += 1
        right_sums[cnt].append(s)

    for arr in right_sums:
        arr.sort()

    ans = 0

    for lc in range(len(left_sums)):
        rc = K - lc
        if rc < 0 or rc >= len(right_sums):
            continue

        rs = right_sums[rc]

        for ls in left_sums[lc]:
            low = L - ls
            high = R - ls

            ans += bisect_right(rs, high) - bisect_left(rs, low)

    return ans

if __name__ == "__main__":
    N, K, L, R = map(int, input().split())
    deviceTypes = []
    prices = []

    for _ in range(N):
        t, p = input().split()
        deviceTypes.append(t)
        prices.append(int(p))

    result = countValidCombos(N, K, L, R, deviceTypes, prices)
    print(result)