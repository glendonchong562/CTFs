# Side Channel

## There's something fishy about this PIN-code checker, can you figure out the PIN and get the flag?

For this challenge, we are given a [pin-checker](./pin_checker) that checks for a 8 digit pin and grants us the flag if the correct pin is supplied. Given the hint from the challenge description that this was a *side channel attack*, I figured that inputting the right digit would likely result in a difference in processing time as compared to the wrong digit.

It took awhile for me to figure out that each digit of the pin is checked sequentially, meaning that the **2nd** digit would not even be checked if the **1st** digit was wrong. I then spun up this script that would measure the time it took for each run with a different digit to see the outlier (*longer processing time since it is also checking for next digit*) which would indicate the correct digit. I'm sure there is some way to automate this (based off finding the average of the times and taking the digit that yields a timing greatly above average?) but there were only 8 digits and so I just did it manually digit by digit, adding each correct digit to the variable *correct* after obtaining it.

```python
from pwn import * 
import time

correct = b'4' 
# Digits will be added here after identifying each correct one
zeros = b'0' * (7-len(correct))
exe = './pin_checker'
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'warning'

for i in range(10):
    start = time.time()
    r = process(exe)
    r.sendlineafter(b'\n', correct + str(i).encode('utf-8') + zeros)
    r.recvall()
    end = time.time()
    duration = end - start
    print(f"{duration=} for {i=}")
    r.close()
```

As an example, here we see that the second digit is **8**, given that the time taken is nearly double that of the rest of the digits:

![Capture](https://user-images.githubusercontent.com/71312079/164131050-c1163499-f127-47c9-b2f6-6aca30274db6.PNG)

After obtaining the correct pin on my local machine, I connected to the server instance and inputted the right pin to obtain the flag:

FLAG: `picoCTF{t1m1ng_4tt4ck_9803bd25}`
