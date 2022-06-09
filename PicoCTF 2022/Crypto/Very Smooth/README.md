# Very Smooth

## Forget safe primes... Here, we like to live life dangerously... >:)

For this challenge, we are given both the [source code](./gen.py) and the [output](./output.txt).

From the output, we are given both the value of the **ciphertext** and the **modulus**. From the challenge description, we know that the primes are not *safe*, which I understood to mean that (p-1)/2 might not also be a prime, where p represents the prime number. Knowing this did not help me much and I was slightly loss until the hint suggested that I ask *Mr.Pollard* for help. *Pollard* definitely sounded familiar, and a quick googling shows that I need to use **Pollard's *p* − 1** algorithm to factorise *n*.

In order to use the algorithm, the prime factors *p-1* and *q-1* need to be B-powersmooth, meaning that all its prime factors p\*\*v satisfy p**v <= B. [Reference]([Pollard's p − 1 algorithm - Wikipedia](https://en.wikipedia.org/wiki/Pollard's_p_%E2%88%92_1_algorithm))

We can see from a snippet from the source code below that the factors *p* and *q* are **16bit-powersmooth** and **17bit-powersmooth**. This means that all the factors of *p-1* are less than or equals to 2^16= **65536** and all the factors of *q-1* are less than or equals to 2^17= 131072. 

```python
while True:
    p, p_factors = get_smooth_prime(STATE, 1024, 16)
    if len(p_factors) != len(set(p_factors)):
        continue
    # Smoothness should be different or some might encounter issues.
    q, q_factors = get_smooth_prime(STATE, 1024, 17)
    if len(q_factors) != len(set(q_factors)):
        continue
    factors = p_factors + q_factors
    if e not in factors:
        break
```

As such, we can use the algorithm to solve our problem. I then crafted the following script to obtain the flag: 

```python
from Crypto.Util.number import *
import math

def  pollard (n):  # taken from https://oalieno.github.io/old/algorithm/factoring/pollard/
    a  =  2 
    b  =  2 
    while  True : 
        a  =  pow ( a ,  b ,  n ) 
        d  =  math . gcd ( a  -  1 ,  n ) 
        if  1  <  d  <  n :  return  d 
        b  +=  1

n = 0x6c5f4a08d820579e606aeb3800d1602c53825167d01bd7c87f43041afdc82877c50bbcc7830a0bf8c718fc9016e4a9e73ff0dfe1edd38688acb6add89b2bd6264d61e2ce0c9b3b0813b46b0eb1fcfc56b9f7f072ba2e1e986e6420f8ad9063e10fa9bca464b23fcf0135f95dc11a89bfddf2e81572c196f4362ea551aee18b343638d9d703b234e788bff4ddc3e885da77c7940a0fa670ddc1604646871f0739199fa7fa01f9ed7d84fb9f0cc82965450e7c97153fec84ef8e10a7fceb37a90e847a012528c733070e9ab751215b13a7e2d485089c0c4d00b81dbab382ef7681c717c76c2b14ce6495ef121540653561c3dd519c5f6e2ead18e9d90f3769a029
c = 0x42cbc15285a307d86ac5184c89d6bea5ebdc0a7546debedfe40af69fa6813eaf11ef86543349062587621b845e82817cf7f154c067733ee8b23a75e45861ee0c45a07e702dcb199adffa4ca0892fcd85abfe9e9b59c2ac2df7811a656a3fda16f385972107481409e33e820a19864233b8a35bc49734dc337786dc06c0460a4ec9fc06d16fd66a43654390a526ab0a6239b14427a9868399f6e4863ac04539690357e9a4fa67450286febd9a97dd07864f516f6756c2ffad0b1ba5882980f0089605f0def91120a80a448f77ec272be41de0e11695ba7d0c8899b1d9e8905a1b5e95a755e584dead086f35844052f261e8dcd0d6cffdce38cd5181235dfa0745

p = pollard(n)

e = 0x10001

q = n // p 
phi = (p-1)*(q-1)

d = inverse(e,phi)
m = pow(c,d,n)
print(long_to_bytes(m))
```

FLAG: `picoCTF{7c8625a1}`

NOTE: After solving the challenge, I realised that python's **primefac** library was able to implement *pollard's algorithm* for me and I will be using that in the future instead: 

```python
import gmpy2
import primefac 
q = primefac.pollard_pm1(n)
```
