# Weird Music (25 Points)

## Challenge Description: Does this music sound familiar to you? It's a little bit different though. Remember to use the "flag{...}" format.

We are given an audio file that I named [weird.mid](./weird.mid). As this was my first time encountering a midi file, I did a bit of research and found that it could be opened by Windows Media Player. However, Windows Media Player only allows you to listen to it and I wasn't able to discern anything after listening to it a couple of times.

Next, I used **audacity** to open the file and saw the following: 

![audacity](https://user-images.githubusercontent.com/71312079/155545936-0df7b18b-5fce-4232-9462-1ed3fd1223e1.png)

It wasn't immediately evident to me that it was morse code, due to the presence of multiple rows and no clear dots and dashes. I went down a few rabbit holes trying to convert the midi file/looking at LSB but ended up going back and seeing that all I needed to do was compress them all into a single row and I would get the morse code where the longer lines were the dashes and the shorter ones were the dots.

Running the morse code in a decoder produced the flag:

![decode](https://user-images.githubusercontent.com/71312079/155545961-b051c13d-d950-49eb-bef2-19b29e0a30cb.png)

```Flag: flag{BEEP_BOTOPM}```

