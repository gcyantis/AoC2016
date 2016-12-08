import copy

def printScreen(screen):
    print()
    for row in screen:
        print(''.join(['#' if x else '.' for x in row]))

def countOn(screen):
    total = 0
    for row in screen:
        total += sum(row)
    return total

input = open("inputs/day8.txt", "r")
#screenX, screenY = 7, 3
screenX, screenY = 50, 6
screen = [[0 for x in range(screenX)] for y in range(screenY)]
#printScreen(screen)
for line in input:
    instr = line.strip().split()
    if instr[0] == 'rect':
        a,b = instr[1].split('x')
        for row in range(int(b)):
            for col in range(int(a)):
                screen[row][col] = 1
    elif instr[0] == 'rotate':
        a,b = int(instr[2].split('=')[1]), int(instr[4])
        if instr[1] == 'column':
            newScreen = copy.deepcopy(screen)
            for row in range(screenY):
                newScreen[row][a] = screen[(row - b) % screenY][a]
            screen = newScreen
        elif instr[1] == 'row':
            screen[a] = screen[a][screenX - b:] + screen[a][:screenX - b]
    #printScreen(screen)

input.close()

printScreen(screen)
print("\n{} pixels are lit".format(countOn(screen)))
