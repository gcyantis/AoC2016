def checkABBA(s):
    return()

def part1():
    input = open("inputs/day7.txt", "r")
    total = 0
    for line in input:
        line = line.strip()
        foundOutside, foundInside = False, False
        parts = [y for x in line.split(']') for y in x.split('[')]
        for i in range(len(parts)):
            part = parts[i]
            found = False
            for x in range(len(part)):
                s = part[x:x+4]
                if len(s)==4 and s[0]==s[3] and s[1]==s[2] and s[0]!=s[1]:
                    found = True
                    break
            if found and i % 2 == 0: #outside brackets
                foundOutside = True
            elif found and i % 2 == 1: #inside brackets
                foundInside = True
        if foundOutside and not foundInside:
            #print(line)
            total += 1
    input.close()
    print(total)
part1()

def part2():
    input = open("inputs/day7.txt", "r")
    total = 0
    for line in input:
        line = line.strip()
        abaList, babList = [], []
        parts = [y for x in line.split(']') for y in x.split('[')]
        for i in range(len(parts)):
            part = parts[i]
            found = []
            for x in range(len(part)):
                s = part[x:x+3]
                if len(s)==3 and s[0]==s[2] and s[0]!=s[1]:
                    found.append(s)
            if found and i % 2 == 0: #outside brackets
                abaList += found
            elif found and i % 2 == 1: #inside brackets
                babList += found
        if True in [a[0]==b[1] and b[0]==a[1] for b in babList for a in abaList]:
            total += 1
    input.close()
    print(total)
part2()
