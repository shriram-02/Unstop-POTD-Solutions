import sys

# Function to read input efficiently
def get_ints():
    return list(map(int, sys.stdin.readline().split()))

def get_int():
    return int(sys.stdin.readline())

class SegmentTree:
    def __init__(self, N, A):
        self.N = N
        self.tree = [([0] * 8, 0) for _ in range(4 * N)]  # (counts_array, lazy_xor)
        self.build(1, 1, N, A)

    def build(self, node_idx, start, end, A):
        if start == end:
            self.tree[node_idx][0][A[start - 1]] = 1
        else:
            mid = (start + end) // 2
            self.build(2 * node_idx, start, mid, A)
            self.build(2 * node_idx + 1, mid + 1, end, A)
            self._merge_counts(node_idx)

    def _merge_counts(self, node_idx):
        # Merge counts from left and right children
        left_child_counts = self.tree[2 * node_idx][0]
        right_child_counts = self.tree[2 * node_idx + 1][0]
        
        current_counts = [0] * 8
        for i in range(8):
            current_counts[i] = left_child_counts[i] + right_child_counts[i]
        self.tree[node_idx] = (current_counts, self.tree[node_idx][1]) # Keep existing lazy_xor

    def _apply_xor_to_counts(self, counts, mask):
        new_counts = [0] * 8
        for i in range(8):
            new_counts[i ^ mask] += counts[i]
        return new_counts

    def _push_down(self, node_idx):
        lazy_mask = self.tree[node_idx][1]
        if lazy_mask != 0:
            # Apply lazy_mask to children's counts
            self.tree[2 * node_idx] = (self._apply_xor_to_counts(self.tree[2 * node_idx][0], lazy_mask),
                                       self.tree[2 * node_idx][1] ^ lazy_mask)
            
            self.tree[2 * node_idx + 1] = (self._apply_xor_to_counts(self.tree[2 * node_idx + 1][0], lazy_mask),
                                           self.tree[2 * node_idx + 1][1] ^ lazy_mask)
            
            # Reset current node's lazy_xor
            self.tree[node_idx] = (self.tree[node_idx][0], 0)

    def update_range(self, node_idx, start, end, L, R, M):
        # If current segment is completely outside the query range
        if R < start or end < L:
            return

        # If current segment is completely inside the query range
        if L <= start and end <= R:
            self.tree[node_idx] = (self._apply_xor_to_counts(self.tree[node_idx][0], M),
                                   self.tree[node_idx][1] ^ M)
            return

        # Partial overlap, push down lazy tag and recurse
        self._push_down(node_idx)
        mid = (start + end) // 2
        self.update_range(2 * node_idx, start, mid, L, R, M)
        self.update_range(2 * node_idx + 1, mid + 1, end, L, R, M)
        
        # After children are updated, re-merge their counts
        self._merge_counts(node_idx)

    def query_range(self, node_idx, start, end, L, R):
        # If current segment is completely outside the query range
        if R < start or end < L:
            return [0] * 8  # Return an empty counts array

        # If current segment is completely inside the query range
        if L <= start and end <= R:
            return self.tree[node_idx][0] # Return the counts array

        # Partial overlap, push down lazy tag and recurse
        self._push_down(node_idx)
        mid = (start + end) // 2
        left_counts = self.query_range(2 * node_idx, start, mid, L, R)
        right_counts = self.query_range(2 * node_idx + 1, mid + 1, end, L, R)

        # Merge results from children
        result_counts = [0] * 8
        for i in range(8):
            result_counts[i] = left_counts[i] + right_counts[i]
        return result_counts


# Main part of the solution
N, Q = get_ints()
A = get_ints()

seg_tree = SegmentTree(N, A)

results = []
for _ in range(Q):
    query = get_ints()
    type = query[0]
    
    if type == 1:
        L, R, M = query[1], query[2], query[3]
        seg_tree.update_range(1, 1, N, L, R, M)
    else:
        L, R = query[1], query[2]
        counts = seg_tree.query_range(1, 1, N, L, R)
        max_freq = 0
        for count in counts:
            max_freq = max(max_freq, count)
        results.append(max_freq)

for res in results:
    sys.stdout.write(str(res) + "\n")