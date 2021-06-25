# folderception
Author: [Xiaozhi](https://github.com/xiaoxiao69)

## Description

John the Ripper and Kali commands knowledge

## Requirements 

- John the Ripper
- rockyou.txt
- Kali command line
- Hex editor

## Sources

- [strong_password.zip](https://github.com/ChanTingHui/wssqrctf/blob/main/crypto/Ocean's%20Secret/bin/strong_password.zip)


```
A file in a file. Wait what is going on?
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

After entering the spongebob into the file. Candidates will be greeted with a image . To find if there is a file hidden in the image, use an online hex editor can check the last few hexes of the file. When analysing, it is shown there is a folder named flagfolder contain an image named "cresent5star.jpg" in this image. To extract the image, simply use the unzip command on the image. 


The flag is:

```
wssqrctf{e3_pa55w0rd_h3re}
```

