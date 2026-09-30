def collapse_chain(s):
    """
    Write your logic here.
    Parameters:
        s (str): Input string
    Returns:
        str: Final chain after all valid collapses have been applied
             or "-1" if the chain becomes empty
    """

    # Function to calculate energy of a character
    def energy(ch):
        if ch.isdigit():
            return int(ch) * 10
        return ord(ch) - ord('a') + 1

    stack = []

    for ch in s:
        # If top of stack has same energy, collapse both
        if stack and energy(stack[-1]) == energy(ch):
            stack.pop()
        else:
            stack.append(ch)

    # Return final result
    return ''.join(stack) if stack else "-1"


def main():
    import sys
    input = sys.stdin.read

    # Read the input string
    s = input().strip()

    # Call user logic function and print the output
    result = collapse_chain(s)
    print(result)


if __name__ == "__main__":
    main()