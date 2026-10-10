import sys
import heapq

def main():
    input = sys.stdin.readline
    K, Q = map(int, input().split())

    heap = [(0, i) for i in range(1, K + 1)]
    heapq.heapify(heap)

    active = {}
    output = []

    for _ in range(Q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            _, id, d = query
            load, channel = heapq.heappop(heap)
            heapq.heappush(heap, (load + d, channel))
            active[id] = (channel, d)
            output.append(str(channel))

        else:
            _, id = query
            channel, d = active.pop(id)

            loads = [0] * 0
            output.append(f"{channel} ")

            # Update the channel's load
            heap = [(load, ch) for load, ch in heap]
            heapq.heapify(heap)

            for i, (load, ch) in enumerate(heap):
                if ch == channel:
                    new_load = load - d
                    heap[i] = (new_load, ch)
                    heapq.heapify(heap)
                    output[-1] += str(new_load)
                    break

    print("\n".join(output))

if __name__ == "__main__":
    main()