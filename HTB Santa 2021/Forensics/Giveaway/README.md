# Giveway (Day 4)

We are given a zipped file containing a macro-enabled word document **chritmas_giveaway.docm**. I proceed to use *olevba* to view the contained macros.

![giveaway olevba output](https://user-images.githubusercontent.com/71312079/151481284-4d9b9fc3-a23d-45fd-8221-6c9cab820415.png)

Hmm... looks highly suspicious. Let's take a further look into the actual functions. Scrolling through the function, I see the following:

1. OS enumeration
![enumeration](https://user-images.githubusercontent.com/71312079/151481278-c2ddabcd-49b6-4931-b1a5-429c1650a3d6.png)

2.  Version checks + Testing network connectivity + Malicious file creation
![script_execution](https://user-images.githubusercontent.com/71312079/151481288-aa1218ee-abc8-40a4-9287-898952cdf71d.png)

3.  Obfuscated URL formed by concatenation of multiple variables
![flag_function](https://user-images.githubusercontent.com/71312079/151481280-ca78afad-a7f4-4eb0-b3d3-8ff7af3f7f84.png)

Out of the aforementioned observations, **3** seems the most interesting to me and so I used an online VB compiler from this [link](https://www.onlinegdb.com/online_vb_compiler) to let the compiler deobfuscate the code for me. I also added an extra line at the end to concatenate and print out all the variables and I obtained the flag.

![vbcompiler](https://user-images.githubusercontent.com/71312079/151481292-73f47336-bafa-4e21-8bbf-76abf7c1d960.png)


Flag: `HTB{Th1s_1s_4_pr3s3nt_3v3ryb0dy_w4nts_f0r_chr1stm4s}`
