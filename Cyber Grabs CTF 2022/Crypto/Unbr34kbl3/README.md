# Unbr34kbl3 (1000 points)

## Challenge Description: No one can break my rsa encryption, prove me wrong !!

NOTE: This was a difficult challenge and I did not solve it during the competition. It was a good challenge though so I did up a writeup for documentation purposes

* This challenge involves several steps so I split up my solution into parts that address each step 
* I used sagemath and had to type cast many of my variables as *int* to allow for arthimetic operations so sage doesn't throw me errors
* Full solution can be found [here](sol.py)

I am given a source python file and an output txt file with the following variables:

* n [Modulus]
* ip [Inverse of p mod q]
* iq [Inverse of q mod p]
* c1 [Result of encrypting 1st half of pt]
* c2 [Result of encrypting 2nd half of pt]

Looking at the source code: 

```python
from Crypto.Util.number import *
from secret import *

assert (x>2 and x%2 == 0)
assert (isPrime(e1) and isPrime(e2))

def functor():
    val1 , val2 = 0,0
    for i in range(x+1):
        val1 += pow(e1,i)
    for j in range(3):
        val2 += pow(e2,j)
    assert (val1 == val2)

def keygen():
    while True:
        p,q = [getStrongPrime(1024) for _ in range(2)]
        if p%4==3 and q%4==3:
            break

    r = 2
    while True:
        r = r*x
        if r.bit_length()>1024 and isPrime(r-1):
            r = r-1
            break

    return p,q,r

functor()
p,q,r = keygen()
n = p*q*r
ip = inverse(p,q)
iq = inverse(q,p)
c1 = pow(bytes_to_long(flag[0:len(flag)//2].encode('utf-8')),e1,n)
c2 = pow(bytes_to_long(flag[len(flag)//2:].encode('utf-8')),e2,n)
print(f"n:{n}",f"ip:{ip}",f"iq:{iq}",f"c1:{c1}",f"c2:{c2}",sep="\n")
```

After studying the source code, I see a couple of factors at play:

1. This is a *multi-prime* RSA challenge
2. The assert statement in *functor* appears to give me an equation to solve for **e1**, **e2** and **x**
3. I can obtain **r** after solving for **x**
4. I can obtain **p*q** after obtaining **r**

**Step 1: Obtain e1,e2 & x**

Since I am only given one equation and 3 unknowns, I create a list of primes up till *200* to be iterated through by **e1** and **e2**. Given that **x** is even and likely not greater than *20*, I also iterated through psssible values of **x** and ran the code below to obtain the 3 variables.

```python
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
for x in range(2,21,2):
    for e1 in primes:
        for e2 in primes:
            if sum([pow(e1,k) for k in range(1,x+1)]) == (e2 + pow(e2,2)) and e1 != e2:
                print(f"{e1=}")
                print(f"{e2=}")
                print(f"{x=}")
                break
# e1,e2,x = 2,5,4
```

**Step 2: Obtain r, pq**

After Step 1, it is now trivial to obtain r by using the same code provided to us. **pq** can also easily be found by dividing **n** by **r**.

```python
r = 2
while True:
    r = r*x
    if size(r) >1024 and isPrime(r-1):
        r = r-1
        break

pq = n // r
```

**Step 3: p and q**

Step 3 was considerably more challenging given that **pq** could not be easily factored. I know that the solution probably involves the variables **ip** and **iq** and so I do some research and found the following [writeup](https://gist.github.com/hellman/8e1793771cf240740b731c2b082b1ba2) of a similar CTF challenge. Hmm... seems like I need to construct 2 equations with the variables **p** and **q** and solve them together. 

```python
p,q = var('p q') 
eq1 = ip*q + iq*p == pq + 1
eq2 = p * q == pq

sols = solve([eq1, eq2], p, q,solution_dict=True)

for sol in sols:
    if int(sol[p]) % 4 == 3 and int(sol[q]) % 4 == 3:
        p = int(sol[p])
        q = int(sol[q])
        break
```

Given that **p** and **q** are both similar in size at *1024* bits, equation 1 from the other challenge would still hold. However, I had to tweak equation 2 since the other challenge had an unknown *n* but known *d*. Since we know *n*, we can just form an equation where **p*q = n**.

**Step 4: Finding m1**

Knowing that **e1=2** and that all of the **factors (p,q and r) % 4 == 3**, I discovered that this was characteristic of the *H-Rabin* cryptosystem. I found a [paper](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.1026.7187&rep=rep1&type=pdf) that provides details for decryption with 3 primes and followed the steps to develop the python script below. Given that there are multiple possible roots, I tested each root to see if it contains the known flag component and successfully obtained m1.

```python
#solving m1 - Rabin cryptosystem
r = int(r)
assert(r % 4 ==3)
mp = int(pow(c1,(p+1)//4 , p))
mq = int(pow(c1,(q+1)//4 , q))
mr = int(pow(c1,(r+1)//4 , r))

_mp = int(-mp % p)
_mq = int(-mq % q)
_mr = int(-mr % r)

b1 = int(inverse(n//p,p))
b2 = int(inverse(n//q,q))
b3 = int(inverse(n//r,r))

x1 = (mp*b1*(q*r) + mq*b2*(p*r) + mr*b3*(p*q)) % n
x2 = (_mp*b1*(q*r) + mq*b2*(p*r) + mr*b3*(p*q)) % n
x3 = (mp*b1*(q*r) + _mq*b2*(p*r) + mr*b3*(p*q)) % n
x4 = (mp*b1*(q*r) + mq*b2*(p*r) + _mr*b3*(p*q)) % n
x5 = n - x1
x6 = n - x2
x7 = n - x3
x8 = n - x4

combined = [x1,x2,x3,x4,x5,x6,x7,x8]
for pt in combined:
    m1 = long_to_bytes(pt)
    if b'cybergrabs{' in m1:
        print(m1)
        break
```

**Step 5: Finding m2**

Solving m2 was considerably easier since it was classic multi-prime RSA and running the script below yielded m2.

```python
#solving m2 - Multi prime RSA
phin = (p-1) * (q-1) * (r-1)
d = inverse(e2,phin)
m2 = long_to_bytes(pow(c2,int(d),n))
print(m2)
```

I combined both portions and obtained the flag.

FLAG: `cybergrabs{r481n_cryp70sy5t3m_15_1nt3r35t1n6_8ut_num83r_sy5t3m_15_3v3n_m0r3_1nt3r35t1n6} `