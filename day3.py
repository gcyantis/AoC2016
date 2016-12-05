def checkTriangular(sides):
	c = max(sides)
	sides.remove(c)
	a,b = sides
	
	isTriangular = False
	if (a+b > c):
		isTriangular = True
	return(isTriangular)

def part1():	
	countPossible = 0
	input = open("inputs/day3.txt", "r")
	for line in input:
		line.rstrip()
		sides = [int(line[i*5:(i+1)*5].strip()) for i in range(0,3)]
		if(checkTriangular(sides)):
			countPossible += 1
	input.close()
	print(countPossible)
	
def part2():
	countPossible = 0
	input = open("inputs/day3.txt", "r")
	lineCount = 0
	triangles = [[0,0,0],[0,0,0],[0,0,0]]
	for line in input:
		r = (lineCount % 3)
		for i in range(0,3):
			triangles[i][r] = int(line[i*5:(i+1)*5].strip())
		
		if (r == 2):
			for triangle in triangles:
				if(checkTriangular(triangle)):
					countPossible += 1
			triangles = [[0,0,0],[0,0,0],[0,0,0]]
			
		lineCount += 1
	input.close()
	print(countPossible)

	
part2()