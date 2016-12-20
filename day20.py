def extendRanges(ranges):
    j = 0
    while j < len(ranges):
        l, r = ranges[j]
        added = False
        for i in range(len(ranges)):
            x, y = ranges[i]
            if l < x and r >= x-1:
                x = l
                y = r if r > y else y
                ranges[i] = (x,y)
                added = True
                break
            elif r > y and l <= y+1:
                y = r
                x = l if l < x else x
                ranges[i] = (x,y)
                added = True
                break
        if added:
            del ranges[j]
        j+=1
    ranges.sort(key=lambda tup:tup[0])
    return ranges

def generateRanges():
    input = open("inputs/day20.txt", "r")
    ranges = []
    for line in input:
        l, r = line.strip().split('-')
        l, r = int(l), int(r)
        added = False
        for i in range(len(ranges)):
            x, y = ranges[i]
            if l < x and r >= x-1:
                x = l
                y = r if r > y else y
                ranges[i] = (x,y)
                added = True
            elif r > y and l <= y+1:
                y = r
                x = l if l < x else x
                ranges[i] = (x,y)
                added = True
        if not added:
            ranges.append((l,r))
    ranges = list(set(ranges))
    ranges.sort(key=lambda tup:tup[0])
    input.close

    prevLen, shorten = len(ranges), True
    while shorten:
        ranges = extendRanges(ranges)
        shorten = True if len(ranges) < prevLen else False
        prevLen = prevLen = len(ranges)

    return ranges

def findAllowed(ranges):
    allowed = []
    for i in range(len(ranges)-1):
        x, y = ranges[i][1]+1, ranges[i+1][0]-1
        if x == y:
            allowed.append(x)
        else:
            allowed.append((x,y))
    return allowed


ranges = generateRanges()
allowed = findAllowed(ranges)
print('Lowest allowed IP:',allowed[0])
print('Count allowed IPs:',len(allowed))
