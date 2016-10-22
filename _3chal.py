#challenge 3
import string
import binascii
from Crypto.Util.strxor import strxor_c
#http://www.data-compression.com/english.html

freqs = '0.0651738 0.0124248 0.0217339 0.0349835 0.1041442 0.0197881 0.0158610 0.0492888 0.0558094 0.0009033 0.0050529 0.0331490 0.0202124 0.0564513 0.0596302 0.0137645 0.0008606 0.0497563 0.0515760 0.0729357 0.0225134 0.0082903 0.0171272 0.0013692 0.0145984 0.0007836 0.1918182'
freqs = freqs.split()
freqs = [float(i) for i in freqs]
letters = list(string.ascii_uppercase)
letters.append(' ')
fdict = dict(zip(letters, freqs))

def score(x):
	score = 0
	for i in x:
		char = chr(i).upper()
		if char in fdict:
			score += fdict[char]
	return score

def bustxor(x):
	def key(p):
		return score(p[1])
	return max([(i, strxor_c(x,i)) for i in range(0,256)], key = key)

def showtext(x):
	u = binascii.unhexlify(x)
	b_c = bustxor(u)
	return chr(b_c[0]), b_c[1]

if __name__ == '__main__':
	myster_code = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

	code = showtext(myster_code)

	print(code)

#u_m = binascii.unhexlify(myster_code)
#broken_code = bustxor(u_m)
#print('the key is',chr(broken_code[0]),'and the message is:',broken_code[1].decode('utf-8'))
