# Emperor's Cipher
Author: [Xiaozhi](https://github.com/xiaoxiao69)

## Description

Github 

## Requirements
- Github
- Caesar cipher
- Search engine


## Sources

- [cipher.txt](https://github.com/ChanTingHui/wssqrctf/blob/main/crypto/Emperor's%20Cipher/cipher.txt)

```
An ancient emperor have passed down an ancient flag after his death. The flag is a6645q7t{ce8_jvoff_127_3ijj}.
Help us decrypt this code!
```

## Exploit

You need to identify the decryption cipher first. A hint was given in cipher.txt . By entering the hint into google or any search engine, candidates will be able to identify 
this quote mentioned by Julius Caesar. By searching up Julius Ceasar cipher , candidates will be able to identify the code is encoded in the caesar cipher.

Candidates are then required to decrpyt the code using cryptii or any online Caesar cipher decoder using shift 14 and change the decoding regex 
to abcdefghijklmnopqrstuvwxyz0123456789.


The flag is:

```
wssqrctf{y0u_5ha11_not_p455}
```
