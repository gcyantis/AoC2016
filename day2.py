def findCode(keys,startPosition):
	pos = startPosition
	code = ""
	moves = {"U":(-1,0),"D":(1,0),"L":(0,-1),"R":(0,1)}
	
	input = open("inputs/day2.txt", "r")
	for line in input:
		#print(instructions)
		instructions = line.strip()
		for move in instructions:
			newPos = tuple(min(len(keys)-1, max(0,(x + y))) for x, y in zip(pos, moves[move]))
			if (keys[newPos[0]][newPos[1]] != 0):
				pos = newPos
			#print(keys[pos[0]][pos[1]])
		code += str(keys[pos[0]][pos[1]])
		#print code

	input.close()

	return(code)

def main():
	part1Keys = [[1,2,3],[4,5,6],[7,8,9]]
	part1Pos = (1,1)
	
	part2Keys = [[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,'A','B','C',0],[0,0,'D',0,0],]
	part2Pos = (2,0)
	
	print("Code for simple keypad: {}".format(findCode(part1Keys,part1Pos)))
	print("Code for complex keypad: {}".format(findCode(part2Keys,part2Pos)))
main()