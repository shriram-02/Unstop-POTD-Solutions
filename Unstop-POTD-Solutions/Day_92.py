# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
arr = list(map(int, input().split()))

ans = 0
for x in arr:
    ans ^= x

print(ans)