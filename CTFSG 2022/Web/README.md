# Wildest Dreams Part 2
 
## Challenge Description: The opener is back for another round of fun. Enjoy

NOTE: I did not solve the challenge on my own but my teamate did and I included it here because I learnt about [PHP type juggling](https://medium.com/swlh/php-type-juggling-vulnerabilities-3e28c4ed5c09#:~:text=PHP%20has%20a%20feature%20called,to%20a%20common%2C%20comparable%20type.).

We are given the PHP source code [1989.php](./) for a web app. Focusing just on the PHP section: 

```php
<?php
if(!empty($_GET['i1']) && !empty($_GET['i2'])){
	$i1 = $_GET['i1'];
	$i2 = $_GET['i2'];
	if($i1 === $i2){
		die("i1 and i2 can't be the same!");
	}
	$len1 = strlen($i1);
	$len2 = strlen($i2);
	if($len1 < 15){
		die("i1 is too shorttttttt pee pee pee pee pee");
	}
	if($len2 < 15){
		die("i2 is too shorttttttt pee pee pee pee pee");
	}
	if(md5($i1) == md5($i2)){
		echo $flag;
	}
	echo "<br>The more that you say, the less i know.";
} else {
	echo "<br> You need to provide two strings, i1 and i2. /1989.php?i1=a&i2=b";
}
?>
```
Looking at the code, I see that 2 GET parameters need to be supplied, that 
1. \> 15 characters
2. cannot be the same value
3. will produce the same MD5 hash
   
I immediately think about MD5 hash collision, and proceed to spend time finding for simple strings to input that will cause a collision. Unfortunately, all the strings I found contained non-printable characters and therefore could not be inputted as the GET parameters. 

My teamate then suggested using *PHP type juggling*, which is a vulnerability where PHP can compare 2 different types (e.g ints and strings). Given that PHP's type-safe comparator "===" operator requires both to be the same value and the same type, the following 2 "magic strings" (taken from this [link](https://github.com/spaze/hashes/blob/master/md5.md)) would fail that check but pass the MD5 comparison check:

1. RSnakeUecYwT6N2O9g
    * MD5: 0e126635149374886577950106830662
2. RSnakeIeNRSb8KjzTw
    * MD5: 0e756073880949659567751252231576

While the 2 hashes are not identical, they have the same pattern of **^0+ed\*$** which equates to 0 in PHP when using the '==' operator. "0e..." is short for "0 to the power of something" and will always result in 0 regardless of the remaining characters. PHP thus interprets the MD5 string as an integer. For more information, check out this [link](https://www.whitehatsec.com/blog/magic-hashes/).

I inputted this URL (http://chals.ctf.sg:40401/1989.php?i1=RSnakeUecYwT6N2O9g&i2=RSnakeIeNRSb8KjzTw) and saw a youtube Link to Taylor Swift's Wildest Dreams MV and the flag. 

![flag](https://user-images.githubusercontent.com/71312079/158066711-bba84d8d-0e6d-4d45-bd82-e789e1be1dfb.png)

Flag: `CTFSG{you_see_me_in_h1nds1ght_tangled_up_with_you_all_night}`