#challenge 5

import binascii 

def repeatinkeyxor(m, k):
	return bytes([m[i] ^ k[i % len(k)] for i in range(len(m))])

message = b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

key = b'ICE'

expectedc = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

if __name__ == '__main__':
	c = repeatinkeyxor(message,key)
	codec = binascii.hexlify(c).decode('ascii')
	if expectedc == codec:
		print('yay!')
	else:
		print('dang!')

'''
just for fun, we can do this on any text from the command line
umsg = input("enter the message to be encoded: ")
ukey = input("enter the key: ")
bmsg = bytes(umsg, 'ascii')
bkey = bytes(ukey, 'ascii')


ctext = repeatinkeyxor(bmsg,bkey)
text = binascii.hexlify(ctext).decode('ascii')
print("the hex representation of your cihertext is "+text)
'''