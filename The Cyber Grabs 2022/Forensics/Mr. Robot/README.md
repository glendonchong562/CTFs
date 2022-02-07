# Mr. Robot (200 points)

## Challenge Description: Mr. Robot most famous TV show but least people know about it.


This challenge involves a wav file called [chall.wav](chall.wav). I don't really do alot of audio stego challenges so I did some google searching and stumbled upong this useful [github](https://github.com/x41x41x41/hackingpotato/blob/master/techniques/stenography.md) page about solving image/sound stego problems. I followed the sequence of steps: 

1. **Listen to file** - Just a robotic voice saying what I think were some quotes from the TV series 
2. **strings** - No strings of interest 
3. **binwalk** - No embedded data 
4. **Check Metadata** - Nothing interesting using *exiftool*
5. **Check LSB** - I was initally unsure how to do this so I skipped this 
6. **Check for multiple channels** - Single channel based on *exiftool*
7. **Open in Audacity and check spectogram** - I used *Sonic Visualiser* but did not note anything interesting in the spectrogram 
8. **Slow down file** - No additional findings 
9. **Analyze waveform to see if it's binary** - Definitely non binary waveform

*Waveform snippet*
![Waveform](https://user-images.githubusercontent.com/71312079/152735832-725f4e0b-48c0-41d8-9572-3146bdd81657.png)

It turned out that **Step 5: Check LSB** was the intended solution and actually did not require too much work. After doing a bit of googling I stumbled upon a tool called [WavSteg](https://github.com/ragibson/Steganography#LSBSteg) that can recover a file from the least significant bytes of the file. I ran the following command to recover 50 LSBs and obtained the flag:

```bash
stegolsb wavsteg -r -i chall.wav -o output.txt -b 50
```

Flag: `CYBERGRABS{3VERY_8YTE_4RE_REAL_VALUE}`