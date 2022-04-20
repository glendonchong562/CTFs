# Torrent Anlyze

## SOS, someone is torrenting on our network.One of your colleagues has been using torrent to download some files on the company’s network. Can you identify the file(s) that were downloaded? The file name will be the flag, like `picoCTF{filename}`

For this challenge, we are given a pcap file filled with torrent traffic and tasked to identify a file from the traffic. We are also provided with the following hints:

1. Download and open the file with a packet analyzer like [Wireshark](https://www.wireshark.org/) 
   
   - No too helpful as I already knew that I had to use Wireshark to open the PCAP file

2. You may want to enable BitTorrent protocol (BT-DHT, etc.) on Wireshark. Analyze -> Enabled Protocols
   
   - Very helpful as the traffic appeared gibberish before doing this

3. Try to understand peers, leechers and seeds. [Article](https://www.techworm.net/2017/03/seeds-peers-leechers-torrents-language.html)
   
   - Read this article but also proved to not be very useful since I already understood how torrenting works

4. The file name ends with `.iso`
   
   - Helpful in the end as a method of checking that I obtained the correct file
   
   - Initially went down a rabbit role of trying to carve the ```iso``` magic number or string from the traffic 

This was my first time looking at torrent data on wireshark, and some of the difficulties that I faced before finally getting a correct search query were as follows: 

- Not knowing which BT protocol to search for
  
  - Eventually searched for **bt-dht-bencoded.string contains info_hash which contains file metadata and specifically a file hash ([Wireshark Documentation]([Wireshark &#183; Display Filter Reference: BitTorrent DHT Protocol](https://www.wireshark.org/docs/dfref/b/bt-dht.html)))

- I knew that the IP **192.168.73.132** was suspicious but initially filtered for *ip.dst* instead of *ip.src* and did not obtain anything 
  
  - *ip.src* means that the host seeded the file to other nodes

After narrowing down the results I proceeded to look at the *info_hash* field which contains the SHA1 hash of the file.

![wireshark_search](https://user-images.githubusercontent.com/71312079/164132386-eb0e6294-036d-431b-b066-7c9b78ce3410.png)

I searched the hash ```e2467cbf021192c241367b892230dc1e05c0580e``` on google and received the corresponding iso file ```ubuntu-19.10-desktop-amd64.iso```, which was also the filename in the flag.

FLAG: `picoCTF{ubuntu-19.10-desktop-amd64.iso}`
