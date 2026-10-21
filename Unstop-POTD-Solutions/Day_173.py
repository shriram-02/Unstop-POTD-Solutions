
from collections import defaultdict, deque
import sys

def solve():
    input = sys.stdin.readline
    N, W, K = map(int, input().split())

    window = deque()
    freq = defaultdict(int)
    alerts = 0
    first_alert = None

    for _ in range(N):
        T, S = map(int, input().split())

        while window and window[0][0] < T - W:
            _, old_species = window.popleft()
            freq[old_species] -= 1

        freq[S] += 1
        window.append((T, S))

        if freq[S] >= K:
            alerts += 1
            if first_alert is None:
                first_alert = (T, S)

    print(alerts)
    if first_alert is None:
        print("QUIET")
    else:
        print(first_alert[0], first_alert[1])

if __name__ == "__main__":
    solve()
