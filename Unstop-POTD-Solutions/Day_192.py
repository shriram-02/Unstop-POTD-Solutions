import sys
from collections import deque

def solve():
    # Read all inputs from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    N = int(next(iterator))
    W = int(next(iterator))
    
    # Pre-allocate arrays for fast access
    times = [0] * N
    time_strs = [""] * N
    platforms = [0] * N
    latenesses = [0] * N
    
    # Parse input records
    for i in range(N):
        t_str = next(iterator)
        p = int(next(iterator))
        d = int(next(iterator))
        
        # Convert HH:MM time to total minutes
        h = int(t_str[0:2])
        m = int(t_str[3:5])
        
        times[i] = h * 60 + m
        time_strs[i] = t_str
        platforms[i] = p
        latenesses[i] = d

    # Array to track distinct platforms inside the current time window 
    # Max P is 100,000 per constraints, so 100,005 is safe
    platform_counts = [0] * 100005
    distinct_platforms = 0
    
    # Monotonic deque to track maximum lateness inside the sliding window
    dq = deque()
    left = 0
    
    max_pressure = -1
    best_time_str = ""
    
    for right in range(N):
        t_right = times[right]
        
        # 1. Advance the left pointer to remove expired trains from the window
        while left < right and times[left] <= t_right - W:
            p_left = platforms[left]
            platform_counts[p_left] -= 1
            if platform_counts[p_left] == 0:
                distinct_platforms -= 1
            
            # If the expired train is the maximum lateness, remove it from the deque
            if dq[0] == left:
                dq.popleft()
            left += 1
        
        # 2. Add the current train to the window
        p_right = platforms[right]
        if platform_counts[p_right] == 0:
            distinct_platforms += 1
        platform_counts[p_right] += 1
        
        # Maintain strictly decreasing latenesses in the monotonic deque
        d_right = latenesses[right]
        while dq and latenesses[dq[-1]] <= d_right:
            dq.pop()
        dq.append(right)
        
        # 3. Calculate pressure for the current moment
        current_max_lateness = latenesses[dq[0]]
        current_pressure = current_max_lateness * distinct_platforms
        
        # 4. Check for a new max pressure (first occurrence tie-breaker handles inherently via > instead of >=)
        if current_pressure > max_pressure:
            max_pressure = current_pressure
            best_time_str = time_strs[right]
            
    # Output the required format
    sys.stdout.write(f"{max_pressure} {best_time_str}\n")

if __name__ == '__main__':
    solve()