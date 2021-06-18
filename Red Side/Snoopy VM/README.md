# Anshel Goldfield's Theory
Author: [Xiaozhi](https://github.com/xiaoxiao69)

## Description

Asymetric encryptionknowledge and Anshel Anshel Goldfield key exchange knowledge

## Requirements
- Wikipedia
- Search engine

## Sources

- [keys.txt](https://github.com/ChanTingHui/wssqrctf/blob/main/crypto/Anshel%20Goldfield's%20Theory/bin/keys.txt)
```
Miss Ashley and Mr Gordon were trying to exchange some asymmetric keys to get a shared key. They aren't very good at math, so they decided to use a Rubik's Cube instead to do the crypto. This is not the best way to secure it, but I think we can get their shared key.
```

## Exploit

Matching the description with the provided information we get,

Mr. A public key: [B' U', F B F, R' D, B D'] this is a

a1 = B' U' a2 = F B F a3 = R' D a4 = B D'

Mr. G public key: [R D L', D U' B, U F', L' F] this is b b1 = R D L' b2 = D U' B b3 = U F' b4 = L' F

Then private key A and B is chosen from sequence of elements from a and b

Mr. A sends: [B D' R' D R D L' D' R D B', B D' R' D D U' B D' R D B', B D' R' D U F' D' R D B', B D' R' D L' F D' R D B']

if we look at the moves - B D' R' D and D' R D B' is in all elements . First element contains R D L' in the middle. This is in sync with the description.

Therefore, A inverse = B D' R' D and A = D' R D B'

Mr. G sends: [U F' R D L' B' U' L D' R' F U', U F' R D L' F B F L D' R' F U', U F' R D L' R' D L D' R' F U', U F' R D L' B D' L D' R' F U']

Use the same idea to get B inverse = U F' R D L' and B = L D' R' F U'

SHARED KEY IS A_Inv .B_Inv .A.B = B D' R' D U F' R D L' D' R D B' L D' R' F U'



The flag is:

```
wssqrctf{B D' R' D U F' R D L' D' R D B' L D' R' F U'}
```
