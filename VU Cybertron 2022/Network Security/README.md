# Handshaking 

We are given a [PCAP](./VUCYBERTHON2022.cap) file and instruction to crack the captured WPA2 handshake. 

I don't really know much about WPA2 handshakes or how to locate them in a pcap file, but I realised that **aircrack-ng** has inbuilt capabilities for doing so.

Following the steps in this [article](https://www.aircrack-ng.org/doku.php?id=cracking_wpa), all I needed to do was run the following command with the *rockyou.txt* wordlist available in Kali:

```bash
aircrack-ng -w rockyou.txt VUCYBERTHON2022.cap
```

After around 20 minutes, the key was cracked and I was able to obtain the password:

![aircrackng](https://user-images.githubusercontent.com/71312079/155347132-000f17d3-6462-4f97-90e0-1ae97b99bfe5.png)


```Flag: cybernet2```