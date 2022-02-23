# raw-image (medium)

## My friend messed up decrypting this image. Can you do it properly?

Steps:

1. Checked what time of file it was and saw that it was a `openssl enc'd data with salted password `
2. Opened the file in a hex editor and saw that there were repeating sequences of 16 bytes 
   * Wrote a script in python to see the frequency of the bytes 
```python
import collections

c = collections.Counter()
file = open('raw-image.bin','rb').read().strip()
file = [file[i:i+16] for i in range(0,len(file),16)]
c.update(file)

for Bytes, count in c.most_common(15):
    print(f"{count=} for {Bytes=}")
```
*Output*
![repeating_bytes](https://user-images.githubusercontent.com/71312079/154063590-80e8287a-3f66-4e3e-b2ed-0c19a1c3d8a2.png)

3. Guessed that it was ECB coloring 
   * Originally thought I needed to brute force the password and the salt but decided against it as it would take too long
4. Used this ECB coloring [tool](https://github.com/doegox/ElectronicColoringBook) on the binary file 
   * Click [here](https://doegox.github.io/ElectronicColoringBook/) for more information on the tool and its usage
5. Used the following parameters for *ElectronicColoringBook.py*
   * *pixelwidth=4* because the default value of *1* made the image look long and distorted
   * *-f* flips the image 
```bash
python ElectronicColoringBook.py raw-image.bin --pixelwidth=4 -f
```
![flag](https://user-images.githubusercontent.com/71312079/153878055-732af436-210f-4a26-9b01-50fa77066bb4.png)


FLAG: ```CTF{c589616e64bb57abab4e68d96cb015c442f5a3e14c0c0f27f7ef1892f17bff75}```