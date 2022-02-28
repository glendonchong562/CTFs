# Mysterious (55 Points)

## Challenge Description: Find the input.

We are given a file that I renamed [code.txt](./code.txt). I didn't recognise the code at first so I did a google search and stumbled across [Befunge](https://en.wikipedia.org/wiki/Befunge). There wasn't alot of documentation on it so I found another [article](https://github.com/catseye/Befunge-93/blob/master/doc/Befunge-93.markdown) that sheds more information on it.

Befunge is a stack-based 2D programming language, with the following relevant features:
* Control flow dictated with the following symbols: **<>^v**
* Arthimetic operators work on the top 2 stack elements: **+-**
* Saves the 3rd stack element at the coordinates (x,y) which are the 1st and 2nd stack elements respectively: **p**
* Receive input and store them LIFO on the stack: **~**
* End of the program: **@**

I took the code and placed it in an online [Befunge interpreter](https://befunge.flogisoft.com/)

![program](https://user-images.githubusercontent.com/71312079/155667043-a2250825-4aa8-4eff-a4ab-dc33b4a6eda1.png)

After knowing the output, I then proceeded to enter an input string of ```1111111111111``` and see the shift of each element for the corresponding output. The shifts are then reversed and stored in the array called *rev*. A python script below is then crafted:

```python
out = "v+L^0k@%~~a`F"
In = ""
rev = [7,14,34,-42,1,-59,-11,14,-3,-23,0,12,32]

for i in range(len(out)):
    In += chr(ord(out[i]) + rev[i])
   
print(In[::-1])
```
Running the code above produces the flag:

```Flag: flag{35014n9}```