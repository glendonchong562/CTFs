# Baby APT (Day 1)

We are given a PCAP file called **christmaswishlist.pcap**. Opening the pcap in wireshark, I first check the *Protocol Hierachy*, where I see that the bulk of the traffic is **TLS**, with a small portion of **HTTP** traffic.

![protocol_hierachy](https://user-images.githubusercontent.com/71312079/151584332-28f2fd03-09cc-40bc-8fd5-d5d5c06a1cbd.png)

Following the TCP streams, I note the presence of a web shell on a server, allowing the client to execute arbitary commands on the server. Here we see that the password hashes have been succesfuly retrieved from the server through the command *cat /etc/passwd*.

Request:
![getpasswd](https://user-images.githubusercontent.com/71312079/151584350-93aa1cf1-d2a4-45db-8ec7-b971bf1f07e7.png)

Response:
![passwd](https://user-images.githubusercontent.com/71312079/151584339-04daedb0-6ed1-4fa9-9656-483bf70e2195.png)


Scrolling through the TCP streams, I see both:
1.  TLS streams (**Can't do much since we don't have the decryption key**) 
2.  HTTP streams (**In plaintext thus of interest to us**)

I thus ignore the TLS streams. From the HTTP streams, I see the execution of a couple of other commands :
* groups
* ls -a
* ls -al /var/www/html/sites/default/files
* rm /var/www/html/sites/default/files/.ht.sqlite && echo **SFRCezBrX24wd18zdjNyeTBuM19oNHNfdDBfZHIwcF8wZmZfdGgzaXJfbDN0dDNyc180dF90aDNfcDBzdF8wZmYxYzNfNGc0MW59** > /dev/null+2>&1 && ls -al /var/www/html/sites/default/files

The last command looks interesting to me as it looks like it is encoded in *base64*. Decoding it produces the flag:


![flag](https://user-images.githubusercontent.com/71312079/151584321-2e9c0b62-9d48-47ee-97be-aa5d6e627ad2.png)


Flag: `HTB{0k_n0w_3v3ry0n3_h4s_t0_dr0p_0ff_th3ir_l3tt3rs_4t_th3_p0st_0ff1c3_4g41n}`


