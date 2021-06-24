# Emperor's Cipher
Author: [Xiaozhi](https://github.com/xiaoxiao69)

## Description

Github 

## Requirements
- Github
- Caesar cipher
- Search engine


## Sources

- [cipher.txt](https://github.com/ChanTingHui/wssqrctf/blob/main/crypto/Emperor's%20Cipher/bin/cipher.txt)

```
I heard a rival fast food chain is trying to compete with subway. Can you find out which restaurant is it?
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
