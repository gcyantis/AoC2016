def decompress(input):
	output, i = "", 0
	while i < len(input):
		if input[i] == '(':
			close = input.find(')',i+1)
			next, repeat = input[i+1:close].split('x')
			#print(next,repeat)
			output += input[close+1:close+1+int(next)]*int(repeat)
			i = close+1+int(next)
			#print(output)
		else:
			output += input[i]
			i += 1
			#print(output)
	return(output)

def lenDecompress(input):
	output, i = 0, 0
	while i < len(input):
		if input[i] == '(':
			close = input.find(')',i+1)
			next, repeat = input[i+1:close].split('x')
			output += lenDecompress(input[close+1:close+1+int(next)])*int(repeat)
			i = close+1+int(next)
		else:
			output += 1
			i += 1
	return(output)
	
def test1():
	print('Test 1')
	test = ["ADVENT","A(1x5)BC","(3x3)XYZ","A(2x2)BCD(2x2)EFG","(6x1)(1x3)A","X(8x2)(3x3)ABCY"]
	for t in test:
		d = decompress(t)
		print("Compressed: '{}' Decompressed: '{}' Len: {}".format(t,d,len(d)))
test1()
		
def part1():
	print('\nPart 1')
	input = open("inputs/day9.txt", "r")
	line = input.readline()
	print("Len Decompressed: {}".format(len(decompress(line.strip()))))
part1()


def test2():
	print('\nTest 2')
	test = ["(3x3)XYZ","X(8x2)(3x3)ABCY","(27x12)(20x12)(13x14)(7x10)(1x12)A","(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"]
	for t in test:
		print("Compressed: '{}' Len Decompressed: {}".format(t,lenDecompress(t)))	
test2()

def part2():
	print('\nPart 2')
	input = open("inputs/day9.txt", "r")
	line = input.readline()
	print("Len Decompressed: {}".format(lenDecompress(line.strip())))
part2()