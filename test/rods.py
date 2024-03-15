def countPoints(rings):
    rods = {}
    i = 1
    while i < len(rings) :
        if rings[i] not in rods:
            rods[rings[i]] = [rings[i-1]]
        else:
            rods[rings[i]].append(rings[i-1])
        i+= 2
    count = 0
    for x in rods:
        if 'R' in rods[x] and 'G'in rods[x] and 'B' in rods[x]:
            count += 1
    return count

print(countPoints("B9R9G0R4G6R8R2R9G9"))