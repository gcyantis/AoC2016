import string

def getParts(line):
	checksum = line[len(line)-6:len(line)-1]
	sector = int(line[line.rindex('-')+1:line.rindex('[')])
	name = line[:line.rindex('-')]
	return(name, sector, checksum)

def letterCounts(name):
	letters = {}
	for letter in name:
		if letter in letters:
			letters[letter] += 1
		else:
			letters[letter] = 1
	del letters['-']
	#print(letters)
	
	return letters

def compareChecksum(letters,checksum):
	sortedLetters = sorted(letters.items(), key=lambda tup: tup[0]) #sort alphbetically
	sortedLetters = sorted(sortedLetters, key=lambda tup: tup[1], reverse = True) #sort by counts
	top5 = [sortedLetters[i][0] for i in range(0,5)]
	#print(''.join(top5))
	
	compare = False
	if checksum == ''.join(top5):
		compare = True
		
	return compare		

def caesar(plaintext, shift, alphabet=string.ascii_lowercase):
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    return plaintext.translate(plaintext.maketrans(alphabet, shifted_alphabet))
	
def part1():
	sectorSum = 0
	input = open("inputs/day4-test.txt", "r")
	for line in input:
		name, sector, checksum = getParts(line.strip())
		if compareChecksum(letterCounts(name),checksum):
			sectorSum += sector
	print(sectorSum)
	input.close()

def part2():
	input = open("inputs/day4.txt", "r")
	for line in input:
		name, sector, checksum = getParts(line.strip())
		if compareChecksum(letterCounts(name),checksum):
			decoded = caesar(name,sector%26)
			if decoded == 'northpole-object-storage':
				print(sector)
	input.close()
part2()