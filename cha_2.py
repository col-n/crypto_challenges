#chal_2.py

e_s1 = '1c0111001f010100061a024b53535009181c'
e_s2 = '686974207468652062756c6c277320657965'
e_result = '746865206b696420646f6e277420706c6179'

result = hex(int(e_result,16))

xor = hex(int(e_s1, 16) ^ int(e_s2, 16))

if xor == result:
	print('yay!')
else:
	print('dang!')
