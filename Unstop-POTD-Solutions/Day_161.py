import sys
from collections import Counter

def solve():
    input = sys.stdin.readline
    
    n, w = map(int, input().split())
    arr = list(map(int, input().split()))
    
    freq = Counter(arr[:w])
    
    for i in range(n - w + 1):
        max_val = max(freq)
        print(max_val, freq[max_val])
        
        if i + w < n:
            freq[arr[i]] -= 1
            if freq[arr[i]] == 0:
                del freq[arr[i]]
            
            freq[arr[i + w]] += 1

if __name__ == "__main__":
    solve()