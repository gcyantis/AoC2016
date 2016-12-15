def incTime(values):
    t = 0
    while not all((t+v[1])%v[0] == 0 for v in values):
        t += 1
    return(t)

values, offsets, comb = [], [], []
input = open("inputs/day15.txt", "r")
for line in input:
    line = line.strip().split();
    d, n, t, p = int(line[1][1:]), int(line[3]), 0, int(line[11].strip('.'))
    comb.append((n, p+d))
input.close()

print("Part 1: T=",incTime(comb))

comb.append((11,0+len(comb)+1 ))
print("Part 2: T=",incTime(comb))
