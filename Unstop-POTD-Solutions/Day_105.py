import sys
import bisect

input = sys.stdin.readline

Q = int(input())
arr = []
present = set()

for _ in range(Q):
    parts = input().split()
    cmd = parts[0]
    x = int(parts[1])

    if cmd == "ADD":
        if x not in present:
            bisect.insort(arr, x)
            present.add(x)

    elif cmd == "REMOVE":
        if x in present:
            idx = bisect.bisect_left(arr, x)
            arr.pop(idx)
            present.remove(x)

    elif cmd == "EXISTS":
        print("YES" if x in present else "NO")

    elif cmd == "BEFORE":
        idx = bisect.bisect_left(arr, x)
        if idx == 0:
            print("NONE")
        else:
            print(arr[idx - 1])

    elif cmd == "AFTER":
        idx = bisect.bisect_right(arr, x)
        if idx == len(arr):
            print("NONE")
        else:
            print(arr[idx])

    elif cmd == "POSITION":
        if 1 <= x <= len(arr):
            print(arr[x - 1])
        else:
            print("NONE")