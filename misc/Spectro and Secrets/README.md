# Spectro and Secrets
Author: [Xiaozhi](https://github.com/xiaoxiao69)

## Description

Linux filtering commands knowledge
Basic audio forenics
## Requirements 

- Sonix Visualizer
- 7 zip package
- Kali command line
- Search engine

## Sources

- [Pingu.zip](https://github.com/ChanTingHui/wssqrctf/blob/main/misc/Spectro%20and%20Secrets/bin/Pingu.zip)


```
Pingu's friend have seemed to send a message in his home directory. Can you find the flag? Embed the message in the flag syntex.
```


## Exploit

Candidates are given a zip file that contains part of a Linux home directory. After unzipping the file in kali , user can explore the file directories and files contained in the file. There are 25 text file in documents , 0 files in downloads, two html pages in Desktop , 4 image file in Pictures and a password protected zip file in Music. Candidates are first required to scan for any hidden files downloaded by using following command:
```
ls -la
```
This will show that file .config was a hidden directory. By using entering the .config directory, there is a png given which gives a possible hint to a password in Music. The picture state the following:

![image](https://user-images.githubusercontent.com/69874238/123474018-f22e7200-d62b-11eb-8048-180cffa97da5.png)

This could be refering the text files in the Documents directory. By using the following command in the Document directory , we can filter out the file that contained "3dvcmQ" in part of the line:
```
head * | grep -r 3dvcmQ
```
![image](https://user-images.githubusercontent.com/69874238/123477561-cd88c900-d630-11eb-9bb9-0b7b389bd6a7.png)

This will file show that file 21 contains the following string : "UGFzc3dvcmQzNCQ3czI=". Since it was hinted that it is encrypted , using an online cipher identifier , we can learn that the string was base 64 encoded. By decoding it, we will receive the following password: "Password34$7s2"

Using the 7z package command, we are able to unzip and enter the password of the file "Jammingmusic.zip".
```
7z x Jammingmusic.zip
```

It will show that it contain a hint file and .wav file which is an audio file. The hint states that there is a hidden message in the audio given. When listening to the audio, it play a frequency that does not describe anything. The hint also gave a clue about voice print and the question stated " spectro" which can help identify what tools to use to get the flag. Searching up voiceprint into google gives a wikipedia result of voiceprint which is related to spectrogram which is used to analyse spoken words. Using sonic visualizer and adding the spectrogram using the pane tab, it will show message in the audio.

![image](https://user-images.githubusercontent.com/69874238/123476644-9534bb00-d62f-11eb-9c13-0ebfd11e0af5.png)


Embed the message in the flag syntex.


The flag is:

```
wssqrctf{L@ve_th1s_s1nger}
```
