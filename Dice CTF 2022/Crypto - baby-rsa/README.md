# baby-rsa

## Challenge Description: I messed up prime generation, and now my private key doesn't work!

This RSA challenge was difficult mainly because **e** was not coprime with **phi(n)**. Instead, **phi(n)** was a multiple of **e^2** and thus no distinct inverse could be found. This also means that there are multiple solutions to the RSA equation. Additioanlly, **e** was also not coprime with **phi(p)** and **phi(q)**. The source code is as follows: 

```python
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

def getAnnoyingPrime(nbits, e):
	while True:
		p = getPrime(nbits)
		if (p-1) % e**2 == 0:
			return p

nbits = 128
e = 17

p = getAnnoyingPrime(nbits, e)
q = getAnnoyingPrime(nbits, e)

flag = b"dice{???????????????????????}"

N = p * q
cipher = pow(bytes_to_long(flag), e, N)

print(f"N = {N}")
print(f"e = {e}")
print(f"cipher = {cipher}")
```
I've only ever had to take the square/cube root of a ciphertext before but to take the 17th root? I searched online and a teammate linked this [writeup](https://blog.soreatu.com/posts/intended-solution-to-crypto-problems-in-nctf-2019/#easyrsa909pt-2solvers) describing a similar CTF challenge.

The author of the writeup suggests that instead of **mod n**, we break the problem down into **mod p** and **mod q**. This is possible because **n** is a weak prime, and I easily factored it using http://factordb.com to **p** and **q**. Using sagemath, we can quickly obtain the roots of:
* m^e - c = 0 mod p 
  * Roots: x1,x2,x3...x17
* m^e - c = 0 mod q
  * Roots: y1,y2,y3...y17

We then combine these 2 sets of roots to find a value of our **pt** that satisfies the following equations: 

* pt = X mod p
* pt = Y mod q
* pt contains **'dice{'**

X and Y refer to one of the roots in the set of 17 roots for **mod p** and **mod q** respectively. Putting all together in a script below and running it produced our flag. 

```python
from Crypto.Util.number import long_to_bytes
c = 19441066986971115501070184268860318480501957407683654861466353590162062492971
n = 57996511214023134147551927572747727074259762800050285360155793732008227782157
p = 172036442175296373253148927105725488217
q = 337117592532677714973555912658569668821
e = 17
      
P.<a>=PolynomialRing(Zmod(p))
f=a^e-c
mps=f.roots()
      
P.<a>=PolynomialRing(Zmod(q))
g=a^e-c
mqs=g.roots()
      
for mpp in mps:
    x=mpp[0]
    for mqq in mqs:
      y=mqq[0]
      res = CRT_list([int(x), int(y)], [p, q])
      pt = long_to_bytes(res)
      if b'dice{' in pt:
        print(pt)
        break

```

FLAG: `dice{cado-and-sage-say-hello}`
