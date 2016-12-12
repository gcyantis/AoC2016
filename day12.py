
def runAssembunny(registers, test=False):
    instructions = []
    input = open("inputs/day12"+("-test" if test else '')+".txt", "r")
    for line in input:
        instr = line.strip().split()
        if len(instr) < 3:
            instr.append('')
        instructions.append(instr)
    input.close()

    i = 0
    while i < len(instructions):
        instruct, x, y = instructions[i]
        if instruct == 'cpy':
            x = int(x) if x.isnumeric() else registers[x]
            registers[y] = x
        elif instruct == 'inc':
            registers[x] += 1
        elif instruct == 'dec':
            registers[x] -= 1
        elif instruct =='jnz':
            x = int(x) if x.isnumeric() else registers[x]
            y = registers[y] if y in registers else int(y)
            if x != 0:
                i = i + y - 1
        #print(' '.join(instructions[i]))

        i += 1
        #print(i, registers)

    print(registers)

def part1():
    registers = {'a':0, 'b':0, 'c':0, 'd':0}
    print("Part 1:")
    runAssembunny(registers)

def part2():
    registers = {'a':0, 'b':0, 'c':1, 'd':0}
    print("\nPart 2:")
    runAssembunny(registers)

part1()
part2()
