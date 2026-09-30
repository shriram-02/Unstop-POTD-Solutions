n, m = map(int, input().split()) 
doctorSpecs = list(map(int, input().split()))
shiftReqs = list(map(int, input().split()))
available = {}
for spec in doctorSpecs:
    available[spec] = available.get(spec, 0) + 1
unassigned = 0
for req in shiftReqs:
    if available.get(req, 0) > 0:
        available[req] -= 1
    else:
        unassigned += 1
print(unassigned)