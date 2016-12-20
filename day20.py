def extendRanges(ranges):
    #requires that ranges be sorted by x for (x,y) ranges in ascending order
    i = 0
    while i < len(ranges)-1:
        j = i + 1
        while j < len(ranges) and ranges[j][0] <= ranges[i][1] + 1:
            ranges[i] = (ranges[i][0], ranges[j][1] if ranges[j][1] > ranges[i][1] else ranges[i][1])
            del ranges[j]
        i += 1
    return ranges

def generateRanges():
    input = open("inputs/day20.txt", "r")
    ranges = []
    for line in input:
        l, r = [int(x) for x in line.strip().split('-')]
        ranges.append((l,r))
    input.close

    #clean up inputs: eliminate duplicates, sort, then extend overlapped
    ranges = list(set(ranges))
    ranges.sort(key=lambda tup:tup[0])
    ranges = extendRanges(ranges)

    return ranges

def findAllowed(ranges):
    #makes assumption that 0 and 4294967295 are blacklisted
    allowed = []
    for i in range(len(ranges)-1):
        allowed.append(ranges[i][1]+1)
    return allowed

#Create blacklist, find allowed, output parts
blacklist = generateRanges()
allowed = findAllowed(blacklist)
print('Lowest allowed IP:', allowed[0])
print('Count allowed IPs:', len(allowed))
