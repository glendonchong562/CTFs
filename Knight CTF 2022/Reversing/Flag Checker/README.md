# Flag Checker (100 points)

We are given a file called "**flag checker**"

Running it shows that the file merely tells us if the inputed flag is the correct or wrong fla.

![flag_checker](https://user-images.githubusercontent.com/71312079/150683408-1aca54fc-6ba8-4a11-9212-328266be504a.png)

I originally decompiled the code in ghidra, but the decompiled view was more difficult to read as compared to the view from IDA. I think it's because unlike IDA, ghidra has no concept of the array data structure hence the more confusing decompiled code.

Ghidra:


![ghidra_smaller](https://user-images.githubusercontent.com/71312079/150683412-3b4788ba-b1c0-40bf-90f1-629f7188e29e.png)

IDA:


![ida_disassembled](https://user-images.githubusercontent.com/71312079/150684030-3ec9721c-6071-4ee5-86cd-4ba72084ef4a.png)


After looking through the decompiled C code in IDA, I was initially puzzled about the negative numbers as I thought that the range of char was 0 - 256. However, this [link](https://www.quora.com/How-do-I-store-a-negative-integer-value-using-char-data-type#:~:text=Yes.,be%20assigned%20to%20char%20variables) answered my questions about storing and performing arthimetic operations with negative integer data. Basically, *deducting 1 from -128 will produce 127 and vice versa for addition*.

Given the difficulty in reversing the arthmetic operations to obtain the original characters, I used a dictionary to map each ascii printable character to its output after performing the same steps in the code.

```python
a = bytes("08'5[Z'Y:H3?X2K3V)?D2G3?H,N6?G$R(G]",'utf-8')

mappings = {}
sol = ''

def wraparound(number):
    if number < -128:
        return 128 - (-128 - number)
    else:
        return number
    
#printable ascii range 
for i in range(32,128):
    if i <= 64 or i > 90:
        if i <= 96 or i > 122:
             org  = i
        else:
            org = -37 - i
    else:
        org = -101 - i
    
    mappings[wraparound(org - 32)] = i
        
print(mappings)

         
for i in a:
    sol += (chr(mappings[i]))

print(sol)
```

Running the code above yielded the flag:

KCTF{aTbAsH_cIpHeR_wItH_sOmE_tWiSt}
