from hashlib import md5

def md5hash(str):
	return(md5(str.encode('utf-8')).hexdigest())

def part1():
	door = 'ffykfhsq'
	i = 1
	password = ''

	while len(password) < 8:
		hash = md5hash(door+str(i))
		if hash[0:5] == '00000':
			password += hash[5]
		i += 1

	print(password)

def part2():
	door = 'abc'
	i = 1
	password = ['_','_','_','_','_','_','_','_',]
	print("Generating Password: "+''.join(password), end="\r")
	while '_' in password:
		hash = md5hash(door+str(i))
		if hash[0:5] == '00000':
			pos = hash[5]
			if pos.isnumeric() and int(pos) < 8 and password[int(pos)] == '_':
				password[int(pos)] = hash[6]
				print("Generating Password: "+''.join(password), end="\r")
		i += 1
	print("     Found Password: "+''.join(password))
part2()
