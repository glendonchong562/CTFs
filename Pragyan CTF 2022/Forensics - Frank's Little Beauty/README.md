# Frank's Little Beauty (500 Points)

## Challenge Description:

![Challenge Description](https://user-images.githubusercontent.com/71312079/157819124-a640023d-3bbe-4acc-89b0-62ed0898bd35.png)

We are given a memory dump and a clue that the challenge can probably be solved solely using Volatility2 (Since the profile of *Win7SP1x64* is given)


The flag is broken down into 3 parts: 

## Part 1

From the challenge description, the "*lazy to type*" portion provides us with a hint that the **clipboard** plugin may be useful for us. Running it in Volatility 2 reveals a pastebin URL that was copied to the clipboard.

![clipboard](https://user-images.githubusercontent.com/71312079/157819096-c4878ceb-a28c-45a0-bf74-9181b4d9581b.png)

Navigating to the pastebin URL reveals the first part of the flag: 

![pastebin](https://user-images.githubusercontent.com/71312079/157819581-4286ea11-8a3d-435c-aa78-bd75bea2fb12.png)

```Flag_1: p_ctf{v0l4t1l1ty```

## Part 2

Following another hint: *"Reuses passwords"*, I then run the **hashdump** plugin and see that following output: 

![hashdump](https://user-images.githubusercontent.com/71312079/157820074-4ea2023f-bac4-424d-ba0c-1c1cee0fa861.png)

Knowing that the hashdump output format is **Username:RID:LM:NTLM**, I take both the LM and NTLM password hashes to be cracked on [crackstation](https://crackstation.net/) and the NTLM password hash is cracked to **trolltoll**. 

Hmm, seems like we now need to find a locked file (zip/rar) that we can use the password on. I open volatility's **cmdline** output in Timeline Explorer and see some interesting output: 

![cmdline](https://user-images.githubusercontent.com/71312079/157819106-93173bdf-1558-4ed0-817d-8c7623afba31.png)

I see 3 files of interest:
1. **comp.rar**
2. **README.txt** [Will be discussed in Part 3]
3. **sysinfo.txt** [Will be discussed in Part 3]

**comp.rar** seems to be what I'm looking for, so I find its offset using the **filescan** plugin:

![filescan](https://user-images.githubusercontent.com/71312079/157819111-470b6c7c-570a-49b9-b4b2-be60e5f1ba6b.png)

I then extract it using the following command:

```bash
vol.py -f MemDump.DMP --profile=Win7SP1x64 dumpfiles -Q 0x000000003df4e450 --dump-dir .
```
Renaming the output file to *comp.rar*, I input **trolltoll** as the password and receive the second flag:

![flag2](https://user-images.githubusercontent.com/71312079/157819114-43ebdd41-d286-46ed-a7ca-73595a9ef78c.png)

```Flag_2: _i5_v3ry_h4ndy_at```

## Part 3

Following up from the **cmdline** output mentioned earlier, *sysinfo.txt* did not stand out to be right away as suspicious so I check out *README.txt* using the output from the **mftparser** plugin:

![README](https://user-images.githubusercontent.com/71312079/157819121-f0af7479-8b14-47ef-a90a-4e64b67e95f9.png)

After searching for 'Downloads' in TimelineExplorer from the output of **filescan**, I see an interesting file: **Paddys.lnk** 

![downloads](https://user-images.githubusercontent.com/71312079/157824174-fe19d0c9-c29a-4fc2-aa01-49d6bc3dfea0.png)

Given that the challenge description also mentioned Frank not knowing the shortcut to Paddys, I extract the lnk file and viewed its properties in Windows Explorer.

![PADDYs](https://user-images.githubusercontent.com/71312079/157819120-6bfc9254-2aff-4873-ac93-0018275237b9.png)

Seeing that the target is **sysinfo.txt**, I search for this file from mftparser's output and find the final flag in the $DATA section.

![flag3](https://user-images.githubusercontent.com/71312079/157819117-5b54203c-2960-4e63-beb4-bf68cbdafcc0.png)


```Flag_3: _r34d1ng_dump5_iasip}```

NOTE: I also tried directly extracting **sysinfo.txt** but was unsucessful in obtaining it with **dumpfiles**


Combining all 3 parts together we can obtain the full flag: 

```Flag: p_ctf{v0l4t1l1ty_i5_v3ry_h4ndy_at_r34d1ng_dump5_iasip}```




