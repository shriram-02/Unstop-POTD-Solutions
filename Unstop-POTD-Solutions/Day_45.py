def can_partition_k_subsets(arr, k):
    total = sum(arr)
    
    if total % k != 0:
        return False
    
    target = total // k
    arr.sort(reverse=True)
    
    if arr[0] > target:
        return False
    
    used = [False] * len(arr)
    
    def backtrack(start, curr_sum, subsets_left):
        if subsets_left == 1:
            return True
        
        if curr_sum == target:
            return backtrack(0, 0, subsets_left - 1)
        
        prev = -1
        for i in range(start, len(arr)):
            if used[i] or curr_sum + arr[i] > target or arr[i] == prev:
                continue
            
            used[i] = True
            if backtrack(i + 1, curr_sum + arr[i], subsets_left):
                return True
            used[i] = False
            
            prev = arr[i]
            
            if curr_sum == 0:
                break
        
        return False
    
    return backtrack(0, 0, k)


arr = list(map(int, input().split()))
k = int(input())

print(str(can_partition_k_subsets(arr, k)).lower())