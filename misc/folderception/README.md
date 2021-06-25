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

- [strongpass.zip](https://github.com/ChanTingHui/wssqrctf/blob/main/misc/folderception/bin/strongpass.zip)


```
A file in a file. Wait what is going on?
```


## Exploit

Candidates are required to use John the Ripper to unlock the password encrypted zip file. Firstly, candidates are required to extract the hash of the file using the following
command. <br/>
```
zip2john strongpass.zip > strongpass_hash
```

To crack the hash: <br />
```
john strongpass_hash --wordlist=rockyou.txt
```

The result will show the password to the encrypted file is spongebob.Entering the spongebob into the file. 
```
7z x strongpass.zip
```
Candidates will be greeted with a image . To find if there is a file hidden in the image, use an online hex editor can check the last few hexes of the file. When analysing the hex, it is shown there is a folder named flagfolder contain an image named "cresent5star.jpg" in this image. 

![image](https://user-images.githubusercontent.com/69874238/123493882-86aacb80-d650-11eb-9e53-d5196c822f27.png)


To extract the image, simply use the unzip command as it does not require any password.
```
unzip itwasi.jpg
```
After unzipping, "flagfolder" will be extracted from the picture and by entering the folder , it will show "cresent5star.jpg". However, a flag is still not shown. Check the file for any hidden text in the image using the following command.
```
strings cresent5star.jpg 
```
It will then print out the flag at the bottom out the output.
![image](https://user-images.githubusercontent.com/69874238/123493829-506d4c00-d650-11eb-9e2c-fc050e85c8ed.png)


The flag is:

```
wssqrctf{e3_pa55w0rd_h3re}
```

