import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    e = int(next(iterator))
    
    initial_levels = [int(next(iterator)) for _ in range(n)]
    
    # Track the latest battery level and whether a collar is retired
    battery = [0] + initial_levels
    retired = [False] * (n + 1)
    
    # Version array to invalidate old heap entries when a collar is updated or retired
    version = [0] * (n + 1)
    
    # Min-heap storing tuples of (battery_level, collar_id, version_number)
    heap = []
    for i in range(1, n + 1):
        heapq.heappush(heap, (battery[i], i, version[i]))
        
    ans = []
    
    for _ in range(e):
        op = next(iterator)
        if op == "DRAIN":
            collar_id = int(next(iterator))
            amount = int(next(iterator))
            battery[collar_id] = max(0, battery[collar_id] - amount)
            version[collar_id] += 1
            heapq.heappush(heap, (battery[collar_id], collar_id, version[collar_id]))
            
        elif op == "RETIRE":
            collar_id = int(next(iterator))
            retired[collar_id] = True
            version[collar_id] += 1  # Invalidates any old heap entries for this collar
            
        elif op == "SERVICE":
            # Pop out-of-date or retired collars from the top of the heap
            while heap:
                lvl, idx, ver = heap[0]
                if retired[idx] or ver != version[idx]:
                    heapq.heappop(heap)
                else:
                    break
                    
            if not heap:
                ans.append("NONE")
            else:
                lvl, idx, ver = heapq.heappop(heap)
                ans.append(str(idx))
                # Reset collar to level 100
                battery[idx] = 100
                version[idx] += 1
                heapq.heappush(heap, (100, idx, version[idx]))
                
    sys.stdout.write("\n".join(ans) + "\n")

if __name__ == "__main__":
    solve()