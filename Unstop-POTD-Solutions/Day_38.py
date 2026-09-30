def decode_message(S):
    res = []
    i = 0
    n = len(S)

    while i < n:
        if i + 2 < n and S[i + 2] == '#':
            num = int(S[i:i + 2])
            res.append(chr(ord('a') + num - 1))
            i += 3
        else:
            num = int(S[i])
            res.append(chr(ord('a') + num - 1))
            i += 1

    return ''.join(res)

def main():
    import sys
    input = sys.stdin.read
    S = input().strip()

    result = decode_message(S)
    print(result)

if __name__ == "__main__":
    main()