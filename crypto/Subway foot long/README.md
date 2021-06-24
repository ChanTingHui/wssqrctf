# Sub 64 inches sandwich
Author: [Xiaozhi](https://github.com/xiaoxiao69)

## Description

Github 

## Requirements
- Binary Converter
- Substitution cipher
- Search engine


## Sources

- [cipher.txt](https://github.com/ChanTingHui/wssqrctf/blob/main/crypto/Emperor's%20Cipher/bin/cipher.txt)

```
I heard a rival fast food chain is trying to compete with subway. Can you find out which restaurant is it?
```

## Exploit

You need to identify the decryption key first. There are two types of variable given in the txt file. The easier file to decrypt would be the binary which when decrypted using a binary to text converter will give the following cipher key: vwodrqulcnfsmxybpthgejzkai. The question title have given a hint on what cipher is used to get the flag. By searching up sub cipher in google, it will show a substitution cipher.

The way substitution cipher works is replacing all the alphabet with another alphabet using a cipher key. In this case, the plain text string 
abcdefghijklmnopqrstuvwxyz us now replaced with vwodrqulcnfsmxybpthgejzkai. By using an online substitution cipher tool and specifying the cipher key, candidates can obtain the flag for this question.

The flag is:

```
wssqrctf{subwaysnmcdonlads}
```
