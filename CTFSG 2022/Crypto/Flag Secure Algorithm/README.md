# Flag Secure Algorithm
 
## Challenge Description: Hello. I'm @CTFSG[-1]. And welcome to... CTF.SG Presents: Fun with Flags!

We are given the source code for an encryption service:

```python
from functools import reduce
import random
import string

def encod(s, o=0): return reduce(lambda a, b: a*256+b, map(ord, s), 0)

flag = '<CENSORED>' + '<SALT>'

def is_flag(c):
    return ((c[:6] == 'CTFSG{' and c[-1] == '}') or "\U0001F1E6\U0001F1E8" <= c <= "\U0001F1FF\U0001F1FC")

banner = 'banner'

if __name__ == '__main__':
    print(banner)
    print()
    for _ in range(2):
        text = input('Enter flag\n>')
        if not is_flag(text): break  # KEK
        print(pow(encod(text), 65537, encod(flag)))  # Encrypt our flag with the participant's flag!
```
From the source code, it seems like the server
1.  Receives user input and encodes it 
2.  Takes the encoded input and raises it to the power of **65537**
    * The encoding is bascially just an implementation of *bytes_to_long* from Crypto.Util.number
3.  Performs a modulus operation with the encoded value of the flag
4.  Returns the result 

We can see the code in action when we connect to the service

![service](https://user-images.githubusercontent.com/71312079/158062561-eb18026d-c3ee-407d-b168-2ad852a79b00.png)

From the following code, it appears that the flag needs to either be formatted properly or fall within certain unicode hex values in order for output to be produced.

```python
def is_flag(c):
    return ((c[:6] == 'CTFSG{' and c[-1] == '}') or "\U0001F1E6\U0001F1E8" <= c <= "\U0001F1FF\U0001F1FC")
```

Initially, I was very fixated on the latter portion involving the unicode values but gave up after it wasn't able to give me more information about the flag.

After thinking about the relation between the input and the output, I constructed the following equations:

* C1 = pow(M1,65537) % Flag
  * Rearranging: K1* Flag = C1 - pow(M1,65537)
* C2 = pow(M2,65537) % Flag
  * Rearranging: K2* Flag = C2 - pow(M2,65537)
* gcd(K1,K2) = 1 -> Flag = gcd(C1 - pow(M1,65537), C2 - pow(M2,65537)) 

From the equations above, the following script was crafted: 

```python
from Crypto.Util.number import long_to_bytes
from functools import reduce
from pwn import *
from math import gcd 

def encod(s, o=0): return reduce(lambda a, b: a*256+b, map(ord, s), 0)

p = remote('chals.ctf.sg',10101)

for i in range(0,10,2): #note multiple attempts needed because sometimes the gcd(K1,K2) != 1 resulting in gibberish output
    a1 = "CTFSG{" + str(i) + "}"
    b1 = "CTFSG{" + str(i+1) + "}"
    
    p.recvuntil('>')
    p.sendline(a1)
    a2 = p.recvline()

    p.recvuntil('>')
    p.sendline(b1)
    b2 = p.recvline()
    
    C1 = pow(encod(a1),65537)- int(a2[:-1])
    C2 = pow(encod(b1),65537)- int(b2[:-1])
    res  = long_to_bytes(gcd(C1,C2))
    if b"CTFSG{" in res:
        print(res)
        break
```
Running the code above produced the flag with the appended salt value.

![flag](https://user-images.githubusercontent.com/71312079/158063666-2f95ff01-b25c-4037-880d-aacb6edb47fa.png)


Flag: `CTFSG{Rev_Pwn_Web_and_Misc__Unreveling_the_mystery__that_all_ended_with_decoded_FLAGS}`