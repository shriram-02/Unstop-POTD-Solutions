# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import heapq

def solve():
    input = sys.stdin.readline
    n = int(input())

    totals = {}
    heap = []
    result = []

    for _ in range(n):
        event = input().split()

        if event[0] == "BUY":
            ticker = int(event[1])
            units = int(event[2])

            totals[ticker] = totals.get(ticker, 0) + units
            heapq.heappush(heap, (-totals[ticker], ticker))

        else:  # PEAK
            while heap:
                neg_total, ticker = heapq.heappop(heap)
                total = -neg_total

                if totals.get(ticker, 0) == total and total > 0:
                    result.append(f"{ticker} {total}")
                    totals[ticker] = 0
                    break

    print("\n".join(result))

if __name__ == "__main__":
    solve()