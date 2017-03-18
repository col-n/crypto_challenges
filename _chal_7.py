#chal 7

import base64
from Crypto.Cipher import AES
#open the file and decode the base64'd text into raw bytes (cause we always deal in raw bytes people!)
f = base64.b64decode(open('7.txt','r').read())

key = b'YELLOW SUBMARINE'

#takes encrypted bytes and a key (also in bytes) and decrypts
def decrypt(text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(text)
    return plaintext

print(decrypt(f, key))