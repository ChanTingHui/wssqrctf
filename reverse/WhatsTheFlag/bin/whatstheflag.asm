assembly1:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	cmp    DWORD PTR [ebp+0x8],0x2323
	<+10>:	jg     0x512 <assembly1+37>
	<+12>:	cmp    DWORD PTR [ebp+0x8],0x1f3
	<+19>:	jne    0x50a <assembly1+29>
	<+21>:	mov    eax,DWORD PTR [ebp+0x8]
	<+24>:	add    eax,0xb
	<+27>:	jmp    0x529 <assembly1+60>
	<+29>:	mov    eax,DWORD PTR [ebp+0x8]
	<+32>:	sub    eax,0xb
	<+35>:	jmp    0x529 <assembly1+60>
	<+37>:	cmp    DWORD PTR [ebp+0x8],0xcde
	<+44>:	jne    0x523 <assembly1+54>
	<+46>:	mov    eax,DWORD PTR [ebp+0x8]
	<+49>:	sub    eax,0xb
	<+52>:	jmp    0x529 <assembly1+60>
	<+54>:	mov    eax,DWORD PTR [ebp+0x8]
	<+57>:	add    eax,0xb
	<+60>:	pop    ebp
	<+61>:	ret 
