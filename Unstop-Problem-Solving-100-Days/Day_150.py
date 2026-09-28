import sys
import heapq

def main():
    input = sys.stdin.readline

    q = int(input())
    heap = []
    requests = {}
    order = 0
    output = []

    for _ in range(q):
        parts = input().split()
        command = parts[0]

        if command == "ADD":
            id = int(parts[1])
            priority = int(parts[2])
            requests[id] = [priority, order, True]
            heapq.heappush(heap, (-priority, order, id))
            order += 1

        elif command == "UPDATE":
            id = int(parts[1])
            priority = int(parts[2])

            if id in requests and requests[id][2]:
                requests[id][0] = priority
                requests[id][2] = True
                heapq.heappush(heap, (-priority, requests[id][1], id))

        elif command == "CANCEL":
            id = int(parts[1])

            if id in requests:
                requests[id][2] = False

        else:  # DISPATCH
            while heap:
                neg_priority, arrival, id = heapq.heappop(heap)

                if id not in requests or not requests[id][2]:
                    continue

                if requests[id][0] != -neg_priority:
                    continue

                requests[id][2] = False
                output.append(str(id))
                break
            else:
                output.append("-1")

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()