import sys

input = sys.stdin.readline

Q = int(input())
events = []
eras = set()

for _ in range(Q):
    parts = input().split()
    typ, s, era = parts[0], parts[1], int(parts[2])
    events.append((typ, s, era))
    eras.add(era)

era_id = {x: i for i, x in enumerate(eras)}

# Trie node: children, counts by era
children = [{}]
counts = [{}]

for typ, s, era in events:
    if typ == "ADD":
        node = 0
        eid = era_id[era]

        if eid not in counts[node]:
            counts[node][eid] = 0
        counts[node][eid] += 1

        for ch in s:
            if ch not in children[node]:
                children[node][ch] = len(children)
                children.append({})
                counts.append({})

            node = children[node][ch]

            if eid not in counts[node]:
                counts[node][eid] = 0
            counts[node][eid] += 1

    else:
        node = 0
        found = True

        for ch in s:
            if ch not in children[node]:
                found = False
                break
            node = children[node][ch]

        if not found:
            print(0)
        else:
            print(counts[node].get(era_id.get(era, -1), 0))