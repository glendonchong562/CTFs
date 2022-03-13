# XOR can't be that hard
 
## Challenge Description: XorXorXorXorXorXorXorXorXorXorXorXorXorXorXorXor

We are given the encryption source code along with the [ciphertext](./ct).

```python
import os
import string
import random
from itertools import cycle
from hashlib import sha1

allowed_chars = string.ascii_lowercase + '_- .!?'
allowed_chars = allowed_chars.encode('utf-8')

xor_enc = lambda pt,key: [x^y for x,y in zip(pt, cycle(key))]

pt  = [allowed_chars[i&31] for i in os.urandom(0x100000)]
key = os.urandom(random.randint(10,0x1000))

ct = xor_enc(pt, key)

open('flag', 'w').write("CTFSG{%s}"%sha1(bytes(pt)).hexdigest())
open('ct', 'wb').write(bytes(ct))
```

I solved the challenge with the following steps:
1. Determine the key length
2. Determine the key value 
3. Reverse the XOR operation by XORing the ct with the cycled key
4. Obtain the SHA1 digest of the pt

Running the script below produced the flag:

```python
from itertools import cycle
from hashlib import sha1
import string

allowed_chars = string.ascii_lowercase + '_- .!?'
allowed_chars = allowed_chars.encode('utf-8')

ct = open('ct', 'rb').read()
length = len(ct)

xor_enc = lambda ct,key: [x^y for x,y in zip(ct, cycle(key))] # given XOR function

def testvalidchar(subset): #checks if the result of XOR is in allowable_chars
    for h in range(256):
        for i in range(len(subset)):
            if subset[i] ^ h not in allowed_chars:
                break 
            if i == len(subset) - 1: # this is the correct value since the resultant character in subset after XOR is in allowable_char
                return bytes([h])
    return False

def testkeylen(i):
    subsets = [ct[k:length:i] for k in range(5)] # 5 was just a arbitrary number I used because testing only 2/3 subsets gave me too many possible keylengths
    return all([testvalidchar(subset) for subset in subsets])
    
def brutekey(keylen):
    key = b""
    for k in range(keylen):
        subset = ct[k:length:keylen]
        key += testvalidchar(subset)
    return key


def findkeylen():
    for keylen in range(10,0x1000):
        if testkeylen(keylen):
            print(keylen) # Yielded 2 values of 1596 and 3192 which is a multiple of 1596 so I just used 1596

findkeylen() # Step 1: Determine keylength      
key  = brutekey(1596) # Step 2: Determine key value
pt = xor_enc(ct,key) # Step 3: Reverse XOR
print("CTFSG{" + sha1(bytes(pt)).hexdigest() + "}") # Step 4: SHA1 digest
```

Flag: `CTFSG{81aee17d64bd59cd167ffce34523060f7e2bcac0}`