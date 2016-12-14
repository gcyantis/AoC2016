from hashlib import md5
import re

def md5hash(str):
	return(md5(str.encode('utf-8')).hexdigest())

def stretch(hash, x=2016):
	for i in range(x+1):
		hash = md5(hash.encode('utf-8')).hexdigest()
	return(hash)


def part1():
	salt='ahsbgdzn'

	found = []
	quintuples = {}

	tx = re.compile(r'(.)\1{2}')
	qx= re.compile(r'(.)\1{4}')

	i = 0
	maxChecked = 0

	print("Found: 0", end='\r')
	while len(found) < 64:
		hash = md5hash(salt+str(i))
		
		t = tx.search(hash)
		if t:
			g = t.group()
			if g in quintuples:
				for j in quintuples[g]:
					if j > i and j <= i+1000:
						found.append(i)
						print("Found: {}".format(len(found)), end="\r")
						break
			else:
				for j in range(maxChecked+1, i+1001):
					maxChecked = j if j > maxChecked else maxChecked
					
					h = md5hash(salt+str(j))
					q = qx.search(h)
					if q:
						qg = q.group()
						
						if qg[:3] in quintuples:
							quintuples[qg[:3]].append(j)
						else:
							quintuples[qg[:3]] = [j]

						if qg[:3] == g:
							found.append(i)
							print("Found: {}".format(len(found)), end="\r")
							break
		i+=1
	print()
	print(len(found),max(found),found)

def part2():
	salt='ahsbgdzn'

	found = []
	quintuples = {}

	tx = re.compile(r'(.)\1{2}')
	qx= re.compile(r'(.)\1{4}')

	i = 0
	maxChecked = 0

	print("Found: 0", end='\r')
	while len(found) < 64:
		hash = stretch(salt+str(i))
		
		t = tx.search(hash)
		if t:
			g = t.group()
			if g in quintuples:
				for j in quintuples[g]:
					if j > i and j <= i+1000:
						found.append(i)
						print("Found: {}".format(len(found)), end="\r")
						break
			else:
				for j in range(maxChecked+1, i+1001):
					maxChecked = j if j > maxChecked else maxChecked
					
					h = stretch(salt+str(j))
					q = qx.search(h)
					if q:
						qg = q.group()
						
						if qg[:3] in quintuples:
							quintuples[qg[:3]].append(j)
						else:
							quintuples[qg[:3]] = [j]

						if qg[:3] == g:
							found.append(i)
							print("Found: {}".format(len(found)), end="\r")
							break
		i+=1
	print()
	print(len(found),max(found),found)

part1()
part2()