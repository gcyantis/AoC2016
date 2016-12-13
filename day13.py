import copy

def maxXY(path):
    maxX, maxY = 0, 0
    for coord in path:
        x,y = coord
        maxX = x if x > maxX else maxX
        maxY = y if y > maxY else maxY
    return(maxX,maxY)

def minLenList(listOfLists):
    min = 0
    for l in listOfLists:
        min = l if min == 0 or len(l) < len(min) else min
    return(min)

def isOpen(coord):
    x, y = coord
    fxy = (x*x + 3*x + 2*x*y + y + y*y) + 1362
    open = True if bin(fxy).count('1') % 2 == 0 else False
    return(open)

def search(end, path):
    current = path[len(path)-1]
    cardinal = [(0,1), (1,0), (0,-1), (-1,0)]
    found = False
    paths = []
    for direction in cardinal:
        new = tuple(x + y for x, y in zip(current, direction))
        if new == end:
            found = True
            path.append(new)
            #print("Found in {} steps".format(len(path)-1)
            break

        elif new[0] >= 0 and new[1] >= 0 and new not in path and isOpen(new):
            # and new[0] <= end[0] and new[1] <= end[1]
            newPath = copy.deepcopy(path)
            newPath.append(new)
            f, p = search(end, newPath)
            if f:
                found = True
                paths.append(p)

    path = minLenList(paths) if len(paths) else path

    return(found, path)

def radius(max, path, visited):
    if len(path) <= max+1:
        current = path[len(path)-1]
        cardinal = [(0,1), (1,0), (0,-1), (-1,0)]
        for direction in cardinal:
            new = tuple(x + y for x, y in zip(current, direction))
            if new[0] >= 0 and new[1] >= 0 and new not in path and isOpen(new):
                newPath = copy.deepcopy(path)
                newPath.append(new)
                visited.add(new)
                radius(max, newPath, visited)

def printMaze(path):
    maxX, maxY = maxXY(path)
    for y in range(maxY+2):
        line = ""
        for x in range(maxX+2):
            if (x,y) in path:
                line += 'O'
            else:
                line += '.' if isOpen((x,y)) else '#'
        print(line)

def part1():
    print("Part 1:")
    print("Searching...", end="\r")
    f, path = search((31,39),[(1,1)])
    print("End found in {} steps\n".format(len(path)-1))
    printMaze(path)
def part2():
    visited = set()
    radius(50, [(1,1)], visited)
    print("\nPart 2:\nVisited {} locations in 50 steps\n".format(len(visited)))
    printMaze(visited)

part1()
part2()
