# Secure Browser???

Author: [Ting Hui](https://github.com/ChanTingHui)

## Description

Obfuscated JS in Frontend

## Requirements

- Dev-tools
- Docker: [Dockerfile](./Dockerfile)

## Sources

```
Secure Browser but is it really secure
```

## Exploit

First, you will need to view the page source and you will see a whole line of array.
You will realised that the variable 'var _0x575c' has been obsfucated and is checking for the password in the browser. However, the values are encoded to hex.

Next, in the function CheckPassword, the word `window` has been called multiple times. 
For example `window[_0x4bbdc3[0x0]][_0x4bbdc3[0x2]]` is actually storing the values to the local storage `window.localStorage.setItem` and `window[_0x4bbdc3[0x0]][_0x4bbdc3[0x1]]` is actually getting the value from `window.localStorage.getItem`

You will realised that the passwords are actually split into different parts. The password is 5W$Fbb=+nBE*pg4t^7M.
<br />

The flag is:
```
wssqrctf{th1$_mU$t_b3_c0nfUs1ng}
```
