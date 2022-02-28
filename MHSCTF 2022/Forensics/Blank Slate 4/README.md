# Blank Slate 4 (30 Points)

## Challenge Description: There's something seriously wrong with my friend. They keep sending me these blank files! I hate to keep pestering you, but can you figure out what this one says?

We are given a file that I renamed [blank.txt](./blank.txt). Opening the file, I see that it has a size of **1kb** although it appears to be blank in my text editor. Wanting to obtain more information on the file, I run the **file** command on it and receive this output: 

```blank.txt: UTF-8 Unicode (with BOM) text, with no line terminators```

Hmm, I've never really handled UTF-8 Unicode (with BOM) files before so I do some research on it and found the following:
* BOM files have an extra 3 bytes of **EF BB BF** at the beginning to signify that it is a UTF-8 file
* UTF-8 has *variable width character encoding*, meaning that each character can be between **1-4** bytes

I then open the file in *Hxd64* and see the following: 

![hxd](https://user-images.githubusercontent.com/71312079/155555099-18442a63-d2ec-45ef-a3ca-cedfb216de68.png)

Looking at the hex view, I see that there seems to only be 2 different types of characters present:
* E2 80 8B
* 20

This would likely signify binary encoding and so I decided to modify the bytes and see if they could be decoded to give me a proper result.

The following steps were then performed with the file to obtain the flag : 
1. Removed the bytes **EF BB BF** at the beginning 
2. Replaced the bytes **E2 80 8B** with **30**
   * 30 = Dec value for '0'
3. Replaced the bytes **20** with **31**
   * 31 = Dec value for '1'
4. Took the output binary values and decoded them in cyberchef 

![flag](https://user-images.githubusercontent.com/71312079/155554220-f24001a1-136c-4284-abdc-01d84e7b736b.png)

```Flag: flag{still_n0t_blank}```
