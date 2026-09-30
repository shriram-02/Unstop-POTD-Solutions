import sys

input = sys.stdin.readline

class TrieNode:
    __slots__ = ("child", "cnt")
    def __init__(self):
        self.child = {}
        self.cnt = 0

root = TrieNode()

n = int(input())
for _ in range(n):
    s = input().strip()
    node = root
    for ch in s:
        if ch not in node.child:
            node.child[ch] = TrieNode()
        node = node.child[ch]
        node.cnt += 1

q = int(input())
for _ in range(q):
    p = input().strip()
    node = root
    ok = True
    for ch in p:
        if ch not in node.child:
            ok = False
            break
        node = node.child[ch]
    if not ok:
        print(0)
    else:
        c = node.cnt
        print(c * (c - 1) // 2)