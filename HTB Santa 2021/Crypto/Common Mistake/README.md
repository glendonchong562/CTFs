# Common Mistake (Day 1)

For this challenge, we are given 2 ciphertexts encrypted with RSA. Both ciphertexts have the same plaintexts and modulus, but were encrypted with different values of e. 

I've seen this type of challenge before and immediately thought about the Common Modulus Attack, where the Extended Eucledian Algorithm is used to find the gcd of the ciphertexts, as well as **a** and **b** to retrieve the plaintext. More information and the code I adapted can be found at this [link](https://infosecwriteups.com/rsa-attacks-common-modulus-7bdb34f331a5).

```python


```

Running the code aboe produced the flag

Flag: HTB{c0mm0n_m0d_4774ck_15_4n07h3r_cl4ss1c}