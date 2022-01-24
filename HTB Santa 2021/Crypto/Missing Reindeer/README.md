# Missing Reindeer (Day 3)

We are given an email message (*message.enc*) that contains a public key as well as the encrypted ciphertext.

```
-----BEGIN PUBLIC KEY-----
MIIBIDANBgkqhkiG9w0BAQEFAAOCAQ0AMIIBCAKCAQEA5iOXKISx9NcivdXuW+uE
y4R2DC7Q/6/ZPNYDD7INeTCQO9FzHcdMlUojB1MD39cbiFzWbphb91ntF6mF9+fY
N8hXvTGhR9dNomFJKFj6X8+4kjCHjvT//P+S/CkpiTJkVK+1G7erJT/v1bNXv4Om
OfFTIEr8Vijz4CAixpSdwjyxnS/WObbVmHrDMqAd0jtDemd3u5Z/gOUi6UHl+XIW
Cu1Vbbc5ORmAZCKuGn3JsZmW/beykUFHLWgD3/QqcT21esB4/KSNGmhhQj3joS7Z
z6+4MeXWm5LXGWPQIyKMJhLqM0plLEYSH1BdG1pVEiTGn8gjnP4Qk95oCV9xUxWW
ZwIBAw==
-----END PUBLIC KEY-----
```

The public key is then imported into python to determine the e and n values. After noticing that the value for e was **3**, I thought of the *Cube Root Attack* where the modulus was greater than the plaintext raised to the power of 3. As such, the modulus had no effect and the ciphertext could simply be cube rooted to obtain the plaintext. I obtained the cube root code from this [writeup](https://secgroup.dais.unive.it/teaching/cryptography/challenges-201415/challenge-weak-rsa/).


```python
import base64
from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse,long_to_bytes, bytes_to_long
def root3rd(x):
    y, y1 = None, 2
    while y!=y1:
        y = y1
        y3 = y**3
        d = (2*y3+x)
        y1 = (y*(y3+2*x)+d//2)//d
    return y

key_encoded=
'''-----BEGIN PUBLIC KEY-----
MIIBIDANBgkqhkiG9w0BAQEFAAOCAQ0AMIIBCAKCAQEA5iOXKISx9NcivdXuW+uE
y4R2DC7Q/6/ZPNYDD7INeTCQO9FzHcdMlUojB1MD39cbiFzWbphb91ntF6mF9+fY
N8hXvTGhR9dNomFJKFj6X8+4kjCHjvT//P+S/CkpiTJkVK+1G7erJT/v1bNXv4Om
OfFTIEr8Vijz4CAixpSdwjyxnS/WObbVmHrDMqAd0jtDemd3u5Z/gOUi6UHl+XIW
Cu1Vbbc5ORmAZCKuGn3JsZmW/beykUFHLWgD3/QqcT21esB4/KSNGmhhQj3joS7Z
z6+4MeXWm5LXGWPQIyKMJhLqM0plLEYSH1BdG1pVEiTGn8gjnP4Qk95oCV9xUxWW
ZwIBAw==
-----END PUBLIC KEY-----'''

pubkey = RSA.importKey(key_encoded)
n = pubkey.n
e = pubkey.e
# e = 3

c1= bytes_to_long(base64.b64decode(open('message.enc').read()))
m1 = root3rd(c1)
print(long_to_bytes(m1))
```

Running the code above produced the decrypted email message, along with the flag.

Flag: HTB{w34k_3xp0n3n7_ffc896}