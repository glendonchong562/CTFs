# Let's Walk Together (50 Points)

We are provided with a png file called **interesting_waves.png**
![interesting_waves](https://user-images.githubusercontent.com/71312079/150639112-c7d93f22-3714-4194-8769-578e9617a347.png)

We examine the png with *exiftool* and note that the png contains trailing data

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
