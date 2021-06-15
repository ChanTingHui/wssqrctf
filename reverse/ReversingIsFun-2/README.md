# Reversing is Fun - 2
Author: [Ting Hui](https://github.com/ChanTingHui)

## Description

Knowledge of bits rotation
Conversion of ASCII to unicode
interleaved array


## Requirements 

- labVIEW (community edition)
- Python
- understanding the length for each flag
- ascii and unicodes understanding


## Sources

- [reverse_me_if_you_can.vi](https://github.com/ChanTingHui/wssqrctf/blob/main/reverse/ReversingIsFun-2/bin/reverse_me_if_you_can.7z)

```
Another of Singapore Power Station confidential application has been released online. However, this time it requires a combination of 5 passwords to get the final passcode into the application.
I know u can do this. I believe in you.

Hint: 
- LabVIEW community edition will be required.
- Find a way to temper the number of tries to ignore the one time try.
- Phase 4 requires the inspection of the .tdms file
```


## Exploit
After opening the source file into LabVIEW, you will be greeted with a UI program. Next, by pressing Ctrl-E you will have of the pictorial of the source code.
<br />

After understanding of the source code, you will released that in order to get the actual flag. It requires a combination of 5 flags, and each flag is arrange by their substring length.
<br />

For the first flag, there are two arrays of integers and each arrays are rotated left by 3 bits and 4 bits of its respective arrays and are compared with two constant bytearrays. In addition, the bytes are treated as 8-bits unsigned integers.
<br />

For the second flag, the bytearray is represented in a form of RGB values. R being the 'byte values', G being the 'constant value' and B being the 'array index'.
<br />

For the third flag, the flag are split into two parts and 7 bytes each, then interleaved. By re-organising the characters, you will get the flag.
<br />

For the fourth flag, every 2 characters in the .tdms file are concatenated and are given an array index. By inspecting the .tdms file, and re-positioning the characters base on their array index, you will get the flag.
<br />
For the fifth flag, when inspecting the source code of the application in the fifth phase, you will realised that only character 'd' returns True while the rest returns False. After going deeper, you will realised that a part5_P3 vi has a password protecting it and to get to that the password is hidden behind a comment "BEHIND THE SCENES". After opening the source code using the password, you will realised that the input of the flag is multiplied by '7929' then followed by subtracting 0x49. Next, how can each of the output of the equation be equal to each comparision of values in the given array. For example, 990802 == 1187410. This is because both values are comparing its last 16 bits instead of its decimal.

Hence, after understanding the whole source code, you will need to code it out taken into consideration of some points mentioned above.
<br />


The flag is:

```
wssqrctf{g0t_fL@g_By_R3v3r$ing_th3_wh0L3_$ructur3_the_r1de_n3v3r_3nd5}
```
