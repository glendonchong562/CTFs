# Let's Walk Together (50 Points)

A png file called **interesting_waves.png** is provided

![2022-01-22 20_58_44-interesting_waves_resized](https://user-images.githubusercontent.com/71312079/150639528-ba32c00d-a01b-4752-8e5f-1a74be9cd1cf.png)

Examine the png with *exiftool* reveals that the png contains trailing data

![exiftool](https://user-images.githubusercontent.com/71312079/150639128-6c36b871-249e-484c-b614-f4bf376fe76b.png)

*Binwalk* is then used to extract the embedded file and we see that the flag is found inside **11150.zip**, a password protected zip file 

![Flag](https://user-images.githubusercontent.com/71312079/150639402-d0c0ad97-1860-443e-9318-28d04aa8453c.png)

I performed the following steps to attempt to retrieve the password:
* Ran *strings* on the png to see if it contained the password
* Ran *stegoveritas* on the png to see if the password was in embedded files/RGB layers
* Studied the graph in the png to see if it was somehow related to the password 

After the steps mentioned above were unsuccessful, I just decided to attempt to brute force the password with *john* using the following bash commands in Kali Linux:
```bash
zip2john 11150.zip > hash.txt
john hash.txt
```
Within 5 seconds the brute force attempt was successful and the password (**letmein!**) was revealed! The cracked password was then used to unlock the zip file and retrive the flag

FLAG: KCTF{BiNw4lk_is_h3lpfUl}

---

# Unknown File (50 Points)

The file of interest was called **unknown.file**
The following commands were then run on the file:
* *file* : No known file type, only a generic 'data' type
* *strings*: 'IHDR' header, revealed to be characteristic of png file upon a quick google search

![strings](https://user-images.githubusercontent.com/71312079/150640716-118bfcbb-892d-4ca5-863c-1f9d9cba8c0e.png)
I then opened the file in a hex editor and saw that first few bytes of the file did not match the magic signature of a png file:
``` 89 50 4E 47 0D 0A 1A 0A ```

Old Header:
![old_header](https://user-images.githubusercontent.com/71312079/150640781-446c0e0c-a9b7-4b42-ac3e-893b1910af12.png)

New Header:
![new_header](https://user-images.githubusercontent.com/71312079/150640790-32419c54-a434-4052-89d2-30d399b97030.png)

Changing the first few bytes of the file yielded a properly formatted png file with the flag.

Flag: KCTF{Imag3_H3ad3r_M4nipul4t10N}

