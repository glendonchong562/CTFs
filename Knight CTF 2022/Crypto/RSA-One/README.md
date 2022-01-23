# RSA-One (100 Points)

We are given the ciphertext file containing the flag (**flag.enc**) and private key file (**private.pem**).

However, of one of the bytes of the private key file was misplaced and denoted by a ❌.

![pkey](https://user-images.githubusercontent.com/71312079/150670224-d7159966-19a1-46d8-898a-92f8cb5bf885.png)


To properly decrypt the file, we need to replace the ❌ with the correct character, of which there are only 64 possible characters (since it is encoded in base64). 

The following python script was used to obtain the correct character and decrypt the flag.

```python
from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import string

ct = open('flag.enc','rb').read()

wrong_byte = bytes("❌",'utf-8')

privateKey = open('private.pem','rb').read()
index = privateKey.find(wrong_byte)
first = privateKey[:index]
second = privateKey[index + len(wrong_byte):]

possibilities = string.ascii_letters + string.digits + "+/="
for i in possibilities:
    try:
        Key = RSA.importKey(first + bytes(i,'utf-8') + second)
        ct = bytes_to_long(ct)
        decrypted = pow(ct, Key.d, Key.n)
        print(long_to_bytes(decrypted))
    except Exception as e:
        print(f" {e} for character \"{i}\"")
        continue

```
Output: 

![flag](https://user-images.githubusercontent.com/71312079/150670219-fb8bb81e-51fc-46c0-b95e-d02597a5c686.png)


FLAG: KCTF{M4Y_TH3_8RUT3F0rc3_B3_W1TH_Y0U}