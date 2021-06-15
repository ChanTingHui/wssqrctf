# Reversing is Fun - 1
Author: [Ting Hui](https://github.com/ChanTingHui)

## Description

Knowledge of XOR and conversions of bytes
Upderstanding of the source codes

## Requirements 

- labVIEW (community edition)
- Python
- XOR
- ascii codes


## Sources

- [reversingIsFun_1.vi](https://github.com/ChanTingHui/wssqrctf/blob/main/reverse/ReversingIsFun-1/bin/reversingIsFun_1.vi)

```
The Singapore Power Station confidential application has been released online. However, a passcode is required to get access to full control of the Power Station.
Please help us to figure out the passcode to get admin access.

Note: NO MODIFYING OF THE FILE AS IT WILL HAVE ERROR! PLEASE RUN AND STOP THE PROGRAM ONLY.

Hint: LabVIEW community edition will be required.
```


## Exploit
After opening the source file into LabVIEW, you will be greeted with a UI program. Next, by pressing Ctrl-E you will have of the pictorial of the source code.
<br />

After understanding of the source code, you will released that in order to get the flag, it requires two parts of encrypted strings to form the flag. For the first part of the flag, the substring of (0,11) is XOR with 5 of each character.
<br />

For the second part of the flag, the source code shows that the remain string from 11 onwards will be reversed follow by a deduction of 10(0xA).
After understanding of the source code, you can code a [python](https://github.com/ChanTingHui/wssqrctf/blob/main/reverse/ReversingIsFun-1/bin/solution.py) code to decrypt and get the flag.
<br />


The flag is:

```
wssqrctf{x0r_F1@g_w1n}
```
