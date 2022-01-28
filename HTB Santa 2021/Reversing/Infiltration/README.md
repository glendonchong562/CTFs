# Infiltration (Day 1)

For this challenge we are given a single file called **client**, which is a 64-bit ELF file.

![file](https://user-images.githubusercontent.com/71312079/151476809-f657bef0-b3b9-4bec-b904-de377b1b9111.png)

Running the file produced the following prompt:
![client](https://user-images.githubusercontent.com/71312079/151476511-d71d57ad-d6b3-4d28-840f-54cc64ed8d86.png)


I performed the following steps:
* Decompiled the file in *ghidra* but could not find any functions of interest other than a socket connection to the remote server
* Ran *strings* on the file but no noteworthy strings that could be related to the flag

At this point I realised that I had not yet supplied an *IP address* and a *port* , but running **client** with the docker IP and port that I was given didn't seem to return any result...

Being new to reversing challenges, I was almost about the give up when I realised that I had not attempted the low hanging fruits - tracing system & DLL calls with **strace** and **ltrace**. I ran the following command and saw that the flag had been leaked:
 ```bash
strace ./client 178.129.34.54 38712
```

![strace](https://user-images.githubusercontent.com/71312079/151475264-dd6771f5-35a9-4ba2-84c0-bbab12888094.png)

Flag: `HTB{n0t_qu1t3_s0_0p4qu3}`
