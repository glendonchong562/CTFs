# Xmas Spirit (Day 2)

We are given the following *challenge.py* 

```python
#!/usr/bin/python3

import random
from math import gcd

def encrypt(dt):
	mod = 256
	while True:
		a = random.randint(1,mod)
		if gcd(a, mod) == 1: break
	b = random.randint(1,mod)

	res = b''
	for byte in dt:
		enc = (a*byte + b) % mod
		res += bytes([enc])
	return res

dt = open('letter.pdf', 'rb').read()

res = encrypt(dt)

f = open('encrypted.bin', 'wb')
f.write(res)
f.close()
```

From the python code, it seems like our goal is to reverse the encryption and retrieve the original pdf file. Since we know the file signature and thus first few bytes of a pdf file (```25 50 44 46 2D```) , we can determine **a** and **b** and thus undo the encryption to obtain the original pdf file.

In order to obtain **a** and **b**, we cycle through every possible combination and break out of the nested loop when there is a value of a and b that matches the first 2 bytes of the ciphertext. [Not sure if there's a faster way to do this but it shouldn't take so long since the only 256 values of b and even fewer values for a]

A dictionary is also used for the mappings of plaintext to ciphertexts.

```python
from math import gcd

mod = 256
gcd_set = []
ct = open('encrypted.bin', 'rb').read()

for i in range(mod):
    if gcd(i,mod) == 1:
        gcd_set.append(i)

#pdf header
header = [0x25,0x50,0x44,0x46,0x2D]

for x in gcd_set:
    for y in range(mod):
        if (x*header[0] + y) % mod == ct[0] and (x* header[1] + y) % mod == ct[1]:
            a = x
            b = y
            break
            break

# Verification for the other 3 bytes of the pdf header
for i in range(2,5):
    assert (a*header[i]+ b) % mod == ct[i]

mappings = {}
decrypted = []

for k in range(len(ct)):
    if ct[k] in mappings.keys():
        decrypted.append(mappings[ct[k]])
    else:
        for i in range(mod):
            enc = (a*i+ b) % mod
            if enc == ct[k]:
                mappings[ct[k]] = i
                decrypted.append(i)
                break

f = open('original.pdf', 'wb')
f.write(bytearray(decrypted))
f.close()
```



Running the code above and opening **original.pdf** reveals the flag.

Flag: `HTB{4ff1n3_c1ph3r_15_51mpl3_m47h5}`

NOTE: After completing the challenge, I went to do a bit more research into the affine cipher and found that my code to reverse the affine cipher could be greatly simplified: 

**Original Code**:
```python
for k in range(len(ct)):
    if ct[k] in mappings.keys():
        decrypted.append(mappings[ct[k]])
    else:
        for i in range(mod):
            enc = (a*i+ b) % mod
            if enc == ct[k]:
                mappings[ct[k]] = i
                decrypted.append(i)
                break
```

**Revised Code**:
```python
# Based on formula : pt = inverse(a) * (ct - b) % mod
from Crypto.Util.number import inverse
for k in range(len(ct)):
    decrypted.append((inverse(a,mod)*(ct[k] -b)) % mod)
```