# Practice for School (55 Points)

## Challenge Description: I think it's a great terrible idea to get practice with some exploits you can absolutely should never use on school assignments. Join my Edpuzzle class using the given link and complete the only assignment there (it's called "flag{???????}"). www.edpuzzle.com/open/disvact Note: the video is 168 hours (1 week) long so you will not be able to watch through the whole thing. :)

I visit the website and am greeted with a login page for edpuzzle. I create an account and see that the assisgnment is to watch a video for 168 hours. The video cannot be clicked to the end as it is *locked*. I initially thought that this was a challenge that involves modifying the  JWT and spent awhile attempting to modify it but gave up in the end after seeing that there were no obvious vulnerabilities. I then obtained a hint from my teammate that the strategy was to manually adjust the video timing using the console in Google Chrome.

Viewing the elements in Chrome's Developer Tools, I navigate to the element that contains the video timing scrollbar and see that the total duration of the video is **604807** seconds.

![time](https://user-images.githubusercontent.com/71312079/155999339-8db693d9-7f8b-4716-91aa-f9fffe0db03f.png)

I don't have alot of experience with HTML or Javascript in general and so I referenced the following articles for help:

* [SetTimeout()](https://www.w3schools.com/jsref/met_win_settimeout.asp) - Calls a method after a certain number of miliseconds
  * I initially used *SetInterval()* but it would run the function repeatedly for the specified interval and I only needed to run the function once
  * The specified interval (**5**) after the comma means that the function will run after **5ms**
* [Arrow function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) (**=>**) as a compact alternative to a traditional function expression where  (Similar to lambda in python)
  * In this example, the function takes in no parameters **()** and performs the commands to the right of the arrow head
* [Document.querySelector()](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector) will return the first element in the document that matches the specified selector
  * I obtained the selector by searching for **\<video>** in the elements pane and copying the javascript path 


NOTE: I needed to change the Javascript context from the default (**top**) to the video (**X0RK2jz5HOI**) for the console commands to work
  


![console](https://user-images.githubusercontent.com/71312079/155999342-c84b7da8-c3df-4f11-aa20-0f465cba0c90.png)

Running the code in the console window above brought me to the end of the video and diplayed the flag.

![flag](https://user-images.githubusercontent.com/71312079/155999322-dd9f127d-f8d5-4b69-8058-3612ab1bb563.png)

```Flag: flag{th1s_15_a_us3ful_expl0it_f0r_sch00l}```


