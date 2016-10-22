#challenge 1
import binascii
import base64

def hex_64(i):
	decoder = binascii.unhexlify(x)
	return base64.b64encode(decoder).decode('ascii')

x = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

should_y = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

y = hex_64(x)

if y == should_y:
	print('yay!')
else:
	print('dang!')