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

---

# Unknown File

The file of interest was called **unknown.file**
The following commands were then run on the file:
* *file* : No known file type, only a generic 'data' type
* *strings*: 'IHDR' header, revealed to be characteristic of png file upon a quick google search

(Insert SS)

I then opened the file in a hex editor and saw that first few bytes of the file did not match the magic signature of a png file:
``` 89 50 4E 47 0D 0A 1A 0A ```

(insert SSx2)

Changing the first few bytes of the file yielded a properly formatted png file with the flag

Flag:KCTF{Imag3_H3ad3r_M4nipul4t10N}

