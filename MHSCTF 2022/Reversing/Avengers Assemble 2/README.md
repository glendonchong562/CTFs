# Avengers Assemble 2 (70 Points)

## Challenge Description: Time for some more exploiting-secret-clubs'-authorization-software-to-gain-access fun! This time, they gave us a file and a website to input our responses. I would do it myself but I have... homework. mhsctf-avengersassemble2.0xmmalik.repl.co (you may need to wait for the site to wake up) Note: the file uses the .asm extension which is not necessarily entirely accurate. Don't try to brute force the website, there are over 600 million possible combinations.

Navigating to the website, we see that we need to fill in the correct arthimetic operators in order to obtain the flag. The source code is provided below:

``` 
c$ = 0
tv64 = 4
d$ = 8
a$ = 32
b$ = 40
int mystery(int,int) PROC                              ; mystery
$LN3:
        mov     DWORD PTR [rsp+16], edx
        mov     DWORD PTR [rsp+8], ecx
        sub     rsp, 24
        mov     eax, DWORD PTR a$[rsp]
        mov     ecx, DWORD PTR b$[rsp]
        sub     ecx, eax
        mov     eax, ecx
        mov     DWORD PTR tv64[rsp], eax
        mov     eax, DWORD PTR a$[rsp]
        cdq
        idiv    DWORD PTR b$[rsp]
        mov     eax, edx
        mov     ecx, DWORD PTR tv64[rsp]
        imul    ecx, eax
        mov     eax, ecx
        mov     DWORD PTR c$[rsp], eax
        mov     eax, DWORD PTR a$[rsp]
        imul    eax, DWORD PTR b$[rsp]
        mov     ecx, DWORD PTR c$[rsp]
        add     ecx, eax
        mov     eax, ecx
        mov     DWORD PTR d$[rsp], eax
        imul    eax, DWORD PTR b$[rsp], 5
        mov     ecx, DWORD PTR a$[rsp]
        imul    ecx, DWORD PTR c$[rsp]
        add     eax, ecx
        mov     ecx, DWORD PTR b$[rsp]
        imul    ecx, DWORD PTR d$[rsp]
        sub     eax, ecx
        add     rsp, 24
        ret     0
int mystery(int,int) ENDP                              ; mystery
```

This challenge was good because I'm not all too familiar with assembly syntax and so through the challenge I was able to learn the following: 

* Cdq: Sign extend EAX into EDXv (Typically before a division operation)
* idiv: Quotient is stored in *ecx* and remainder is stored in *edx*

I followed the code step by step and filled in the following arthimetic operators as seen below: 


```Solution:```


![answer](https://user-images.githubusercontent.com/71312079/155991845-597cc978-c207-4db7-8b00-0c563b1785f9.png)
