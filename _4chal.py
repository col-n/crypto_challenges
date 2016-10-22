#challenge 4
import binascii
import _3chal

def dlines(fname):
	with open(fname) as f:
		for line in f:
			if line[-1] == '\n':
				line = line[:-1]
			x = binascii.unhexlify(line)
			yield x

def findsbxor(lines):
	blines = [_3chal.bustxor(l)[1] for l in lines]
	def score (i):
		return _3chal.score(blines[i])
	maxi = max(range(len(blines)), key = score)
	return (maxi+1, blines[maxi])

if __name__ == '__main__':
	print(findsbxor(dlines('4.txt')))