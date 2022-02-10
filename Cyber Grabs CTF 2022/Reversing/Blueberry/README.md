# Blueberry (250 points)

## Challenge Description: Welcome to the bluebakery new baker. Mr. Bluepher has left you a message. Now get back to work.

NOTE: I did not manage to solve this challenge on my own and had help from a team mate. This challenge was interesting as it involves patching the binary and so I wrote it here for documentation.

I am given a file called **blueberry**. Running the file produces no visible output in the terminal. 

![unpatched](https://user-images.githubusercontent.com/71312079/153428159-eba84a2b-a78a-490f-8a84-9db8cfc23afa.png)

I open the file in IDA and see the disassembled code. 

![main](https://user-images.githubusercontent.com/71312079/153425492-d096ffbf-f0ba-4381-b609-507ade14f62f.png)

I did not at first notice the *os_Exit* function, and I went down a rabbit hole trying to find the the value of the variables and stepping into the *main_bakery* function to try to make sense of it as well. After fruitless exploration of the various functions, I returned to *os_Exit* and clicked it to see its text view.

![original](https://user-images.githubusercontent.com/71312079/153425504-0198357e-f3e0-436e-94f7-1c5401a66a95.png)

In order to completely avoid this function and move on to the rest of the code, *nop* instructions would need to replace this function call. I thus replaced the **5** bytes of call instruction with **90** (nop).

![patched](https://user-images.githubusercontent.com/71312079/153425507-b21f84d5-4a16-4ebc-aeb4-5d5073d535a3.png)

Saving this patched binary to a new file, I ran the file again and obtained the flag:

![blueberry_patched](https://user-images.githubusercontent.com/71312079/153425512-5fd68990-aff8-4381-8ce5-fc6cb38a37a8.png)

FLAG: `cybergrabs{b4K3_m3_s0mE_CuPc4k3}`


## Learning Points (Mainly on navigating in IDA):
* Opcodes not shown by default
  * Options -> General -> Number of opcode bytes (non-graph) -> **6**
* Patching the binary
  * Edit -> Patch Program -> Change byte
* Saving patched binary
  * Edit -> Patch Program -> Apply patches to input file
  * Save a backup of the original file in case the patched file doesn't work! 

