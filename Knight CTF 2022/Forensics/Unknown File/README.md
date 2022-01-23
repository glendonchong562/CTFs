# Unknown File

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