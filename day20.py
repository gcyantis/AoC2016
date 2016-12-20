def extendRanges(ranges):
    j = 0
    while j < len(ranges):
        l, r = ranges[j]
        added = False
        for i in range(len(ranges)):
            x, y = ranges[i]
            #check to see if span overlaps current range
            if (l < x and r >= x-1) or (r > y and l <= y+1):
                x, y = l if l < x else x, r if r > y else y
                ranges[i], added = (x,y), True
                break
        if added:
            del ranges[j]
        j+=1
    return ranges

def generateRanges():
    input = open("inputs/day20.txt", "r")
    ranges = []
    for line in input:
        l, r = [int(x) for x in line.strip().split('-')]
        ranges.append((l,r))
    input.close

    #clean up inputs: eliminate duplicates, then sort
    ranges = list(set(ranges))
    ranges.sort(key=lambda tup:tup[0])

    #ranges can overlap, so loop over ranges until none do anymore
    prevLen, condense = len(ranges), True
    while condense:
        ranges, condense, prevLen = extendRanges(ranges), True if len(ranges) < prevLen else False, len(ranges)

    return ranges

def findAllowed(ranges):
    #makes assumption that 0 and 4294967295 are blacklisted
    #allows for ranges of allowed, even though not needed by problem
    allowed = []
    for i in range(len(ranges)-1):
        x, y = ranges[i][1]+1, ranges[i+1][0]-1
        if x == y:
            allowed.append(x)
        else:
            allowed.append((x,y))
    return allowed

#Create blacklist, find allowed, output parts
blacklist = generateRanges()
allowed = findAllowed(blacklist)
print('Lowest allowed IP:', allowed[0])
print('Count allowed IPs:', len(allowed))
