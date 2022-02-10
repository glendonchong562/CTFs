# No Strings (100 points)

## Challenge Description: did you try strings?

We are given a file called **chall**. Running the file produces a prompt for the flag: 

![chall](https://user-images.githubusercontent.com/71312079/153361393-5cf32eb4-7af0-4a95-862d-b3f979f7f22b.png)

Next, I open the file in IDA and see that the *main* function has multiple variables and function calls, all of which look very foreign to me. Here is a snippet:

![main](https://user-images.githubusercontent.com/71312079/153361387-e6cea4dc-6815-4c51-8b9c-cac532072b26.png)

Being new in reversing, I decide that examining each function and variable would take too long and so I decide to do a string search for **'Enter the flag'**, bringing me to this window:

![string_search](https://user-images.githubusercontent.com/71312079/153361389-b49a8d02-2671-478b-ab8e-0fcac8b51209.png)

Here I see a string of interest: *cybergrabs{}* - our flag format without its contents. Clicking its X-REF, I am brought to an IDA view where I see ASCII characters right below this address that look alot like our flag.

![flag](https://user-images.githubusercontent.com/71312079/153361375-aa2db3b3-9dcd-470b-b9bd-72bbef31e41d.png)

I manually concatenated these characters and obtain the string **4lWAY5_sTrInG$_DOEs_No7_WORK**.

Running the file again with and inputting `cybergrabs{4lWAY5_sTrInG$_DOEs_No7_WORK}` produced the prompt: `Congratulations!!`

FLAG: `cybergrabs{4lWAY5_sTrInG$_DOEs_No7_WORK}`