NOTE: This challenge had 3 parts, requiring the previous part to be solved before the next would be unlocked 

# Wayback 1 (50 points)

## Challenge Description: Some answers are hidden in the past, Whose website theme did we “cyberange.io” used when we first went public.

This challenge was great because I've learnt about [waybackmachine](https://archive.org/web/) before but never actually used it. Searching up *cyberange.io*, I see that the website was formed in *2016* and there were *46* available screenshots.

![cyberange io_history](https://user-images.githubusercontent.com/71312079/152742347-ff467a64-dadc-4019-9d26-849c4ee3afcd.png)

 Clicking the earliest available screenshot on **2 Nov 2017**, I scroll to the bottom and see the website theme's artist:

![artist](https://user-images.githubusercontent.com/71312079/152742334-9662c285-d006-471c-8284-ff1f55996d86.png)

FLAG: `flag{andrea_galanti}`



# Wayback 2 (100 points)

## Challenge Description: Some answers are hidden in the past, Find the phone number of the person in Wayback 1

From the previous challenge and screenshot, I noted that *Andrea Galanti* was hyperlinked and clicked on it, where I am brought to his personal [website](http://www.andreagalanti.it/) from 2017.

I translate the page from Italian to English and find a link to his personal information. Clicking that link brings me to this page with his phone number:

![telephone](https://user-images.githubusercontent.com/71312079/152742356-517c6b1b-056e-4915-a900-47e6fcd7942f.png)

FLAG: `flag{393451384748}`

# Wayback 3 (200 points)

## Challenge Description: Some answers are hidden in the past, his number is unavailable now, find his skype id

This challenge was less straightforward, I continued clicking around on Andrea's website but found no mention of his skype ID. I even considered sending him an email and maybe would receive an automatic response with his skype ID but decided against that in case his email is still active and he gets swarmed LOL. 

After hitting several dead ends with browsing to his social media accounts (*Linkedin/Instagram/Twitter*), I eventually decided to go to Skype itself and check if I could find him there (His skype id is unlikely to change after 4 years right?)

As it turns out, Andrea Galanti is a pretty popular Italian name and I found many hits on Skype. After adding the additional word `italy` (as if that was needed?), I found a profile picture that looked somewhat like him, in addition to *91* in the skype ID which was the year that Andrea was born, based on the previous screenshot. This turned out to be the correct skype ID.

![Skype](https://user-images.githubusercontent.com/71312079/152742350-c27ebd64-264a-439d-8056-0bc6684bded0.png)


FLAG: `flag{ixidron91}`



