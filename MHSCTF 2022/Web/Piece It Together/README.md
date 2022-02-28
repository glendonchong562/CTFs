# Piece It Together (15 Points)

## Challenge Description: My friend dared me to find the secret password to their website, but their code is so messy! It's impossible to see what's what! Can you help me? mhsctf-pieceittogether.0xmmalik.repl.co (you may need to wait for the site to wake up)

I visited the website and am presented with the following page: 

![login](https://user-images.githubusercontent.com/71312079/155997062-940cdc43-e274-479b-9e9e-c4a8b41ba12d.png)


Wanting to analyse the source code more, I saved it to a file called [piece_it_together.html](./piece_it_together.html)

The code contains multiple instance of **&#** appended by numbers, which looks to be characteristic of [HTML character references](https://en.wikipedia.org/wiki/List_of_XML_and_HTML_character_entity_references).

After 2 rounds of HTML entity decoding in cyberchef, I am presented with the following cleartext code:

![cyberchef](https://user-images.githubusercontent.com/71312079/155998260-a812c966-8718-4018-b0af-6e85a4f30e14.png)

Hmm seems like *_var0xa8fe* is responsible for the authentication and looks to be obfuscated. Using a [HTML beautifier](https://beautifier.io/), I am able to see the function that checks for the password and obtain the flag: 

![flag](https://user-images.githubusercontent.com/71312079/155995009-04604102-9777-49e4-96b4-1b7067e351b9.png)

```Flag: flag{j1gs4w}```


