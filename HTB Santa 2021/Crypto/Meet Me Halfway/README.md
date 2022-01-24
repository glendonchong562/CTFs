# Meet Me Halfway (Day 4)

Similar to day 2, we are given the following *challenge.py*.

```python
from random import randint
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import json

flag = b'HTB{dummyflag}'

def gen_key(option=0):
    alphabet = b'0123456789abcdef'
    const = b'cyb3rXm45!@#'
    key = b''
    for i in range(16-len(const)):
        key += bytes([alphabet[randint(0,15)]])

    if option:
        return key + const
    else:
        return const + key

def encrypt(data, key1, key2):
    cipher = AES.new(key1, mode=AES.MODE_ECB)
    ct = cipher.encrypt(pad(data, 16))
    cipher = AES.new(key2, mode=AES.MODE_ECB)
    ct = cipher.encrypt(ct)
    return ct.hex()


def challenge():
    k1 = gen_key()
    k2 = gen_key(1)
    ct = encrypt(flag, k1, k2)
    
    print('Super strong encryption service approved by the elves X-MAS spirit.\n'+\
                    'Message for all the elves:\n' +ct + '\nEncrypt your text:\n> ')
    try:        
        dt = json.loads(input().strip())
        pt = bytes.fromhex(dt['pt'])
        res = encrypt(pt, k1, k2)
        print(res + '\n')
        exit(1)
    except Exception as e:
        print(e)
        print('Invalid payload.\n')
        exit(1)
    
if __name__ == "__main__":
    challenge()
```
Right off the bat we see that **2** keys are being generated for the AES encryption, consisting of a constant string ```(cyb3rXm45!@#)``` as well as **4** random alphanumeric characters. The random characters are appended to one key and prepended to the other key.

In addition, we are also given the **ciphertext** as well as the option to encrypt a plaintext of our choosing. The plaintext has to be formatted in the following manner: ```{"pt"}:"<value>"}```

I spent quite awhile thinking if I had to brute force both keys (I remember AES ECB is quite a weak algorithm?) and tried unsuccessfully for awhile before I realised that it would take too long.

In the end I found a hint in the challenge name (*Halfway*) and thought about having 2 dictionaries:
* 1 for mapping the intermediate ciphertext after encryption with key 1 to the plaintext
* 1 for mapping the intermediate ciphertext after decryption with key 2 to the final ciphertext

Finding a match for the intermediate ciphertext between the dictionary mappings would thus allow us to retrieve both keys and decrypt the actual ciphertext.

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import json
from pwn import *

def gen_key(option,ls):
    alphabet = b'0123456789abcdef'
    const = b'cyb3rXm45!@#'
    key = b''
    for i in range(4):
        key += bytes([alphabet[ls[i]]])
    if option:
        return key + const
    else:
        return const + key

def encrypt(data, key1):
    cipher = AES.new(key1, mode=AES.MODE_ECB)
    ct = cipher.encrypt(pad(data, 16))
    return ct.hex()
    
def decrypt(data,key2):
    cipher = AES.new(key2, mode=AES.MODE_ECB)
    pt = cipher.decrypt(data)
    return pt.hex()
    
combinations = []
for i in range(16):
    for k in range(16):
        for s in range(16):
            for t in range(16):
                combinations.append([i,k,s,t])

test = b"""{"pt":"0000"}"""
dt = json.loads(test.strip())
pt_test = bytes.fromhex(dt['pt'])

p = remote('134.209.186.58', 30549)
p.recvuntil("elves:\n")
ct = p.recvuntil("\n").strip()
p.recvuntil("\n"))
p.sendline(test)
test_enc = p.recvuntil("\n").strip()

encrypt_map = {}
decrypt_map = {}
for sublist in combinations:
    k1 = gen_key(0,sublist)
    k2 = gen_key(1,sublist)
    encrypt_map[encrypt(pt_test,k1)] = k1
    decrypt_map[decrypt(bytes.fromhex(test_enc),k2)] = k2

for value in encrypt_map.keys():
    if value in decrypt_map.keys():
        k1 = encrypt_map[value]
        k2 = decrypt_map[value]
        break

halfway = bytes.fromhex(decrypt(bytes.fromhex(ct),k2))
plain = decrypt(halfway,k1)
print(bytes.fromhex(plain))
```

Running the code above provides us with a Youtube [link](https://www.youtube.com/watch?v=DZMv9XO4Nlk) to the song *Let It Snow* in 8-bit version and the flag.

Flag: HTB{m337_m3_1n_7h3_m1ddl3_0f_3ncryp710n}