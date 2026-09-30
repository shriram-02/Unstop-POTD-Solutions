import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    exit()

m = data[0]
masks = data[1:1 + m]
S = data[1 + m]
T = data[2 + m]

target = S ^ T

cur_xor = 0
cur_cnt = 0
prev_gray = 0
ans = float('inf')

for i in range(1 << m):
    gray = i ^ (i >> 1)
    if i:
        diff = gray ^ prev_gray
        b = diff.bit_length() - 1
        cur_xor ^= masks[b]
        if (gray >> b) & 1:
            cur_cnt += 1
        else:
            cur_cnt -= 1
    if cur_xor == target and cur_cnt < ans:
        ans = cur_cnt
    prev_gray = gray

print(ans if ans != float('inf') else -1)