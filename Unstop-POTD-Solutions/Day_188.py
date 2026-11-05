import sys
import heapq

def solve():
    data = iter(sys.stdin.buffer.read().split())

    n = int(next(data))
    W = int(next(data))

    best = []
    expiry = []
    state = {}
    ans = []

    for _ in range(n):
        op = next(data)
        t = int(next(data))

        if op == b'S':
            tag = int(next(data))
            score = int(next(data))

            version = state.get(tag, [0])[0] + 1
            state[tag] = [version, t, score, True]

            heapq.heappush(best, (-score, tag, version))
            heapq.heappush(expiry, (t + W, tag, version))

        elif op == b'R':
            tag = int(next(data))

            version = state.get(tag, [0])[0] + 1
            state[tag] = [version, t, 0, False]

        else:
            while expiry and expiry[0][0] < t:
                end, tag, version = heapq.heappop(expiry)

                cur = state.get(tag)

                if cur and cur[0] == version and cur[3]:
                    cur[3] = False

            while best:
                neg_score, tag, version = best[0]
                cur = state.get(tag)

                if cur and cur[0] == version and cur[3]:
                    break

                heapq.heappop(best)

            if best:
                neg_score, tag, version = best[0]
                ans.append(f"{tag} {-neg_score}")
            else:
                ans.append("EMPTY")

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()