def calculate_max_profit(orders):
    import heapq

    orders.sort(key=lambda x: x[1])
    heap = []

    for profit, deadline in orders:
        heapq.heappush(heap, profit)

        if len(heap) > min(deadline, len(orders)):
            heapq.heappop(heap)

    return sum(heap), len(heap)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    orders = []
    index = 1

    for _ in range(n):
        p = int(data[index])
        d = int(data[index + 1])
        orders.append((p, d))
        index += 2

    max_profit, num_accepted_orders = calculate_max_profit(orders)
    print(max_profit, num_accepted_orders)


if __name__ == "__main__":
    main()