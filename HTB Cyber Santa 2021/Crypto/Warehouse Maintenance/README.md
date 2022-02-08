# Warehouse Maintenance (Day 5)

**Disclaimer**: I did not manage to solve this challenge during the CTF due to the short time given to challenges on the final day.

This challenge involves generating a valid signature for a message of our choosing with the following characteristics: 
* Unknown salt value prepended to the signature hash 
* Known range for the length of the salt values [```randint(8,100)```]
* Ability to see the signature associated with known plaintext (```USE xmas_warehouse;
#Make sure to delete Santa from users. Now Elves are in charge.```)
* Known data to add to to the original plaintext that queries the backend database to display all tables (```SHOW tables;```)
  * NOTE: Code for the backend database can be found [here](util.py)

As such, it was vulnerable to a **Hash Length Extension** attack, of which I referred to this [writeup](https://ctftime.org/writeup/22046) for more details and code snippets.

Challenge.py:

```python
import signal
import subprocess
import socketserver
from random import randint
import json
import hashlib
import os
from util import executeScript

salt = os.urandom(randint(8,100))

def create_sample_signature():
	dt = open('sample','rb').read()
	h = hashlib.sha512( salt + dt ).hexdigest()

	return dt.hex(), h

def check_signature(dt, h):
	dt = bytes.fromhex(dt)
	
	if hashlib.sha512( salt + dt ).hexdigest() == h:
		return True

def challenge():
	print("Welcome to Santa's database maintenance service.\nPlease make sure to get a signature from mister Frost.\n")
	while True:
		try:
			print('1. Get a sample script\n2. Update maintenance script.\n> ')
			option = input().strip()

			if option=='1':
				data, sign = create_sample_signature()
				payload = json.dumps({'script': data, 'signature': sign})
				print(payload + '\n')
			elif option=='2':
				print('Please send your script and its signature.\n> ')
				resp = input().strip()
				resp = json.loads(resp)
				if check_signature(resp['script'], resp['signature']):
					script = bytes.fromhex(resp['script'])
					res = executeScript(script)

					print(res+'\n')
				else:
					print('Are you sure mister Frost signed this?\n')

			else:
				print('There is no such an option.\n')
				exit(1)
		except Exception as e:
			print(e)
			print('Invalid payload. Bye!')
			exit(1)


def main():
	try:
		challenge()
	except:
		pass

if __name__ == "__main__":
	main()
```
Prior to performing the hash length extension attack, we need to determine the length of the hash based on the response from the server.
```python
from random import randint
import json
import hashlib
import os
from hashpumpy import hashpump
from pwn import *

p = remote("178.62.5.61", 32500)
p.sendlineafter(b'> ', b'1')

sample = json.loads(p.recvline().decode().strip())
sig = sample['signature']
knowndata = b'USE xmas_warehouse;\n#Make sure to delete Santa from users. Now Elves are in charge.'
data_to_add = b'\nSHOW tables;'

for key_length in range(8,101):
     p.recvuntil(b">")
     p.send(b'2')
     signature, script = hashpump(sig, knowndata, data_to_add, key_length)
     d = {"script": script.hex(), "signature": signature}
     payload = bytes(json.dumps(d), 'utf-8')
     p.recvuntil(b">")
     p.sendline(payload)
     result = p.recvuntil(b'\n')

     if b'Are you sure mister Frost signed this?' in result:
        log.info(f"key_length {key_length} failed, trying next")
        continue
     else:
        log.info(f"correct secret length was {key_length}")
        correct_secret_len = key_length
        break
```
At the same time, we have now successfully run the command: "```SHOW tables;```" and note the presence of a table called **materials**.
![2022-01-24 17_22_00-HTB CyberSanta 2021 - Crypto Writeups – ctf rip](https://user-images.githubusercontent.com/71312079/150755607-6c4c5e83-ee1a-47b1-a682-e32e9804154d.png)

We now proceed to dump the contents of the **materials** table with the following new query:

```python
query = b'\nSELECT * FROM materials;'
p.recvuntil(b">")
p.send(b'2')
signature, script = hashpump(sig, knowndata, query, correct_secret_len)
d = {"script": script.hex(), "signature": signature}
payload = bytes(json.dumps(d), 'utf-8')
p.recvuntil(b">")
p.sendline(payload)
print(p.recvline())
```
Running the code above reveals the flag.

Flag: HTB{h45hpump_15_50_c001_h0h0h0}




