# ahh shit! (250 points)

## Challenge Description: Where are we going?

This challenge was so simple that I'm surprised it was worth 250 points. I opened the file **ahh_shit** in IDA and instantly saw the flag in the main function:

![ida](https://user-images.githubusercontent.com/71312079/153383022-fe0b8bdf-c3b9-4e44-822d-c5a1247306de.png)


In ghidra, it would have taken some effort to convert the bytes into chars as ghidra does not recognise arrays:

![ghidra](https://user-images.githubusercontent.com/71312079/153383018-b6491d7e-4f0c-4d08-a893-0046046d6e7b.png)


Alternatively, I can also obtain the flag if I listen on port 9999 with `nc -lvp 9999` and then run the file:

**run file**
![run_file](https://user-images.githubusercontent.com/71312079/153383007-c751d9c3-ce1a-4240-8311-45369587a921.png)


**nc listener**

![nc_receiver](https://user-images.githubusercontent.com/71312079/153383025-80178745-4334-40c8-87c9-e5eb87c328bf.png)


FLAG: `cybergrabs{h3r3_w3_g0_4g4in}`

