# Willywonker VM

This directory consists of challenges related to `Willywonker VM`.

Author: Joe

# Walkthrough

•	First, run the netdiscover command on the Kali machine. This command will scan the network for ip addresses.
•	Nmap -sV the ip addresses and it will show open port 22, 80, 31337
•	Access the Ip address and you will get to the website. 
•	On the website, view page source and when you hover over the rabbit, it will show the name of the img which is assets/img/p0rt_31337.png which points us to port 31337
•	 
•	I keyed in the port number after the ip address and it brought me to a different website. (192.168.56.106:31337)
•	At the new website, I viewed its page source and found a hidden base64 encoded message
 
•	Decoded this message and got a cypher.matrix name which could be a file.
 
•	Entered it into the address bar after the port (31337/Cypher.matrix) and got a downloadable bin file.
 
•	The file displayed Brainfuck encoded content. Googled Brainfuck decoder and it gives us this message. “You can enter into matrix as guest, with password k1ll0rXX. Note: Actually, I forget last two characters so I have replaced with XX try your luck and find the correct string of password.” 
 
•	After that, use crunch command to generate a wordlist to brute force. (crunch 8 8 -t k1ll0r%@ -o password.txt) %@ is the missing string value.
•	Used hydra to brute force ssh login and found out the password was k1ll0r7n. (hydra -l guest -P password.txt 192.168.56.106 ssh) 
   
•	Then, ssh into the vm by using ssh guest@192.168.56.106 using the credentials found.  
•	We are in a restricted environment, so we have to escape it by running vi. Then using !:/bin/bash.  
•	After escaping restricted shell, ran export SHELL=/bin/bash:$SHELL and export PATH=/usr/bin:$PATH so that linux commands can work. 
 
•	Sudo -l works however sudo su doesn’t as /bin directory have not been export to PATH, run export PATH=/bin:$PATH to allow it to work properly.
 
•	Run sudo su and key in credentials found earlier on which is k1ll0r7n
•	In the environment, used cd to change directory and ls to list the files and flag.txt was there.
•	Cat flag.txt and it shows us the flag 


