# Toy Management (Day 2)

Similar to day 1's challenge, we are given the source code of a web application along with its Dockerfile. I navigate to my local instance and am greeted with this screen: 

![login_page](https://user-images.githubusercontent.com/71312079/151394809-3af7cb3e-380f-40eb-b2a5-6af61665d829.png)

Hmm... I immediately think of SQL injection when I see this login page and so I next turn to the source code to obtain more information about the web application and its routes.

I first navigate to *routes.js*, where I see the login mechanism with the supplied username and password:

![login](https://user-images.githubusercontent.com/71312079/151394206-1062ee15-ca5b-4485-a896-8f31879b5133.png)

I next navigate to the **loginUser** function, located in *database.js*.

![loginuser](https://user-images.githubusercontent.com/71312079/151394209-5b250e91-8aa6-49be-8a6c-d1b3987ba90a.png)

Here I see SQL statement that will be executed from the inputted username and password, and looks to be vulnerable to a classic SQL injection command as the input appears to not be sanitised.

In order to craft my SQL Injection statement, I navigate to the database file (*database.sql*), noting that it is a **mysql** database with the flag in a table called **toylist**. Interestingly, the flag is the only toy that is not approved on the list.

![database](https://user-images.githubusercontent.com/71312079/151394183-b586cf68-0908-46b0-a044-c75110fe91a6.png)

Navigating back to *routes.js*, I see that a successful login will generate a valid cookie and the *dashboard.html* will be rendered. 
![dashboard](https://user-images.githubusercontent.com/71312079/151400031-50885efc-12b4-4e1e-9987-184fb137b2a1.png)

Additionally, a script called *dashboard.js* will be called, which fetches */api/toylist* that is seen in the image below.

I also see that logging in as admin would result in the variable **approved** having a value of 0 and passed to the *listToys* function.

![api_list_toys](https://user-images.githubusercontent.com/71312079/151394179-64824f84-c6e1-4139-9e9b-07e386a53698.png)

Browsing to the *listToys* function, I can see that the variable **approved** is passed into the SQL statement. This means that logging in as admin will now enable me to see toys that are have an approved value of **0**, exactly what I want in order to see my flag.

![list_toys](https://user-images.githubusercontent.com/71312079/151394193-09ec6eaa-4f13-4302-8b18-cb0e8a644284.png)

I now craft the SQL injection query, noting the correct **mysql** syntax for comments based on its [documentation](https://dev.mysql.com/doc/refman/8.0/en/comments.html).

Username: 
* admin' -- 
  * NOTE: There is a space after the --
* admin' #

Password: Any value

Using either one of the aforementioned usernames would authenticate me and I can then see the flag.

![flag](https://user-images.githubusercontent.com/71312079/151479732-6167cf5c-8b08-425d-917a-1184a8ade58a.jpg)

Flag: `HTB{1nj3cti0n_1s_in3v1t4bl3}`


