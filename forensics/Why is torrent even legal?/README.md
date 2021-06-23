# Bacon Rule
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

For this challenge, candidates are required to research and have a basic understanding of the malware in this pcap file. By reading up on the txt file given, it shows some
snort rules of how to set up an IDS to prevent the trickbot malware.

From there, candidates will be able to identify trickbot typically uses http traffic . By filtering, candidates will be able to limit down the amount of traffic
they need to analyse. Reading through http traffic, it will show 2 users identified in this pcap, philip which is the victim and timothy which is the attacker.
This can be identified in packet 12866 and packet 2256. To locate the password, candidates need to identify the http post request packet 1600. By following the tcp stream,
it will show that victim's account data have been exfiltrated through the malware.

![image](https://user-images.githubusercontent.com/69874238/121502579-e0858180-ca12-11eb-9245-ecb6ecb5e0c4.png)



The flag is:

```
wssqrctf{gh3ntf@st}
```
