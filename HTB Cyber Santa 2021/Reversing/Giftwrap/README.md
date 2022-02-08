# Giftwrap (Day 2)

We are given a single file called **giftwrap**

Running **giftwrap** produces this prompt:

![giftwrap](https://user-images.githubusercontent.com/71312079/150803991-0613458f-1e99-4e58-a038-997c45a44315.png)

It seems like we need to input the correct magic word to obtain the flag. Opening the file in IDA and decompiling it gives us this view:

![ida_decompiled](https://user-images.githubusercontent.com/71312079/150803834-40ea024d-f63c-4145-bdb1-766f58d22310.png)

From the decompiled view, we see that there are 2 operations at play: 
1. An XOR operation with **0xF3**
2. A compare operation of **23** bytes starting at the memory location of **CHECK**

Navigating to the address of **CHECK**, we are able to see the actual bytes that will be compared against in operation 2.

![CHECK](https://user-images.githubusercontent.com/71312079/150803816-aced7761-4afd-4dfc-8597-2c9bf8922141.png)

The bytes were then extracted and XORed to reverse operation 1. 

```python
CHECK = [0xBB,0xA7,0xB1,0x88,0x86,0x83,0x8B,0xAC,0xC7,0xC2,0x9D,0x87,0xAC,0xC6,0xC3,0xAC,0x9B,0xC7,0x81,0x97,0xD2,0xD2,0x8E]

flag = []
for i in range(len(CHECK)):
 	flag.append(chr(CHECK[i] ^ 0xF3))
print(''.join(flag))
```
Running the code above produced the flag:

FLAG: HTB{upx_41nt_50_h4rd!!}
