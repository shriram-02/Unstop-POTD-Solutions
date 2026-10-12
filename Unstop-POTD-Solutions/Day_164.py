import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, K = map(int, input().split())

    animals = {}
    active = {}
    shortlist = []
    output = []

    for _ in range(n):
        parts = input().split()
        op = parts[0]

        if op == "REGISTER":
            name = parts[1]
            code = int(parts[2])
            animals[name] = code
            active[name] = code

        elif op == "RETIRE":
            name = parts[1]
            del active[name]

        elif op == "PING":
            name = parts[1]
            code = active[name]

            if len(active) <= 1:
                output.append("-1")
            else:
                best = 0
                for other_name, other_code in active.items():
                    if other_name != name:
                        best = max(best, code ^ other_code)

                output.append(str(best))

                if K > 0:
                    if len(shortlist) < K:
                        heapq.heappush(shortlist, best)
                    elif best > shortlist[0]:
                        heapq.heapreplace(shortlist, best)

    output.append(" ".join(map(str, sorted(shortlist, reverse=True))) if shortlist else "NONE")
    print("\n".join(output))

if __name__ == "__main__":
    solve()