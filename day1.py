def part1():
    instructions = "L4, L3, R1, L4, R2, R2, L1, L2, R1, R1, L3, R5, L2, R5, L4, L3, R2, R2, L5, L1, R4, L1, R3, L3, R5, R2, L5, R2, R1, R1, L5, R1, L3, L2, L5, R4, R4, L2, L1, L1, R1, R1, L185, R4, L1, L1, R5, R1, L1, L3, L2, L1, R2, R2, R2, L1, L1, R4, R5, R53, L1, R1, R78, R3, R4, L1, R5, L1, L4, R3, R3, L3, L3, R191, R4, R1, L4, L1, R3, L1, L2, R3, R2, R4, R5, R5, L3, L5, R2, R3, L1, L1, L3, R1, R4, R1, R3, R4, R4, R4, R5, R2, L5, R1, R2, R5, L3, L4, R1, L5, R1, L4, L3, R5, R5, L3, L4, L4, R2, R2, L5, R3, R1, R2, R5, L5, L3, R4, L5, R5, L3, R1, L1, R4, R4, L3, R2, R5, R1, R2, L1, R4, R1, L3, L3, L5, R2, R5, L1, L4, R3, R3, L3, R2, L5, R1, R3, L3, R2, L1, R4, R3, L4, R5, L2, L2, R5, R1, R2, L4, L4, L5, R3, L4"
    instructions = instructions.strip()
    instructions = instructions.split(", ")

    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    turns = {"R":1, "L":-1}
    pos = (0,0)
    heading = 0

    for instruction in instructions:
        turn = instruction[0]
        blocks = int(instruction[1:])
        heading = (heading + turns[turn]) % len(directions)
        pos = tuple(x + (y * blocks) for x, y in zip(pos, directions[heading]))
        #print(pos)

    print("HQ is {} blocks away".format(abs(pos[0])+abs(pos[1])))

def part2():
    instructions = "L4, L3, R1, L4, R2, R2, L1, L2, R1, R1, L3, R5, L2, R5, L4, L3, R2, R2, L5, L1, R4, L1, R3, L3, R5, R2, L5, R2, R1, R1, L5, R1, L3, L2, L5, R4, R4, L2, L1, L1, R1, R1, L185, R4, L1, L1, R5, R1, L1, L3, L2, L1, R2, R2, R2, L1, L1, R4, R5, R53, L1, R1, R78, R3, R4, L1, R5, L1, L4, R3, R3, L3, L3, R191, R4, R1, L4, L1, R3, L1, L2, R3, R2, R4, R5, R5, L3, L5, R2, R3, L1, L1, L3, R1, R4, R1, R3, R4, R4, R4, R5, R2, L5, R1, R2, R5, L3, L4, R1, L5, R1, L4, L3, R5, R5, L3, L4, L4, R2, R2, L5, R3, R1, R2, R5, L5, L3, R4, L5, R5, L3, R1, L1, R4, R4, L3, R2, R5, R1, R2, L1, R4, R1, L3, L3, L5, R2, R5, L1, L4, R3, R3, L3, R2, L5, R1, R3, L3, R2, L1, R4, R3, L4, R5, L2, L2, R5, R1, R2, L4, L4, L5, R3, L4"
    #instructions = "R8, R4, R4, R8"
    instructions = instructions.strip()
    instructions = instructions.split(", ")

    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    turns = {"R":1, "L":-1}
    pos = (0,0)
    heading = 0
    visited = [(0,0)]
    found = False
    
    for instruction in instructions:
        turn = instruction[0]
        blocks = int(instruction[1:])
        heading = (heading + turns[turn]) % len(directions)
        for i in range(0,blocks):
            pos = tuple(x + y for x, y in zip(pos, directions[heading]))
            if pos in visited:
                found = True
                break
            else:
                visited.append(pos)
        if found:
            break
        #print(pos)
    #print(visited)
    print("HQ is {} blocks away".format(abs(pos[0])+abs(pos[1])))
part2()
