# this-file-hides-something (medium)

## Challenge Description: There is an emergency regarding this file. We need to extract the password ASAP. It's a crash dump, but our tools are not working. Please help us, time is not on our side.

NOTE: I did not solve the challenge during the challenge duration but I included this writeup as a reminder that I should follow my gut feeling and not look for complicated tools for an easy challenge.

We are given a file called **crashdump.elf**. Running *file* on it showed that it was an **ELF 64-bit LSB core file, x86-64, version 1 (SYSV)**. This threw me off quite a bit because I haven't analysed ELF core dump files before and I googled for tools but didn't find any that could retrieve the password. 

Initially, I ran volatility on it and saw that it had a profile of *Win7SP1x64* and was a little confused because I thought it was a linux operating system? I even tried to use *strings* to find the version of linux but to no avail. At this stage I gave up and moved to a different challenge.

After the competition ended, I saw that all I had to do was run the *lsadump/mimikatz* module on vol2 to obtain the flag:

**mimikatz**

![flag](https://user-images.githubusercontent.com/71312079/153878086-19c16901-a141-4b32-b6c6-be3d69038bca.png)

**Lsadump**

![flag_with_lsadump](https://user-images.githubusercontent.com/71312079/153880641-59b0a20e-0833-45c9-83cb-80b98dbce99e.png)

Password: ```Str0ngAsAR0ck!```
