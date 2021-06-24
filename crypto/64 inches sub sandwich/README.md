# 64 inches sub sandwich
Author: [Xiaozhi](https://github.com/xiaoxiao69)

## Description

Github 

## Requirements
- Binary converter
- Substitution Cipher
- Search engine
- Base 64 decoder


## Sources

- [cipher.txt](https://github.com/ChanTingHui/wssqrctf/blob/main/crypto/Emperor's%20Cipher/bin/cipher.txt)

```
Subway have just came up with a new sandwich but we heard a rival fast food chain is trying to compete with them. Can you figure which one it is?
```

## Exploit

There are 2 key information given in the title for this question which is 64 and sub . By searching a 64 cipher and sub cipher on google, we will get a result of base 64 and substitution cipher. The way substitution cipher works is by encrypting by plaintext alphabets which are replaced with ciphertext key according to a fixed system. 

In the file given, there is a hint given that the encrypted text below given is a likely cipher key for the encrypted text above. Since we are not given a key for the substitution cipher, we will have to decrypt the text below using a base 64 decoder which will result in a binary given: 
01110110 01110111 01101111 01100100 01110010 01110001 01110101 01101100 01100011 01101110 01101001 01110011 01101101
01111000 01111001 01100010 01110000 01110100 01101000 01100111 01100101 01101010 01111010 01101011 01100001 01100110

Looks like we need to decrypt the binary above to receive a key, by using a binary to text converter, we will be given the key as : vwodrqulcnismxybpthgejzkaf. To prove that this is the key of the three given. Use a online character counter , it will there are 26 characters in the key which is required in substitution cipher as substitution replaces each alphabet with another alphabet. Since there are 26 alphabet in the world, this is correct key for this cipher. 

Using a substitution cipher decoder online, replace the key with the following: vwodrqulcnismxybpthgejzkaf
The flag will be decoded as the following:

![image](https://user-images.githubusercontent.com/69874238/123252796-40a21a80-d51f-11eb-9008-f0271ed17d12.png)


The flag is:

```
wssqrctf{eatfreshatmcdonlads}
```

