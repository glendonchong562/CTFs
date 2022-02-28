NOTE: There wasn't a single forensics challenge but multiple sub-challenges all arising from the same E01 image.

## MD5 & SHA1 Checksum

This involves opening the image in FTK imager and looking at the *properties* window to see the verification hashes.

![hash](https://user-images.githubusercontent.com/71312079/155440834-0dd69b62-69c1-4903-8e47-77e7b4b72f4f.png)


## Identification: 

NOTE: All the information can be found in the various registry hives (**C:\Windows\System32\Config**)

### Timezone

The timezone information can be found in the same location in the *SYSTEM* hive in the following subkey:

**HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation**

![timezone](https://user-images.githubusercontent.com/71312079/155442062-0ad861c8-71d6-492f-85e1-945c5e17a529.png)

### Login Count

Information on the activity of each user account is found in the *SAM* hive. I used *regripper* to extract key information from the hive to obtain the user with the highest login count.

![logons](https://user-images.githubusercontent.com/71312079/155442088-3eca7671-a632-4e51-b3b5-75fa63d9ffb0.png)

### OS & Registered Owner & Organisation of OS

All 3 pieces of information can be found in the same location in the *SOFTWARE* hive in the following subkey: **HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion**

![OS](https://user-images.githubusercontent.com/71312079/155440995-de11c657-7139-437b-a0ae-95e80d35ba7a.png)

## Manual Analysis: Password



## Analysis: Files

In order to find the credit card skimming related file with a creation date of *2022-01-29 22:22:02* , I used **MFTECmd** by Eric Zimmerman to parse the *$MFT* file found in the root directory into a csv file. I then used **Timeline Explorer** to open the large csv file and filter to the date and time in question to obtain the desired file: ```Devices.odt```: 

![file analysis](https://user-images.githubusercontent.com/71312079/155448120-5727df38-d35d-435c-abef-7ad34d0b1824.png)

## Deleted Information: File Name

For deleted files, we need to look at the *$RecycleBin* folder in the NTDS root directory. Browsing through the various user accounts, I am able to find the name of the deleted file: 

![name](https://user-images.githubusercontent.com/71312079/155443052-795a320c-5961-445b-bfc8-3d837e41d57b.png)


## Browsing: Tor Browser

This challenge was considerably more difficult as it required a series of steps:
1. Finding the location of app data for the Tor Browser
2. Browsing through the folders to locate files that contain history/cache information
3. Sorting by last modfied date to look at the most recent files
4. Searching individual files for URLs

![url](https://user-images.githubusercontent.com/71312079/155442682-c80ded52-df95-4b88-8eff-93add23c533e.png)

```URL: https://www.cashoutempire.com/reviews/```


## Chat Client: 

### Name

There was a hint in the challenge that it was an XMPP chat client, and a quick google search of popular XMPP chat clients showed one that also appeared in the *Program Files (x86)* directory: ```Pidgin```

### Nickname

After knowing the chat client, I did a quick google search for the location of the pidgin logs: ```C:\Users\joohn\AppData\Roaming\. purple\logs```. Browsing through the subdirectories I eventually find joohn's nickname: ```johnny007```

![nickname](https://user-images.githubusercontent.com/71312079/155444621-845c2fb1-0931-4b2b-bfd1-294de4d25358.png)

## Email Client: 

### Software Name

Similar to the chat client, the software ```Thunderbird``` was immediately evident in the *Program Files* directory 

### Suspect Email

Again I repeated the same steps as the chat client but this time for the user *Pandemic* and went to ```C:\Users\Pandemic\AppData\Roaming\Thunderbird``` folder to browse around and eventually found Marcus Brown's email: ```exhibitlinux2019@gmail.com``` in the **Sent** folder: 

![marcus_brown_email](https://user-images.githubusercontent.com/71312079/155447900-6ebfd0d4-51f8-4d20-8f33-956efe04277f.png)


