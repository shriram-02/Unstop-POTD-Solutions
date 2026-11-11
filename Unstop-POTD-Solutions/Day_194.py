from collections import deque, defaultdict

n, w = map(int, input().split())

q = deque()
freq = defaultdict(int)

distinct = 0
peak = 0
earliest = 0

for _ in range(n):
    t, species = map(int, input().split())

    q.append((t, species))
    freq[species] += 1

    if freq[species] == 1:
        distinct += 1

    while q and q[0][0] <= t - w:
        old_t, old_species = q.popleft()
        freq[old_species] -= 1

        if freq[old_species] == 0:
            distinct -= 1

    if distinct > peak:
        peak = distinct
        earliest = t

print(f"PEAK {peak} AT {earliest}")