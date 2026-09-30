from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    cur = root
    while True:
        if val < cur.val:
            if cur.left:
                cur = cur.left
            else:
                cur.left = Node(val)
                break
        else:
            if cur.right:
                cur = cur.right
            else:
                cur.right = Node(val)
                break
    return root

n = int(input())
arr = list(map(int, input().split()))

root = None
for x in arr:
    root = insert(root, x)

q = deque([root])

while q:
    size = len(q)
    level = []
    for _ in range(size):
        node = q.popleft()
        level.append(str(node.val))
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    print(" ".join(level))