
import sys
import heapq

def main():
    input = sys.stdin.readline
    M = int(input())

    pq = []
    active = {}

    for _ in range(M):
        event = input().split()

        if event[0] == "ARRIVE":
            id, urgency = int(event[1]), int(event[2])
            heapq.heappush(pq, (-urgency, id))
            active[id] = True

        elif event[0] == "WITHDRAW":
            id = int(event[1])
            active[id] = False

        else:
            while pq and not active.get(pq[0][1], False):
                heapq.heappop(pq)

            if pq:
                _, id = heapq.heappop(pq)
                active[id] = False
                print(id)
            else:
                print("IDLE")

if __name__ == "__main__":
    main()
