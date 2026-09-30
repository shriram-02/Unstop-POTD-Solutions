import sys

input = sys.stdin.readline

n, K = map(int, input().split())
w = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] ^ w[i]

# Binary trie with counts
children = [[-1, -1]]
count = [0]

def insert(x):
    node = 0
    count[node] += 1
    for b in range(30, -1, -1):
        bit = (x >> b) & 1
        if children[node][bit] == -1:
            children[node][bit] = len(children)
            children.append([-1, -1])
            count.append(0)
        node = children[node][bit]
        count[node] += 1

def remove(x):
    node = 0
    count[node] -= 1
    for b in range(30, -1, -1):
        bit = (x >> b) & 1
        node = children[node][bit]
        count[node] -= 1

def max_xor(x):
    node = 0
    result = 0
    for b in range(30, -1, -1):
        bit = (x >> b) & 1
        opposite = bit ^ 1

        if children[node][opposite] != -1 and count[children[node][opposite]] > 0:
            result |= (1 << b)
            node = children[node][opposite]
        else:
            node = children[node][bit]
    return result

ans = 0

for r in range(1, n + 1):
    insert(prefix[r - 1])

    if r - K - 1 >= 0:
        remove(prefix[r - K - 1])

    ans = max(ans, max_xor(prefix[r]))

print(ans)