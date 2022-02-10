# Simple (150 points)

## Challenge Description: We just shifted to a new home...

We are given a file called **simple**. Running it gives me the following prompt: 

![simple](https://user-images.githubusercontent.com/71312079/153351323-de1066f0-e0cf-4d77-bf19-fe5faeda06eb.png)

Dissembling the file in IDA, I see that the function *sub_1188* is called by the *main* function.

![ida_main](https://user-images.githubusercontent.com/71312079/153351316-b72576a1-de50-4c13-b2e9-95d1208bdf6c.png)

Stepping into function *sub_1188*, I see that there is a string copy of `"QllB^pvCloQebCfopqCi^d"` into the variable *v5*. Every character in *v5* is subsequently compared to every character in our input *a2*, checking if the byte value of our input is **3** greater than that of *v5*. I also see the output we received: ``Cope Harder!`` all the way at the bottom as we did not pass any arguments to **simple**.


![ida_function](https://user-images.githubusercontent.com/71312079/153351327-bce5cefd-4bf5-475b-bd79-37e127cd684b.png)

As such, I create a python script to increment every character in the supplied string by **3** and print the result.

```python
a = "QllB^pvCloQebCfopqCi^d"
ls = []
for char in a:
    ls.append(chr(ord(char) + 3))

print(''.join(ls))
```
Running the code above produced the flag:
![flag](https://user-images.githubusercontent.com/71312079/153351324-d1c0a277-ea07-47a0-b8ff-2cb58be4e0c6.png)

Running the file again with ```./simple TooEasyForTheFirstFlag``` produced the prompt: ```BINGO!```

FLAG: ```cybergrabs{TooEasyForTheFirstFlag}```

