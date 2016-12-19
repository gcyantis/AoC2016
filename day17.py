from hashlib import md5

def minListInList(lists):
    smallest = 0
    for l in lists:
        smallest = l if smallest == 0 or len(l) < len(smallest) else smallest
    return smallest

def maxListInList(lists):
    biggest = 0
    for l in lists:
        biggest = l if biggest == 0 or len(l) > len(biggest) else biggest
    return biggest

def checkDoors(pos, code, path, end = (3,3)):
    moves = ['U','D','L','R']
    directions = {"U":(0,-1),"D":(0,1),"L":(-1,0),"R":(1,0)}
    paths = []
    hash = md5((code+path).encode('utf-8')).hexdigest()
    for c in range(4):
        if hash[c] in ['b','c','d','e','f']:
            newPos = tuple(x + y for x, y in zip(pos, directions[moves[c]]))
            if newPos == end:
                paths.append(path+moves[c])
            elif newPos[0] >= 0 and newPos[0] < 4 and newPos[1] >= 0 and newPos[1] < 4:
                paths += checkDoors(newPos, code, path+moves[c])
    return(paths)

paths = checkDoors((0,0),'pslxynzg','')
print('Shortest Path:', minListInList(paths))
print('Length Longest Path:', len(maxListInList(paths)))
