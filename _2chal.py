#chal_2.py

e_s1 = '1c0111001f010100061a024b53535009181c'
e_s2 = '686974207468652062756c6c277320657965'
e_result = '746865206b696420646f6e277420706c6179'

result = hex(int(e_result,16))

def strxor(a,b):
	a = int(a,16)
	b = int(b,16)
	return hex(a ^ b)

xor = strxor(e_s1,e_s2)

'''
if xor == result:
	print('yay!')
else:
	print('dang!')
'''