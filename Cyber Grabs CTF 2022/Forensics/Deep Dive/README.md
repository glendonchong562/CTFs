# Deep Dive (200 points)
 
## Challenge Description: This challenge file have some secret files hidden deep inside which you might need.

This challenge involves a Microsoft Word file called [**hacker.docx**](hacker.docx). Opening up the file, I see that it is the Wikipedia page of the word **"Hacker"** that spans 9 pages:

*Page 1*:

![2022-02-07 12_11_19-hacker docx - Word](https://user-images.githubusercontent.com/71312079/152723285-d9919144-ff40-468b-9e1f-ceafb0358b1e.png)

From the challenge description, it seems like there are embedded files that I will need to access in order to obtain the flag. 

Given that a *docx* file is really just a *zip* file, I rename it to **hacker.zip** and extract it. I then explore the folders and come across the media folder with a bunch of images:

![media_folder](https://user-images.githubusercontent.com/71312079/152723717-ec36e3b7-64b6-41e1-82ae-6cef6bdb1f3b.png)

I scroll through the images and find the flag in [image8.png](image8.png)


FLAG: `cybergrabs{1337_c3r531_1_w4n7_h3r_70_kn0w_17_w45_m3}`