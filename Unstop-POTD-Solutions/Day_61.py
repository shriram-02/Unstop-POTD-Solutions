def solve():
    N = int(input())
    E = list(map(int, input().split()))
    T = list(map(int, input().split()))

    # Calculate the initial difference array: D[i] = T[i] - E[i]
    # Our goal is to make all D[i] <= 0
    # A positive wave (increase E) decreases D[i].
    # A negative wave (decrease E) increases D[i].
    D = [T[i] - E[i] for i in range(N)]

    total_operations = 0

    # Iterate until all elements in D are <= 0
    while any(val > 0 for val in D) or any(val < 0 for val in D):
        
        # Find the first non-zero element to start a segment operation
        start_index = -1
        for i in range(N):
            if D[i] != 0:
                start_index = i
                break
        
        if start_index == -1: # All elements are zero
            break

        current_sign = 1 if D[start_index] > 0 else -1
        
        # Determine the segment and the amount to apply
        end_index = start_index
        amount_to_apply = abs(D[start_index])

        for j in range(start_index + 1, N):
            if (D[j] > 0 and current_sign == 1) or \
               (D[j] < 0 and current_sign == -1):
                amount_to_apply = min(amount_to_apply, abs(D[j]))
                end_index = j
            else:
                break
        
        total_operations += amount_to_apply

        # Apply the operation to the identified segment
        for k in range(start_index, end_index + 1):
            if current_sign == 1: # Original D[k] was positive, so we reduce it
                D[k] -= amount_to_apply
            else: # Original D[k] was negative, so we increase it (towards 0)
                D[k] += amount_to_apply
    
    print(total_operations)

solve()