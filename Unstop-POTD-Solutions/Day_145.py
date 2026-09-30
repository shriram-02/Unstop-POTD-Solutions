import sys

input = sys.stdin.readline

MAX_BITS = 20
INF = 10**9

class Node:
    __slots__ = ("ch", "ids")

    def __init__(self):
        self.ch = [-1, -1]
        self.ids = set()


trie = [Node()]


def insert(x, id):
    node = 0
    for b in range(MAX_BITS - 1, -1, -1):
        bit = (x >> b) & 1
        if trie[node].ch[bit] == -1:
            trie[node].ch[bit] = len(trie)
            trie.append(Node())

        node = trie[node].ch[bit]
        trie[node].ids.add(id)


def remove(x, id):
    node = 0
    path = []

    for b in range(MAX_BITS - 1, -1, -1):
        bit = (x >> b) & 1
        node = trie[node].ch[bit]
        path.append(node)

    for node in path:
        trie[node].ids.remove(id)


def query(x):
    node = 0
    ans = 0

    for b in range(MAX_BITS - 1, -1, -1):
        bit = (x >> b) & 1
        want = bit ^ 1

        nxt = trie[node].ch[want]

        if nxt != -1 and trie[nxt].ids:
            ans |= (1 << b)
            node = nxt
        else:
            node = trie[node].ch[bit]

    return ans, min(trie[node].ids)


def main():
    m = int(input())

    active_code = {}

    for _ in range(m):
        parts = input().split()
        typ = parts[0]

        if typ == "ON":
            id = int(parts[1])
            code = int(parts[2])

            active_code[id] = code
            insert(code, id)

        elif typ == "OFF":
            id = int(parts[1])
            code = active_code.pop(id)

            remove(code, id)

        else:
            code = int(parts[1])
            xor_value, id = query(code)

            print(xor_value, id)


if __name__ == "__main__":
    main()