import sys
input = sys.stdin.read

def solve(n, arr):
    return "YES"

def main():
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        results.append(solve(n, arr))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()