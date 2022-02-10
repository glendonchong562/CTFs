# Custom Cipher (150 points)

## Challenge Description: Do you have key to decrpyt this?

Finally a challenge that was not an ELF file :) This challenge involves a file called **script.pyc**. 

I first ran the file in python and received the following error: `RuntimeError: Bad magic number in .pyc file`. Realising that my python version was probably wrong (I was using **python 3.8**), I ran `file` on the file and noted that it was compiled with **python 2.7**.

![file](https://user-images.githubusercontent.com/71312079/153372587-000c31eb-65d1-4b51-a125-04927efc1439.png)


I then run the file with python2 and receive a prompt for text to encrypt:

![run](https://user-images.githubusercontent.com/71312079/153372603-63f9a667-2e04-424c-ae4b-605e35ffb6cb.png)

Given that the file contains bytecode and few readable characters, I did  a google search on the best way to decompile *pyc* files to its original python file. I found [uncompyle6](https://pypi.org/project/uncompyle6/) and successfully decompiled the file to produce the following python code: 

```python
encoded_flag = '*@),9.9():B@tz&k6<5i&\\mX&xmn-y&*Vu/,wD'
alphabet = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

def encode_secret(secret):
    rotate_const = 37
    encoded = ''
    for c in secret:
        index = alphabet.find(c)
        original_index = (index + rotate_const) % len(alphabet)
        encoded = encoded + alphabet[original_index]

    return encoded

text = raw_input('Enter any text to encrypt: ')
if encoded_flag == encode_secret(text):
    print 'Congratulations!!!. You found the flag.'
else:
    print 'Sorry!!!'
```
This code is alot more manageable and human-readable and I created a script to reverse the encoding and obtain the flag:

```python
encoded_flag = '*@),9.9():B@tz&k6<5i&\\mX&xmn-y&*Vu/,wD'
alphabet = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

def decode_secret(flag):
    rotate_const = 37
    decoded = ''
    for c in flag:
        index = alphabet.find(c)
        if index < rotate_const:
            original_index = len(alphabet) + index - rotate_const
        else:
            original_index = index - rotate_const
        decoded = decoded + alphabet[original_index]

    return decoded

print(decode_secret(encoded_flag))
```
Running the script produced the flag.

FLAG: `cybergrabs{yOU_FounD_7H3_SHIfT_c1PheR}`
