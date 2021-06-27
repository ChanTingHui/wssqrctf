# Why is torrent even legal
Author: [Xiaozhi](https://github.com/xiaoxiao69)

## Description
Wireshark filtering

## Requirements
- Wireshark

## Sources

- [GoddamTorrent.pcap](https://github.com/ChanTingHui/wssqrctf/blob/main/forensics/Why%20is%20torrent%20even%20legal%3F/bin/GoddamTorrent.pcap)

```
Our employee received alerts on bittorrent traffic from 10.0.0.201 on our network. Help us identify the file being seeded (shared) by the torrent client on 10.0.0.201?
Embed the SHA1 hash in wssqrctf{x} where x is the hash}
```

## Exploit

Candidates are given a hint that this pcap traffic is caused by a torrent client. By doing a search on torrent , candidates can view on the wikipedia page on how a torrent traffic work. A torrent file is usually given out by a bittorrent client to allow the host to download small parts of file from an original data that have already downloaded it. The wikipedia also shown examples of seeds in the under the title extension named "http seeds" which states that the torrent file retreiving data from a list of website. On the file structure section of the , it shows torrent file contains announce as part of its url section,

The wikipedia have given a lot of examples of how to locate the file downloaded. To filter out the file that was seeded , use the following filter syntax:

http.request.uri contains .torrent

This will show packet 4264 . By following the tcp stream of the packet, it will show that the torrent file downloaded was named Betty_Boop_Rhythm_on_the_Reservation.avi.torrent and was sent by the host named publicdomaintorrents.com. 
![image](https://user-images.githubusercontent.com/69874238/123537806-f6f64180-d763-11eb-9263-2ec89c6d9bec.png)

The above information showed us the host 
The flag is:

```
wssqrctf{e4be9e4db876e3e3179778b03e906297be5c8dbe}
```
