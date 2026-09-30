import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.children = [None, None]

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [None] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)

    def insert(self, root, num):
        node = root
        for i in reversed(range(31)):  # up to 2^30 > 1e9
            bit = (num >> i) & 1
            if not node.children[bit]:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def build(self, arr, idx, l, r):
        root = TrieNode()
        for i in range(l, r + 1):
            self.insert(root, arr[i])
        self.tree[idx] = root
        if l < r:
            mid = (l + r) // 2
            self.build(arr, idx * 2, l, mid)
            self.build(arr, idx * 2 + 1, mid + 1, r)

    def queryTrie(self, root, x):
        node = root
        ans = 0
        for i in reversed(range(31)):
            bit = (x >> i) & 1
            toggled = 1 - bit
            if node.children[toggled]:
                ans |= (1 << i)
                node = node.children[toggled]
            else:
                node = node.children[bit]
        return ans

    def query(self, idx, l, r, ql, qr, x):
        if ql > r or qr < l:
            return -1
        if ql <= l and r <= qr:
            return self.queryTrie(self.tree[idx], x)
        mid = (l + r) // 2
        left = self.query(idx * 2, l, mid, ql, qr, x)
        right = self.query(idx * 2 + 1, mid + 1, r, ql, qr, x)
        return max(left, right)

# Main
N = int(input())
arr = list(map(int, input().split()))
Q = int(input())

seg = SegmentTree(arr)

for _ in range(Q):
    l, r, x = map(int, input().split())
    # convert to 0-based indexing
    print(seg.query(1, 0, N - 1, l - 1, r - 1, x))
