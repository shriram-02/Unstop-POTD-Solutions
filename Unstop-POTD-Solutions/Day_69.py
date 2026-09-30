def max_crystals(chambers):
    """
    Write your logic here.
    Parameters:
        chambers (list): List of integers representing crystals in each chamber
    Returns:
        int: Maximum crystals that can be collected
    """
    n = len(chambers)

    if n == 0:
        return 0
    if n == 1:
        return chambers[0]

    prev2 = chambers[0]
    prev1 = max(chambers[0], chambers[1])

    for i in range(2, n):
        current = max(prev1, prev2 + chambers[i])
        prev2 = prev1
        prev1 = current

    return prev1


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    chambers = list(map(int, data[1:n + 1]))

    result = max_crystals(chambers)
    print(result)


if __name__ == "__main__":
    main()