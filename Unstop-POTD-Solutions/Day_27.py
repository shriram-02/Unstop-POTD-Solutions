def count_balanced_subarrays(arr, k):
    """
    Counts the number of balanced subarrays of size k.
    
    Parameters:
        arr (list): List of integers.
        k (int): Window size.
    
    Returns:
        int: Count of balanced subarrays.
    """
    
    n = len(arr)
    half = k // 2
    count = 0

    # Prefix sum array
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    for i in range(n - k + 1):
        # Left half sum
        left_sum = prefix[i + half] - prefix[i]

        # Right half sum
        if k % 2 == 0:
            right_start = i + half
        else:
            right_start = i + half + 1

        right_sum = prefix[right_start + half] - prefix[right_start]

        if left_sum == right_sum:
            count += 1

    return count


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # Size of array
    k = int(data[1])  # Window size
    
    arr = list(map(int, data[2:]))  # Array elements
    
    result = count_balanced_subarrays(arr, k)
    print(result)


if __name__ == "__main__":
    main()