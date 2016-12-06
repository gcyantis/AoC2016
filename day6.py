def part1():
    input = open("inputs/day6.txt", "r")
    columns = []
    for line in input:
        line = line.strip()
        if len(columns) == 0:
            columns = list(dict() for i in range(len(line)))
        for i in range(0,len(line)):
            char = line[i]
            if char in columns[i]:
                columns[i][char] += 1
            else:
                columns[i][char] = 1
    message=""
    for col in columns:
        message += max(col, key=lambda key: col[key])
    #print(columns)
    print(message)
    input.close()
part1()

def part2():
    input = open("inputs/day6.txt", "r")
    columns = []
    for line in input:
        line = line.strip()
        if len(columns) == 0:
            columns = list(dict() for i in range(len(line)))
        for i in range(0,len(line)):
            char = line[i]
            if char in columns[i]:
                columns[i][char] += 1
            else:
                columns[i][char] = 1
    message=""
    for col in columns:
        message += min(col, key=lambda key: col[key])
    #print(columns)
    print(message)
    input.close()
part2()
