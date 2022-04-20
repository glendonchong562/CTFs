# Keygenme

## Can you get the flag?

For this challenge, we are given a binary called [keygenme](./keygenme). Upon opening the binary, we are greeted with a prompt for the license key: 

![license_key](https://user-images.githubusercontent.com/71312079/164142376-e2d9e4af-cead-4fdf-9dda-2cc53dea1e26.PNG)

Running strings on the binary, I thought I obtained the flag, but it turned out to only be half of the flag :( 

![half_flag](https://user-images.githubusercontent.com/71312079/164142388-b304a112-e69b-4e9f-bef4-a146c9bb13b4.png)

Suspecting that some form of debugging may be needed to obtain the flag, I open the flag in **radare2** and locate the function that checks for the key, noticing that the function also calculates the MD5 hash of the input license key.

I first see all the functions using the commands *aaa* and *afl*. 

![main](https://user-images.githubusercontent.com/71312079/164142380-560f431b-c22f-4b0a-8b6d-0c9fe79aef22.png)
I next set a breakpoint with *db main* and then *dc* to continue to the breakpoint. Moving to the *disassembly* view, I see that there is a function at address *0x55f0cb043209* that will be called to compare the key, adjusting the **al** register which would subsequently be used to return either a **key valid/key invalid** string. I then set a breakpoint at this function and proceed to step into it.

![disassembly](https://user-images.githubusercontent.com/71312079/164144933-a53c9044-efd1-4caa-bb90-c45388a1eef9.PNG)

After stepping through the function, I noted that half the correct key was printed, and stepping through more subsequently printed out the entire key on the stack:

- NOTE: I increased the stack size to **256** using the command *e
  stack.size = 256* to see more of the stack to allow for an easier display

![flag](https://user-images.githubusercontent.com/71312079/164142385-0064937f-57c5-40de-af39-486148fb457c.png)

FLAG: `picoCTF{br1ng_y0ur_0wn_k3y_9d74d90d}`
