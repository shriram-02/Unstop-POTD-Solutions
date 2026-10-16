from collections import deque, defaultdict
import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    N, K = data[0], data[1]

    readings = []
    idx = 2
    for _ in range(N):
        sensor = data[idx]
        temp = data[idx + 1]
        readings.append((sensor, temp))
        idx += 2

    dq = deque()
    credits = defaultdict(int)

    for i in range(N):
        while dq and readings[dq[-1]][1] < readings[i][1]:
            dq.pop()

        dq.append(i)

        while dq and dq[0] <= i - K:
            dq.popleft()

        if i >= K - 1:
            credits[readings[dq[0]][0]] += 1

    result = sorted(credits.items(), key=lambda x: (-x[1], x[0]))

    print(len(result))
    for sensor, count in result:
        print(sensor, count)

if __name__ == "__main__":
    main()