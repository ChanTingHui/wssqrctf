# DIE & MENTION
Author: [Ting Hui](https://github.com/ChanTingHui)

## Description

Basic knowledge of hex

## Requirements 

- [TweakPNG](http://entropymine.com/jason/tweakpng/)
- 010 Editor

## Sources
- [fzktgaqqe](https://github.com/ChanTingHui/wssqrctf/blob/main/misc/DIE%20%26%20MENSION/bin/fzktgaqqe.zip)


```
Can you find the flag??? 
```


## Exploit

The zip file contains a file after extracting it. The file has an extension which is missing and the hex values have been removed. Hence, you will need to modify the hex values by looking at the last few values `IEND®B`to determind that it is a .png file as well as to modify the extention of the file in file explorer.
<br />
The image has been recovered but nothing shows as the dimension of the image have been modified to 1x1. You will need to use `TweakPNG` to modify the dimension back to an appropriate dimension to see the flag. However, When apply the image into `TweakPNG` you will realised that that the is a CRC mismatch error and you will need to modify the CRC hex values in hex editor again before you modify the dimensions.
<br />


The flag is:

```
wssqrctf{d1m3nsion_n33ds_chang3s}
```
