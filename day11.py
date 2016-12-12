testPuzzle = [  [('h','m'),('l','m')],
                [('h', 'g')],
                [('l', 'g')],
                []]

def checkSafe(floor, piece):
    element, type = piece

def solve(puzzle):
    steps, floor = 0, 0
    while len[puzzle[1]] < sum([len(x) for x in puzzle]):
        #check if moving each element is safe
        for piece in puzzle[floor]:
            if floor > 0: #check below
                checkSafe(puzzle[floor-1], piece)
            if floor < 3: #check above
                checkSafe(puzzle[floor+1], piece)

print("I cheated and solved using slips of paper...")
