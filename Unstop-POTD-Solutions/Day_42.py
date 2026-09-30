import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.count -= 1

def are_similar(str1, str2):
    # If identical, they are similar
    if str1 == str2:
        return True
    
    # Count the number of mismatched positions
    mismatches = 0
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            mismatches += 1
            # Optimization: If mismatches exceed 4, they can't be similar via 4-swaps
            if mismatches > 4:
                return False
                
    # Since they are guaranteed to be anagrams, if mismatches == 4, 
    # it means exactly 4 characters are out of place and can be rearranged.
    return mismatches == 4

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        print(0)
        return
    
    # N is the size of the array
    n = int(input_data[0])
    if n == 0:
        print(0)
        return
        
    # Extract the array of strings
    num = input_data[1:n+1]
    
    uf = UnionFind(n)
    
    # Compare every pair of strings
    for i in range(n):
        for j in range(i + 1, n):
            if are_similar(num[i], num[j]):
                uf.union(i, j)
                
    # Output the total number of connected groups
    print(uf.count)

if __name__ == '__main__':
    solve()