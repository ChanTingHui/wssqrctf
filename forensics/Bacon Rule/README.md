# Bacon Rule
Author: [Xiaozhi](https://github.com/xiaoxiao69)

## Description
Wireshark filtering and Snort rules understanding 

## Requirements
- Wireshark
- Snort rules

## Sources

- [Lost.pcap](https://github.com/ChanTingHui/wssqrctf/blob/main/forensics/Bacon%20Rule/bin/Lost.pcap)
- [crispy.txt](https://github.com/ChanTingHui/wssqrctf/blob/main/forensics/Bacon%20Rule/bin/crispy.txt)

```
A computer have been infected. Help to find the user's password. For this flag, embed the password in flag syntex 
(e.g. wssqrctf{I_am_password}).
```

## Exploit

For this challenge, candidates are required to research and have a basic understanding of the malware in this pcap file. By reading up on the txt file given, it shows some
snort rules of how to set up an IDS to prevent the trickbot malware.

From there, candidates will be able to identify trickbot typically uses http traffic . By filtering using http.request.uri , candidates will be able to limit down the amount of traffic to http traffic only.
Reading through http traffic using http.request.uri contains "/90", it will show 2 users identified in this pcap, philip which is the victim and timothy which is the attacker which can be identified in packet 12866 and packet 2256. 

To locate the password, candidates can identify the http post request packet 1600 by using the following filter :

```
http.request.uri contains "/81" and ip contains mail
```


By following the tcp stream, it will show that victim's account data have been exfiltrated through the malware.

![image](https://user-images.githubusercontent.com/69874238/121502579-e0858180-ca12-11eb-9245-ecb6ecb5e0c4.png)



The flag is:

```
wssqrctf{gh3ntf@st}
```
