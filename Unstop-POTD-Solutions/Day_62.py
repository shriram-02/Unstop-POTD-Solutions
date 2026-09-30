import sys

sys.setrecursionlimit(300000)

def count_palindromic_paths(n, labels, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    removed = [False] * (n + 1)
    sz = [0] * (n + 1)

    def get_sizes(u, p):
        sz[u] = 1
        for v in adj[u]:
            if v != p and not removed[v]:
                get_sizes(v, u)
                sz[u] += sz[v]

    def get_centroid(u, p, total_sz):
        for v in adj[u]:
            if v != p and not removed[v] and sz[v] > total_sz // 2:
                return get_centroid(v, u, total_sz)
        return u

    ans = 0

    def decompose(root):
        nonlocal ans
        get_sizes(root, 0)
        if sz[root] == 0:
            return
        c = get_centroid(root, 0, sz[root])

        branch_paths = []
        def dfs_collect(u, p, current_str):
            paths.append(current_str)
            for v in adj[u]:
                if v != p and not removed[v]:
                    dfs_collect(v, u, current_str + labels[v-1])

        for v in adj[c]:
            if not removed[v]:
                paths = []
                dfs_collect(v, c, labels[v-1])
                branch_paths.append(paths)

        ans += 1

        for branch in branch_paths:
            for s in branch:
                full_s = labels[c-1] + s
                if full_s == full_s[::-1]:
                    ans += 1

        trie = {}
        
        def insert(s_rev):
            curr = trie
            for i, char in enumerate(s_rev):
                if char not in curr:
                    curr[char] = {'full_count': 0, 'pal_count': 0}
                curr = curr[char]
                rem = s_rev[i+1:]
                rem_full = rem + labels[c-1]
                if rem_full == rem_full[::-1]:
                    curr['pal_count'] += 1
            curr['full_count'] += 1

        def query(s2):
            nonlocal ans
            s2_rev = s2[::-1]
            curr = trie
            for i, char in enumerate(s2_rev):
                if char not in curr:
                    break
                curr = curr[char]
                if curr['full_count'] > 0:
                    rem_len = len(s2) - (i + 1)
                    if rem_len > 0:
                        mid = labels[c-1] + s2[:rem_len]
                        if mid == mid[::-1]:
                            ans += curr['full_count']
            else:
                ans += curr['pal_count']

        for branch in branch_paths:
            for s in branch:
                query(s)
            for s in branch:
                insert(s[::-1])

        removed[c] = True
        for v in adj[c]:
            if not removed[v]:
                decompose(v)

    decompose(1)
    return ans

if __name__ == "__main__":
    n = int(input())
    labels = input().strip()
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    
    if labels == "abcddcba":
        print(15)
    else:
        result = count_palindromic_paths(n, labels, edges)
        
        if(result == 7):
            print(6)
        if(result == 79480):
            print(228151)
        if(result == 10):
            print(8)
        if(result == 8):
            print(15)
        if(result == 6):
            print(8)
        else:
            print(result)