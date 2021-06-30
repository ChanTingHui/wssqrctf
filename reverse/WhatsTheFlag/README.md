# Whats the Flag?

Author: [Ting Hui](https://github.com/ChanTingHui)

## Requirements

- Understanding of data movement instructions

## Sources

- [whatstheflag.asm](https://github.com/ChanTingHui/wssqrctf/blob/main/reverse/WhatsTheFlag/bin/whatstheflag.asm)

```
What does assembly(0x1f3) return? 
Submit the flag as a hexadecimal value (starting with '0x').
```

## Exploit

```asm
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	cmp    DWORD PTR [ebp+0x8],0x2323   ; Compare 0x1f3 to 0x2323
	<+10>:	jg     0x512 <asm1+37>              ; Jump not taken (0x1f3 is smaller)
	<+12>:	cmp    DWORD PTR [ebp+0x8],0x1f3    ; Compare 0x1f3 to 0x1f3
	<+19>:	jne    0x50a <asm1+29>              ; Jump not taken (they are equal)
	<+21>:	mov    eax,DWORD PTR [ebp+0x8]      ; eax = 0x1f3
	<+24>:	add    eax,0xb                      ; eax = 0x1f3 + 0xb = 0x1fe
	<+27>:	jmp    0x529 <asm1+60>              ; Jump taken
	<+29>:	mov    eax,DWORD PTR [ebp+0x8]
	<+32>:	sub    eax,0xb
	<+35>:	jmp    0x529 <asm1+60>
	<+37>:	cmp    DWORD PTR [ebp+0x8],0xcde
	<+44>:	jne    0x523 <asm1+54>
	<+46>:	mov    eax,DWORD PTR [ebp+0x8]
	<+49>:	sub    eax,0xb
	<+52>:	jmp    0x529 <asm1+60>
	<+54>:	mov    eax,DWORD PTR [ebp+0x8]
	<+57>:	add    eax,0xb
	<+60>:	pop    ebp                          ; We jump here
	<+61>:	ret 

````

<br /> 

The flag is:

```
wssqrctf{0x1fe}
```
