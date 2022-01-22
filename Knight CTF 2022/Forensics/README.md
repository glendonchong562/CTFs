# Let's Walk Together 

We are provided with a png file called **interesting_waves.png**
(Insert png)

We examine the png with *exiftool* and note interesting 

(Insert screenshot)

*Binwalk* is then used to extract the embedded file and we see that the flag is found inside **11150.zip**, a password protected zip file 

(Insert screenshot)

I examined the png file again (strings/stegoveritas) to see if it contained the passwords but to no avail. I then decided to attempt to brute force the password 
with *john* using the following bash commands in Kali Linux:
```bash
zip2john 11150.zip > hash.txt
john hash.txt
```
Within 5 seconds the brute force was successful and the password (**letmein!**) was revealed! The cracked Password was then used to unlock the zip file and retrive the flag

(Insert SS)

FLAG: KCTF{BiNw4lk_is_h3lpfUl}