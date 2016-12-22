password = 'abcdefgh'

input = open("inputs/day21.txt", "r")

print(password)
for line in input:
    print(line.strip())
    instr = line.strip().split()
    operation, type = instr[0] , instr[1]
    if operation == 'swap':
        if type == 'position':
            pX, pY = int(instr[2]), int(instr[5])
            password = list(password)
            x, y = password[pX], password[pY]
            password[pX], password[pY] = y, x
            password = ''.join(password)

        elif type == 'letter':
            x, y = password.find(instr[2]), password.find(instr[5])
            password = list(password)
            password[x], password[y] = instr[5], instr[2]
            password = ''.join(password)

    elif operation == 'rotate':
        if type == 'left' or type == 'right':
            direction = type.split
            steps = (int(instr[2]) % len(password))
            steps = len(password) - steps if type == 'right' else steps
            password = password[steps:] + password[:steps]

        elif type == 'based':
            pX = password.find(instr[6])
            pX += 2 if pX >= 4 else 1
            steps = len(password) - (pX % len(password))
            password = password[steps:] + password[:steps]

    elif operation == 'reverse':
        x, y = int(instr[2]), int(instr[4])
        password = password[:x]+password[y:x:-1]+password[x]+password[y+1:]

    elif operation == 'move':
        x, y = int(instr[2]), int(instr[5])
        password = list(password)
        l = password[x]
        del password[x]
        password.insert(y,l)
        password = ''.join(password)

    print(password)
