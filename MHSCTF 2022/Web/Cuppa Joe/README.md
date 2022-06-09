# Cuppa Joe (30 Points)

## Challenge Description: A new coffee shop is opening up in my neihborhood! It's called Cuppa Joe and I can't wait to check it out! It would ahem be a real shame if someone were to ahem hack their website and, hypothetically, get their secret flag. mhsctf-cuppajoe.0xmmalik.repl.co (you may need to wait for the site to wake up)

I visit the website and am greeted with the following page: 

![main](https://user-images.githubusercontent.com/71312079/155993838-dd3d16a3-f8a1-4db8-bb41-1bf70f34a75a.png)

Clicking any of the links (index/flag/message) doesn't seem to do anything and seeing the form submission I immediately think of XSS.

1. Checked that the vulnerable to XSS
   * Used \<script>alert('XSS!)\</script> and saw the alert message box
2. Inputted \<img src=https://mhsctf-cuppajoe.0xmmalik.repl.co/flag.php> to access *flag.php*
   * Code was taken from https://book.hacktricks.xyz/pentesting-web/dangling-markup-html-scriptless-injection

![xss php](https://user-images.githubusercontent.com/71312079/155993845-005e5fc7-0d2e-4981-bf5c-71ac6a72973e.png)

3. Opened image in a new tab to get the flag

![messagephp](https://user-images.githubusercontent.com/71312079/155993839-9f8ad745-cda3-4f42-b441-81d9a0ecdf08.png)
