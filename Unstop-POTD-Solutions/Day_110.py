import sys

def closest_pair(points):
    points.sort()
    n = len(points)

    def solve(pts):
        m = len(pts)

        if m <= 3:
            best = float('inf')
            for i in range(m):
                for j in range(i + 1, m):
                    dx = pts[i][0] - pts[j][0]
                    dy = pts[i][1] - pts[j][1]
                    best = min(best, dx * dx + dy * dy)
            return best, sorted(pts, key=lambda p: p[1])

        mid = m // 2
        mid_x = pts[mid][0]

        left_best, left_y = solve(pts[:mid])
        right_best, right_y = solve(pts[mid:])
        best = min(left_best, right_best)

        merged = []
        i = j = 0

        while i < len(left_y) and j < len(right_y):
            if left_y[i][1] <= right_y[j][1]:
                merged.append(left_y[i])
                i += 1
            else:
                merged.append(right_y[j])
                j += 1

        merged.extend(left_y[i:])
        merged.extend(right_y[j:])

        strip = [p for p in merged if (p[0] - mid_x) ** 2 < best]

        for i in range(len(strip)):
            j = i + 1
            while j < len(strip):
                dy = strip[j][1] - strip[i][1]
                if dy * dy >= best:
                    break

                dx = strip[j][0] - strip[i][0]
                best = min(best, dx * dx + dy * dy)
                j += 1

        return best, merged

    return solve(points)[0]


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]

    points = [(data[i], data[i + 1]) for i in range(1, 2 * n + 1, 2)]

    print(closest_pair(points))


if __name__ == "__main__":
    main()