# Ye Olde Threat (500 Points)

## Challenge Description: One of your spies has obtained intel about the resurgence of an old threat to the planet. He was only able to get this text file to you. Find the nature of the threat to help stop it.

We are given a txt file called **intel.txt**. Opening the file reveals a base64 encoded string that decodes to a URL from Google Drive which hosts a file **intel.zip**. Downloading and extracting the zip file yields a broken png image [Just_A_Plane_Image.png](./Just_A_Plane_Image.png).

These were the following steps taken to fix the file:

1. Opened the file in Hxd64 and fixed the following:
   * File header
   * IHDR chunk 
   * 1st IDAT chunk 

*Original*
![org_1](https://user-images.githubusercontent.com/71312079/157845555-6e5cc47b-0554-4e80-b262-94ffd5f889c3.png)

*Modified*
![cor_1](https://user-images.githubusercontent.com/71312079/157845542-f2d0bf4c-74fb-478d-82e3-8134f2c93c54.png)


2. Length of 2nd IDAT chunk

NOTE: All the IDAT chunks had a length of **0x2000** and the 2nd one was an outlier with length of **0x08010902** and so it needed to be fixed

*Original*

![org_2](https://user-images.githubusercontent.com/71312079/157845558-9e45e352-371f-4683-910a-d3ed4b7d543f.png)

*Modified*

![cor_2](https://user-images.githubusercontent.com/71312079/157845552-f2f4adfd-2719-4657-a5dd-5ec926129b45.png)

3. Fixed the CRC with [PCRT](https://github.com/sherlly/PCRT)

PCRT is a great tool as it locates and automatically fixes the wrong CRC.

![PCRT](https://user-images.githubusercontent.com/71312079/157846843-27738406-2d39-4e9f-b2d0-7ae8e182fbca.png)

After fixing the CRC and verifying with *pngcheck*, we finally see a functional PNG file! 

![pngcheck](https://user-images.githubusercontent.com/71312079/157847513-71c099ca-513e-44df-9ce8-9b74c0969f77.png)


*final.png*


![final](https://user-images.githubusercontent.com/71312079/157846027-1a630886-0080-45a4-befc-430d44f67a94.png)

4.  Inverted the planes in *Stegsolve*

Alas, no flag can be seen and so I used stegsolve to invert the RGB planes and see the flag in one of the planes:

![final png_Blue_2](https://user-images.githubusercontent.com/71312079/157838139-3083b875-79ed-4f0e-9ddf-766970c53d5d.png)


```Flag: pctf{K@nye_w@nt5_To_Buy_Th3_3n71r3_E4rth}```


