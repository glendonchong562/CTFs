# Tips

1. Always use ROP chains for simplicity 
 * No need to worry about adding fake return address for 32-bit with arguments 

2. RIP will NOT even be populated for an invalid memory address 
 * Different from 32-bit where you can see the overwritten EIP
 * Thus need to look at RSP instead of RIP 

## GEF 

1. Finding offset:
 * 32-bit 
	* Pattern create 100
	* Look at overwritten value of EIP 
	* Pattern search EIP value
	* NOTE: Be mindful of endianess 
* 64-bit 
	* Pattern create 100
	* Pattern search $rsp 
	
2. Inputting non-printable characters:
 * python2 -c 'print "A"* offset + desired_func_addr + any_return_addr + args (if any)' > payload
	* NOTE: 'any_return_addr' ONLY for 32-bit, ignore for 64-bit
 * r < payload 

3. Toggle breakpoints at the "ret" part before the vulnerable function returns 
 * break *<address of ret> 