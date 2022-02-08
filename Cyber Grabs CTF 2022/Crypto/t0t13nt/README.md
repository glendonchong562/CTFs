# t0t13nt (200 points)
 
## Challenge Description: numbers numbers everywhere , why cant they leave me alone

This was an interesting challenge that inolves the *totient* function. I am given two files:
* [source_1.py](./source_1.py) - Source code for the challenge
* [output_1.py](./output_1.txt) - Output from source_1.py

Examining the source code, I note that every byte in the flag is multiplied by *6969696969* and passed to the *functor* function that performs addition operations involving the totient function. Seeing the nested loop and the large value of n tells me that I can't simply iterate through every possible byte and pass each value to *functor* as it would take a long time.

```python
def functor(n):
    val = 0
    for j in tqdm(range(1,n+1)):
        for i in range(1,j+1):
            val += j//i * totient(i)
    return val

lest = []
for i in flag:
    lest.append(functor(ord(i)*6969696969))

print(lest)
```
I'm not the most familiar with the totient function and I stumbled upon this [link](https://math.stackexchange.com/questions/8002/identity-involving-eulers-totient-function-sum-limits-k-1n-left-lfloor) which provides an identity that would be useful for our challenge:

![Identity involving Euler's totient function](https://user-images.githubusercontent.com/71312079/153015599-74c6ac82-1c7e-4f23-a43e-ef261574232a.png)

Having the identity above would greatly simplify our nested loop calculation, but we still need to sum up all values until n to fulfill this first loop. In essence, we need to apply the formula above to every value from 1 to n and sum them all up. 

I needed a bit of refresher on summation and so I referenced this [link](https://brilliant.org/wiki/sum-of-n-n2-or-n3/) to find the summation of **n** and **n^2**. I sketched it out in the diagram below: 

![summation](https://user-images.githubusercontent.com/71312079/153031631-a0ad358b-e18b-4087-bb76-8907904c8732.png)

After removing both loops, I can now map each plaintext character to its output and compare it with the given output to obtain our flag.

```python
from sympy import totient
import string 

def functor_simplified(n):
    return (n*(n+1)*(2*n+1)//6 + (n*(n+1))//2) // 2
    
output = [54751499983812600001595164999947606, 99964672809872376546137976728298625, 53109066146380481534971079770844564, 58137259942365444979479997549034855, 83599752542227961885740894770768516, 61659800043905527133538302215438384, 83599752542227961885740894770768516, 51499811650564080459894297372806965, 53109066146380481534971079770844564, 85819100646121058196943447618203070, 105003982813844976161353898313196914, 8400749730877624158255771399988559, 6240424741484609266392009977454864, 73075186383278314052649120872243371, 7485157899144949411682111055590430, 48379486424936974614387887472243260, 59881263192906899425738121667861480, 90374940243693329303922258576171375, 75104938249367345681206971604866080, 54751499983812600001595164999947606, 9388117281207654321254731172830840, 6638633268326718341544242944266781, 6240424741484609266392009977454864, 75104938249367345681206971604866080, 32264483340980969722020637386275054, 48379486424936974614387887472243260, 75104938249367345681206971604866080, 7485157899144949411682111055590430, 92712108866793232034695893485547544, 7485157899144949411682111055590430, 83599752542227961885740894770768516, 48379486424936974614387887472243260, 54751499983812600001595164999947606, 7485157899144949411682111055590430, 15496388930720047282261773301643045, 8400749730877624158255771399988559, 58137259942365444979479997549034855, 48379486424936974614387887472243260, 88077383691706059347171006086863620, 6240424741484609266392009977454864, 48379486424936974614387887472243260, 7934151132541799341665122998944580, 73075186383278314052649120872243371, 7934151132541799341665122998944580, 102463675364526450047988025312160540, 7485157899144949411682111055590430, 48379486424936974614387887472243260, 73075186383278314052649120872243371, 7485157899144949411682111055590430, 110209866655316842092627871164477875]

x = 6969696969
n_dict = {}
pt = []
for char in string.printable:
    n_dict[functor_simplified(ord(char)*6969696969)] = char
for char in output:
    pt.append(n_dict[char])
print(''.join(pt))
```

Running the code above produces the flag.

Flag: `cybergrabs{50m3_func710nS_n3v3r_c3A5e_t0_4m4z3_m3}`