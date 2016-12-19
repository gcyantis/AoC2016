from math import log, floor

#use these numbers to find pattern
def steal(elves, part, steps = False):
    elves = [str(i+1) for i in range(elves)]
    i = 0
    while len(elves) > 1:
        steals = (i+1) % len(elves) if part == 1 else (i + len(elves)//2) % len(elves)
        if steps:
            print(elves[i], 'steals from', elves[steals])
        del elves[steals]
        i = steals if part == 1 else ((i+1)% len(elves) if steals > i else i % len(elves))
    return elves

def printSeries(rows):
    #print series of answers to find functions
    print('/'+'-'*26+'\\')
    print('|{:^8}|{:^8}|{:^8}|'.format('Elves','Part 1', 'Part 2'))
    print('|'+'-'*26+'|')
    for i in range(rows):
        print('|{:>7} |{:>7} |{:>7} |'.format(i+1, steal(i+1,1)[0], steal(i+1,2)[0]))
    print('\\'+'-'*26+'/')

printSeries(32)

#Find winner for given number of elves
def part1Winner(x):
    return (x-2**(x.bit_length()-1))*2 + 1

def part2Winner(x):
    z = 3**(floor(log(x,3)))
    winner = x-z+((x//z)-1)*(x%z)
    return (winner if winner else x)

n = 3018458
print("\nPart 1: Winner", part1Winner(n))
print("Part 2: Winner", part2Winner(n))
