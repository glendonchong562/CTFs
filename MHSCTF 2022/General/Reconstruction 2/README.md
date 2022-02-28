# Reconstruction 2 (40 Points)

## Challenge Description: More fixing-upping to be done. Can I count on you again?

This challenge was difficult for me because I did not recognise the text in the provided file: [Reconstruction2](./Reconstruction2). 

![reconstruction2_snippet](https://user-images.githubusercontent.com/71312079/155845831-140aca7a-847c-42fb-a3aa-37a43d788ee9.png)


After getting a hint from my team mate that the challenge was related to SVG, I read up about the SVG syntax from the following [article](https://css-tricks.com/svg-path-syntax-illustrated-guide/) and learnt the following basics:

* **Letters** are commands 
  * Capital letters are absolute 
* **Numbers** are passing values to the commands
* Highlighted words:
  * m: Pick up the pen and move it to the specified relative location
  * q: Draw a bezier curve based a single bezier control point and end at specified coordinates
  * z: Draw a straight line back to the start of the path 

In order for the code to render as a proper SVG, I then performed the following modifications to obtain the flag: 

1. Add \<svg width="1500" height="400" xmlns="http://www.w3.org/2000/svg"> to the top for attributes for the XML Namespace
2. Add \</svg> to bottom of the file
3. Add <path d = "..."/> to every line starting with m/M to invoke the pen tool in Illustrator to create the basic shapes
4. Renamed the file to [Reconstruction2.svg](./Reconstruction2.svg) and opened it in Microsoft Edge 

```Flag: flag{svg_b4ckgr0und5_4r3_c001}```