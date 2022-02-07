# Super Secret Storage (1000 points)

## Challenge Description: Do you know Windows have a every secret storage location to have important message, but all of us uses it daily.


**NOTE**: While I spent ~5 hours doing the challenge, I was very close to solving it but ultimately did not solve it during the challenge. It was definitely very frustrating but am glad that I learnt alot in the end.

I am given a memory dump simply called **memory.raw**. My DFIR instincts prompted me immeditately to run [winsupermem](https://github.com/CrowdStrike/SuperMem) on it, a CrowdStrike utility that can automatically run:
1. Multiple volatility plugins
2. Bulk Extractor 
3. Strings 
4. Plaso 
5. Yara
6. EVTxtract 

I chose a triage type of *1* as I felt like only the first 3 options would be relevant for this challenge. After obtaining the results in ~9 minutes, I checked the usual suspects:
* Vol3: **pstree/pslist/cmdline/handles/userassist**
* Bulk Extractor: **url/domains/enmail/ip/pii**
* Strings: Tried the low hanging fruit of the flag format `CYBERGRABS{` to no avail. Moved on as there were too many strings and I didn't have a specific one in mind

I went back to the challegenge description as pondered over the last part: *all of us use it daily*. Could it be possibly the registry? I then unsuccessfully tried to enumerate autorun keys like *Run/RunOnce/Services*. I even tried dumping registry hives and browsing them but to no avail.

Moving on, I realised that I should have run a triage type of *2* for *winsupermem*, as it would also process volatility 2 plugins that are not available in volatility 3. I first checked *imageinfo* and saw that the image profile is *Win7SP1x64*. Eventually one volatility 2 plugin (*clipboard*) produced a helpful finding: 

![clipboard](https://user-images.githubusercontent.com/71312079/152719085-7826683f-8d90-424f-b583-5316e1f2cab6.png)

I extracted the data `Ls>#aQb$rjLQ{J+Gh<RkbYF9HFj7HBGkp` and this was when I hit another wall. I inputted the data into cyberchef and thought I tried every possible decoding method, even yielding an unexpected output in Chinese that I translated to English but it turns out it wasn't related to the challenge. [After checking with the challenge setter]


![Text Encoding Brute Force - CyberChef](https://user-images.githubusercontent.com/71312079/152720145-90037750-c22a-4dd9-89c5-5712cd434e83.png)

![translate - Google Search](https://user-images.githubusercontent.com/71312079/152720148-70e0e0f9-c9a6-4ed1-b0ba-012081e1c582.png)

A couple of hours into the challenge, a hint was released: *SGF2ZSB5b3UgY2hlY2tlZCBTY3JlZW5zaG90Pw==* . Decoding it from base64, I get the plaintext: `Have you checked Screenshot?` 

Hmm, I actually did check the *screenshot* plugin in volatility 2 and found a couple of mostly empty screenshots except for one: 

![session_1 WinSta0 Default](https://user-images.githubusercontent.com/71312079/152720440-f0856eef-b580-483a-aaaf-ec01df86db1e.png)

I didn't think too much of the screenshot and went down a couple of other rabbit holes:
* Thought that the clipboard data was encrypted with DPAPI and tried unsuccessfully to decrypt it 
* Thought that the encoding was *CBOR* due to the following output I received:

![cbor](https://user-images.githubusercontent.com/71312079/152720900-4178fa4c-04c7-4a28-9efa-312a79e3a4c6.png)
* Tried every cipher method I could think of (Substitution/Rail/Fence/etc.)
* Did a procdump of *notepad.exe* and *StikyNot.exe* to look at its strings and even executed it

At this stage I was at my wits' ends and I gave up. After the competition was over, I read the discord disucssions and discovered the following:
* I should have used memdump instead of procdump for the 2 processes
* Opening the raw process data in **GIMP** and adjusting the width and height would have yielded 2 more clues:

**Notepad.dmp - Clue: 'I always Love IPv6'**
![Notepad_in_GIMP](https://user-images.githubusercontent.com/71312079/152722218-276d4fd8-f666-4cd6-ba1b-55c6405c1e28.png)

**StikyNot.dmp - Clue: 'That's something which is Secret'**
![StikyNot_in_GIMP](https://user-images.githubusercontent.com/71312079/152722221-9d105984-2208-4b1b-8f5a-983f5f855ac3.png)

* The actual decoding was **base85** with the **ipv6** alphabet

![From Base85 - CyberChef](https://user-images.githubusercontent.com/71312079/152721887-97f2a465-8384-4861-bf73-c3818e6bafe4.png)




Flag: `CYBERGRABS{53cREt_st0RAG3}`

Learning Points:
1. Check for different alphabets when decoding (I saw that the default alphabet for base85 said it was not a valid array and I moved on)
2. How to use **GIMP** to analyse bitmaps from raw process data
3. Not to overthink challenges and look at simple solutions


