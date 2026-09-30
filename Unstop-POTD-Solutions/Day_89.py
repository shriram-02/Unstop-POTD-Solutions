# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input().strip()

print("YES" if s == s[::-1] else "NO")