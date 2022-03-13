# Reconstruction (35 Points)

## Challenge Description: I received an interesting file that's supposed to create a picture, but I'm not exactly sure how. Wanna give it a shot?

I am given a file that I renamed [bytes.txt](./bytes.txt) that contains a list of comma separated numbers, likely the RGB values for individual pixels. In order to reconstruct the image, I used python's PIL library and the script below:

``` python
from math import sqrt
from PIL import Image

a = open('bytes.txt','r').read()[:-3] # remove the trailing ,;
str_arr = a.split(',')

#convert to number array
num_arr = [int(i.replace(';','')) for i in str_arr]

num_pix = len(num_arr) // 3 #3 values/pxel
dim = int(sqrt(num_pix)) # assuming square image -> obtain width/height 

img = Image.frombytes('RGB', (dim, dim), bytes(num_arr))
img.save('flag.png')
```
Running the script produced a flipped image that I flipped in the Windows *Paint* to produce the flag:

![flag_flipped](https://user-images.githubusercontent.com/71312079/155844710-e65095ec-7987-49b9-8a3c-3b607dae5338.png)

```Flag: flag{411_7h3_king5_h0rs3s_and_a11_th3_kings_m3n}```