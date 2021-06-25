# Ocean's Secret
Author: [Xiaozhi](https://github.com/xiaoxiao69)

## Description

John the Ripper and Kali commands knowledge

## Requirements 

- John the Ripper
- rockyou.txt
- Kali command line

## Sources

- [strong_password.zip](https://github.com/ChanTingHui/wssqrctf/blob/main/crypto/Ocean's%20Secret/bin/strong_password.zip)


```
A treasure have been washed up on the shore. Discover it's secret.
```


## Exploit

Candidates are required to use John the Ripper to unlock the password encrypted zip file. Firstly, candidates are required to extract the hash of the file using the following
command. <br/>
```
zip2john strong_password.zip > strong_password_hash
```

To crack the hash: <br />
```
john strong_password_hash --wordlist=rockyou.txt
```

The result will show the password to the encrypted file is spongebob.

After entering the spongebob into password of Garry's pet food.txt, candidates will be greeted with an google drive link leading to an image of Garry the snail. 
Candidates are required analyze the file using a cat command or strings and they will be able to find a string written in the file containing the following: 
Garry's flag ( 64 decode : d3NzcXJjdGZ7ZTNfcGE1NXcwcmRfaDNyZX0=).

Using an online base 64 decoder, candidates will be able to obtain the flag as wssqr{e3_pa55w0rd_h3re}.
<br />


The flag is:

```
wssqrctf{e3_pa55w0rd_h3re}
```
