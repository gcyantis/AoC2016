import re

fo = open("inputs/day22.txt", "r")
lines = fo.readlines()
fo.close()


for line in lines[2:]:
    filesystem, size, used, avail, use = line.strip().split()
    m = re.match(r'/dev/grid/node-x(\d+)-y(\d+)', filesystem)
    coords = (int(m.group(1)),int(m.group(2)))
    print(filesystem,coords, size, used, avail, use)
