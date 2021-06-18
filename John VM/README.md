# John VM

This directory consists of challenges related to `John VM`.

Author: Jerick

# Walkthrough

Fortress VM Walkthrough
Step 1) nmap scan. You’ll find that there is a port 80 open. 
Step 2) Visit the page 
 
Step 3) Dirbuster to find scanner.php
 
Step 4) Use burp intercept the http request
 
Step 5) Enter ls to see the list of directories 
 
Step 6) ls slkr3t and cat flag.txt  
 
1st FLAG:
FLAG{n0_one_br3aches_teh_f0rt}

2nd Flag:
Step 1) ls kingd0m_k3yz, see 2 directories master and passwd
Step 2) cat kingd0m_k3yz/master to find a single entry. Copy the password hash into a text file for later use. 
 
Step 3) cat /etc/passwd to find users craven and vulnhub
 
Step 4: ls into craven’s home directory
 
Step 5: cat /home/craven/hint.txt
 
Step 6: Open reminders.txt to find the pet name
 
Step 7: Create a dictionary.txt to use by using crunch. 
Step 8: john –wordlist=dict.txt (file with the hashed password jn)
Step 9: Username: craven and password: 931qwerty?
Step 10: ssh in as craven, ls and cat flag.txt
 
2nd FLAG {w0uld_u_lik3_som3_b33r_with_ur_r3d_PiLL}

Flag 3:
For this part you would need to do a symlink process
Third flag is in /home/vulnhub
There is a script called reader that is used to read the file. However, purely running the reader with flag.txt is not going to work.
Performing symlink process
Step 1) cd /tmp
Step 2) ln /home/vulnhub/flag.txt (random name)
Step 3) cd /home/vulnhub
Step 4) ./reader /tmp/(name)
Congrats you got the flag.
3rd FLAG
{its_A_ph0t0_ph1ni5h}

