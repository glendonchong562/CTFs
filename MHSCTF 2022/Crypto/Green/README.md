# Green (30 Points)

## Challenge Description: I'm green da ba dee da ba dah

We are given a single png file that I named [green.png](./green.png). Opening it I see a very long and thin strip of green as seen below:

![green](https://user-images.githubusercontent.com/71312079/155543379-f0c6101b-9c2e-45c0-bf6e-466a11f916a8.png)

I run the usual suite of image tools (*binwalk/stegoveritas/zsteg/etc.*) but nothing notable pops up. At first I thought it could be morse code since I saw patches of black in some of the images produced by stegoveritas but decided that they looked to be too random and irregular to be interpreted as morse code.

I had a little help from my teamate on this challenge, who suggested that the challenge name **green** was a clue that I should only look at the green values of the image. I then created a python script to extract only the green values from each pixel and concatenate them into an array

```python
from PIL import Image

green = Image.open("green.png")
width, height = green.size
pixels = green.convert("RGB")

g = []
for k in range(height):
    for i in range(width):   
        g.append(pixels.getpixel((i,k))[1]) # Only green value
print(''.join([chr(i) for i in g]))
```

Running the code above produced what looked like base32 output. 

```
JJFEMRKNKJFU4S2KIZKTIUZSJNEVUTCGJNKVUU2KJZCVMVKSINDEWNKLKZKVKMSLJJNEIRKLKZFVKSKOIRCVGVCTJRFVUS2WJNGVGTCKJJDEKSKWJNGEWWSGKZCVEMSLJJJEGVSPKZBVISSWIVLE2USDK5EVMSKUIVKEGS2KJJCEKS2TJNLUUTSHIVLVOU2HJNNEKVSFJVJUYSSGJJCUOVSTJRFVESSVLFJVGV2JKZGEKMSVKNCEWNKGIVGVGS2VJFLEWRKXKMZEWSSKINCUWUZSKRFE4TCVKVKFGSCJKZGFMS2VGJEEUTSOIVDVMU2GJJLEUVKZKNJUOSSKINKU6VSTJNFTKRSWKNLVGR2KIZFFMR2VGJFEWWSHIVGVGMSWJNHEGRKXJZFUOSKWI5LEOUZSKZFEMTCFKVLEWWCLJZFFKUKTGIZESUSLKVLVKWSTJNHEIVKVKNJVMSZVJNDEOU2LJJFVUR2GJVJDEVSHJJCUKVKUKNHUSVSKKZGVKMSJJJHEOVSVKJJUES2OJJKU6U2TKNEU4S2VGZLFGVCLKJDEMRKSKNLUUVSKKZDVMMSLJFNEMRSNKIZE4S2OIZCVOV2TJBEVMRSWI5GVGV2KJZEEKR2SJNMEUWSGKVGVGMRSJE2UYRKPKZFFGS22IZCU2VCDIZFVMTCFK5LUGTCKKZHEKS2WJNKUSTSGKVJVGU2NJFKVURSNKEZE2SSNGJKU2USKKVFU4SSWJVJTEV2KJZCEKT2VLJJUUSSGKZKVEMSHJJLEURCFKZJUQSSKIVKUWVSLKNFU4SCVKNLFGS2LLJDVMS2NKNFEUSSIIVLVMU2WJNFEMVSBKMZE6SK2IRCTEVJSKRDUURKVGRKEGRSKGVGEMR2WINFEUWSEIZFU4Q2TJNHEYRKTKZJUWSK2IRLEKUZSJRFEUTSFJVJFGTCLJFNEMT2TGJHUSVSLKZHVMU2LJNJEKVSVKJFVMR2KJNKEKVKTJNFEUQ2WJFJEWV2KJZFEKV2XKNDUSUSGKZDVCMSXJE2U4RKXKJBUMS2WIJKVOURSKZEFKNSUGJIEUNKIKU6T2PJ5HU6Q
```

The flag was eventually revealed after **8** rounds of base32 decoding:

![flag - 8 rounds base32](https://user-images.githubusercontent.com/71312079/155543399-7c9029de-2dca-4f19-b4ea-352ca5bc982f.png)

```Flag:flag{d075_4nd_d0ts}