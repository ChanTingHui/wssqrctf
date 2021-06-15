# Tier 1 Followers
Author: [Xiaozhi](https://github.com/xiaoxiao69)

## Description
Hex editor and hex analyser

## Requirements
- Hex editor

## Sources

- [onlyfans.jpeg](https://github.com/ChanTingHui/wssqrctf/blob/main/forensics/Tier%201%20Followers/bin/onlyfans.jpeg)

```
This flag can only be given to my favorite and devoted fan boys <3. Will you be able to read it for me ?
```

## Exploit

For this challenge, candidates are given a jpeg file. When opened, candidates will be greeted with a message that the file is not supported by the image viewer on windows
or something similar on other image viewers.

Candidates are required to open the file in a hex editor software to view that the first 8 bytes of the file are misconfigured. Candidates are required to either search online
for a jpeg format hex bytes or use an existing jpeg image to view a jpeg format hex byte. Candidates are then required change the first 8 bytes to the following:

```
FF D8 FF E0 00 10 4A 46
```
After editing the hex bytes value, candidates will be able to see the image and the flag hiding inside the image.


The flag is:

```
wssqrctf{rll7_b1g_dog3_f4n}
```

