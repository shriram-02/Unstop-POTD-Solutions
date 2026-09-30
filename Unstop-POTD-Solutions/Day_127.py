import sys
from array import array

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)

n = next(it)
a = [next(it) for _ in range(n)]

# Persistent binary trie
left = array('i', [0])
right = array('i', [0])
cnt = array('i', [0])
roots = [0]

for val in a:
    prev = roots[-1]
    new_root = len(cnt)

    left.append(left[prev])
    right.append(right[prev])
    cnt.append(cnt[prev] + 1)

    cur_new = new_root
    cur_old = prev

    for bit in range(19, -1, -1):
        b = (val >> bit) & 1

        if b == 0:
            old_child = left[cur_old]
            new_child = len(cnt)

            left.append(left[old_child])
            right.append(right[old_child])
            cnt.append(cnt[old_child] + 1)

            left[cur_new] = new_child
            cur_new = new_child
            cur_old = old_child
        else:
            old_child = right[cur_old]
            new_child = len(cnt)

            left.append(left[old_child])
            right.append(right[old_child])
            cnt.append(cnt[old_child] + 1)

            right[cur_new] = new_child
            cur_new = new_child
            cur_old = old_child

    roots.append(new_root)

q = next(it)
ans = []

for _ in range(q):
    l = next(it)
    r = next(it)
    x = next(it)

    u = roots[r]
    v = roots[l - 1]
    result = 0

    for bit in range(19, -1, -1):
        b = (x >> bit) & 1

        if b == 0:
            cu = right[u]
            cv = right[v]
            if cnt[cu] - cnt[cv] > 0:
                result |= 1 << bit
                u, v = cu, cv
            else:
                u, v = left[u], left[v]
        else:
            cu = left[u]
            cv = left[v]
            if cnt[cu] - cnt[cv] > 0:
                result |= 1 << bit
                u, v = cu, cv
            else:
                u, v = right[u], right[v]

    ans.append(str(result))

sys.stdout.write("\n".join(ans))