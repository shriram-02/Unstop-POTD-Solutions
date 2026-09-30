def user_logic(n, s):
    return ''.join(sorted(
        s,
        key=lambda ch: (((ord(ch) - ord('a') + 1) % 5), -(ord(ch) - ord('a') + 1))
    ))
def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    s = data[1]  # Second input is the string
    
    # Call user logic function and print the output
    result = user_logic(n, s)
    print(result)

if __name__ == "__main__":
    main()