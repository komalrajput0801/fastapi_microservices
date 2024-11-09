import base64 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

#CBC with Fix IV

from Crypto.Random.random import StrongRandom
import string

def generate_symmetric_key():
    """
    Generate a random symmetric encryption key (16 characters).
    """
    key_length = 16
    # Define character set for key generation
    characters = string.ascii_letters + string.digits
    # Use SystemRandom for cryptographic security
    sys_rand = StrongRandom()
    # Generate a random key by selecting characters from the defined set
    random_key = ''.join(sys_rand.choice(characters) for _ in range(key_length))
    return random_key

# Generate symmetric key

data = 'Hey, This is Komal'
key = generate_symmetric_key() #16 char for AES128
print("Symmetric Key (String):", key)

#FIX IV
iv =  generate_symmetric_key().encode('utf-8') #16 char for AES128

def encrypt(data,key,iv):
        data= pad(data.encode(),16)
        cipher = AES.new(key.encode('utf-8'),AES.MODE_CBC,iv)
        return base64.b64encode(cipher.encrypt(data))

def decrypt(enc,key,iv):
        enc = base64.b64decode(enc)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc),16)

encrypted = encrypt(data,key,iv)
print('encrypted CBC base64 : ',encrypted.decode("utf-8", "ignore"))

decrypted = decrypt(encrypted,key,iv)
print('data: ', decrypted.decode("utf-8", "ignore"))
