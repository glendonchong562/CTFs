# Significant Other (30 Points)

## Challenge Description: Someone sent me this song, but I don't know why! Maybe they're trying to tell me something?


We are given a file that I renamed to [significant.wav](./significant.wav). This challenge took quite awhile to solve as I was unable to obtain any results after performing all the steps that I detailed in a previous [writeup](../../../Cyber%20Grabs%20CTF%202022/Forensics/Mr.%20Robot/README.md) I did involving wav files. 

I knew that the challenge was probably related to the LSB due to the challenge name. However, *stegolsb wavsteg* that I used previously seemed to give me gibberish output. At one point in time I thought I needed to obtain the MSB instead of LSB for the wav but that also didn't produce any meaningful output.

In the end, I looked for another method of extracting the LSB and came across this [article](https://sumit-arora.medium.com/audio-steganography-the-art-of-hiding-secrets-within-earshot-part-2-of-2-c76b1be719b3) that provides some python code to produce the LSB. I copied over the following code and ran it and I obtained the flag! 

```python
# Use wave package (native to Python) for reading the received audio file
import wave
song = wave.open("significant.wav", mode='rb')
# Convert audio to byte array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# Extract the LSB of each byte
extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
# Convert byte array back to string
string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
# Cut off at the filler characters
decoded = string.split("###")[0]

print(decoded[:50])
```

```Flag: flag{ilY_<3}```
