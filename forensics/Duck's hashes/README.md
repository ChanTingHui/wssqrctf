# Duck's hashes
Author: [Xiaozhi](https://github.com/xiaoxiao69)

## Description
- Wireshark traffic analysis knowledge
- Sguil traffic analysis knowledge
- Hashing knowledge
- File hash online research

## Requirements
- Wireshark
- Search Engine
- Image viewer
- Kali or online sha 256 hash viewer

## Sources

- [duckduckgoose.txt](https://github.com/ChanTingHui/wssqrctf/blob/main/forensics/Duck's%20hashes/bin/duckduckgoose.txt)

```
Noooooooooooo. Two of our employees have been hacked. Can you identify the malware? Embed the malware in flag syntex e.g. (wssqrctf{ILOVEYOU})
```

## Exploit

For this challenge, candidates are given a jpeg file containing a sguil traffic log and a pcap file. Candidates should be able to identify which traffic to look out for
based on the sguil log file. In the 4th row of the sguil screenshot, it contains an event message that states 
```
"ET MALWARE Windows executable sent when remote host claims to send an image M3". 
```
It is also the only alert that states that a malware have been detected through a jpeg file. From that row, candidates can also identify that the alert is triggered by traffic from 119.31.234.40 port 80 going back to 10.0.0.167 over tcp port 51132. Candidates should return to wireshark and filter the traffic using the following search syntex:
```
tcp.port eq 51132.
```
![image](https://user-images.githubusercontent.com/69874238/121823673-63d7f900-ccd9-11eb-871c-01d80a482077.png)

Candidates will then need to follow the tcp streams of the bytes to identify if a Windows executable file was identified by the server as an image.
After following the tcp stream of packet 5515, the following information is shown : 

![image](https://user-images.githubusercontent.com/69874238/121823218-62f19800-ccd6-11eb-9974-ce8c79449b16.png)

This shows that the name of the image file is png file named 8888.png which was sent by host alphapioneer.com. At the bottom, it also states this program cannot be run in DOS mode which indicates the exe file was identified as a image file. Next, candidates need to export the image file to do a further analysis. By clicking on file > Export objects >
HTTP (it is received through a webpage), candidates needs to download a file named 8888.png provided by alphapioneer.com. Arranging the hostname in alphabetical order, it is
located in the third row by packet 7388. 

![image](https://user-images.githubusercontent.com/69874238/121823376-7bae7d80-ccd7-11eb-8282-0c4b41f6fb49.png)

Candidates are reuired to save the file and check the sha 256 hash of the file. Run the following command on kali to view the hash value of the file:

shasum -a 256 8888.png

The output is the following : f6210da7865e00351c0e79464a1ba14a8ecc59dd79f650f2ff76f1697f6807b1

By copy and pasting the hash value into google, the first link will show that file orginated from a trojan malware named Qbot.
![image](https://user-images.githubusercontent.com/69874238/121823518-46eef600-ccd8-11eb-92f8-d569d57f3a15.png)



The flag is:

```
wssqrctf{Qbot}
