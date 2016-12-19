test1 = "..^^."
test2 = ".^^.^.^^^^"
input = "^^.^..^.....^..^..^^...^^.^....^^^.^.^^....^.^^^...^^^^.^^^^.^..^^^^.^^.^.^.^.^.^^...^^..^^^..^.^^^^"

def nextRow(row):
    newRow = ""
    traps = ['^^.','.^^','^..','..^']
    for x in range(len(row)):
        l = row[x-1] if x-1 >= 0 else '.'
        c = row[x]
        r = row[x+1] if x+1 < len(row) else '.'
        newRow += '^' if l+c+r in traps else '.'
    return(newRow)

def generateRows(row, rows):
    safe = row.count('.')
    for i in range(rows-1):
        row = nextRow(row)
        safe += row.count('.')
    print('Safe Tiles:',safe)


generateRows(input,40)
generateRows(input,400000)
