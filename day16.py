def dragon(a):
    b = a[::-1]
    b = ''.join(['0' if c == '1' else '1' for c in b])
    return(a+'0'+b)

def checkSum(s):
    while len(s) % 2 == 0:
        new = ''
        for p in range(len(s)//2):
            new += '1' if s[p*2] == s[p*2+1] else '0'
        s = new
    return(s)

def fillDisk(disk, data = '11011110011011101'):
    while len(data) < disk:
        data = dragon(data)
    data = data[:disk]
    return(checkSum(data))

print("Checksum for Part 1:", fillDisk(272))
print("\nChecksum for Part 2: [computing...]", end="\r")
print("Checksum for Part 2:", fillDisk(35651584))
