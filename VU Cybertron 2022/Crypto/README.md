# Blinded by the lights

For this challenge we are given a [zip](./Challange_1.zip) file that contains a text file called [email.txt](./email.txt). Using *john* with the *rockyou.txt* wordlist [], I am able to obtain the password of **82573032060021gt**.

![zip_pw](https://user-images.githubusercontent.com/71312079/155351530-f4f09619-5f39-4544-95be-5407047bcbe5.png)

NOTE: I initially did not use a wordlist and it took too long because the default mode is brute force and the actual password was rather long (**16 characters**)

Opening email.txt, I see that that there is an encoded file called *flag.txt* with encoding that looks like base64. Turns out it wasn't a single decoding but multiple steps of decoding (I used Dcode's [cipher identifier](https://www.dcode.fr/cipher-identifier) to determine each step):

1. Base64 
2. Hex 
3. Alphuck
4. Morbit Cipher 
5. Base32
6. Brainfu*k
7. Base64

Running the steps above finally produced the flag:

```Flag: n0w_y0u_533_why```