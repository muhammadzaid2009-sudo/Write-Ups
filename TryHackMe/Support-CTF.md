# 🛡️ Support Writeup | Muhammad Zaid

**Platform** : TryHackMe  
**Difficulty** : Medium  
**Catagory** : Web  
**Room Link** : https://tryhackme.com/room/support  

<img width="1535" height="782" alt="image" src="https://github.com/user-attachments/assets/ebf467c6-c6aa-4989-8f7c-79f92b5eb04f" />


## Objective
- Retriew the admin flag
- read the content of /home/ubuntu/user.txt file

## Prerequisites
- Nmap
- Directory enumeration
- Command Injection
- API Pentesting
- Web Fundamentals
- Linux Fundamentals
- Proxy tools

## What you'll learn
- Black Box Web pentesting
- Path Traversal
- Account takeover
- Command Injection
- API Pentesting

## Story
A new internal Support Operations Platform has been deployed to assist IT and helpdesk teams. The application handles user management, internal APIs, and system-level operations. However, security was not the primary focus during development. Several features rely on user-controlled input and weak trust boundaries.

# Step 1 Nmap
first we will gonna scan the target with nmap and see what services are running there
the command we will use for this 
`
namp -A -T4 <target ip> -vv -oN scan.txt
`
the -A is for the aggressive scan it combines -sV -sC -O scans with one switch 

we got the result 
```
# Nmap 7.99 scan initiated Wed Sep 30 19:22:02 2026 as: /usr/lib/nmap/nmap --privileged -A -T4 -vv -oN scan.txt 10.114.180.195
Nmap scan report for 10.114.180.195
Host is up, received echo-reply ttl 62 (0.14s latency).
Scanned at 2026-09-30 19:22:03 PKT for 37s
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 62 OpenSSH 9.6p1 Ubuntu 3ubuntu13.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 5a:c4:91:e3:eb:91:4b:49:ca:69:9d:f9:a2:43:07:2a (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBM2dMccHH8y6Vz0Rdudz4cR6Au3f0fTho38lc++trqrXue3rWRJ6o0VW/2fKW5lSEup2IByen6TAr4lz7QcBeTg=
|   256 6a:87:e2:1c:09:f1:ed:f6:23:3b:3d:e7:a3:46:e1:0e (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICvY7papDZRfOfd3MofO4SOcW8LHcgFA9IJlMq505x23
80/tcp open  http    syn-ack ttl 62 Apache httpd 2.4.58 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Support Operations Panel
|_http-server-header: Apache/2.4.58 (Ubuntu)
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.99%E=4%D=9/30%OT=22%CT=1%CU=42357%PV=Y%DS=3%DC=T%G=Y%TM=6ABD1B3
OS:0%P=x86_64-pc-linux-gnu)SEQ(SP=102%GCD=1%ISR=10E%TI=Z%CI=Z%II=I%TS=A)SEQ
OS:(SP=105%GCD=1%ISR=10B%TI=Z%CI=Z%TS=A)SEQ(SP=106%GCD=1%ISR=10B%TI=Z%CI=Z%
OS:TS=A)SEQ(SP=FD%GCD=1%ISR=10F%TI=Z%CI=Z%II=I%TS=A)SEQ(SP=FF%GCD=1%ISR=10F
OS:%TI=Z%CI=Z%II=I%TS=A)OPS(O1=M4E8ST11NW7%O2=M4E8ST11NW7%O3=M4E8NNT11NW7%O
OS:4=M4E8ST11NW7%O5=M4E8ST11NW7%O6=M4E8ST11)WIN(W1=F4B3%W2=F4B3%W3=F4B3%W4=
OS:F4B3%W5=F4B3%W6=F4B3)ECN(R=Y%DF=Y%T=40%W=F507%O=M4E8NNSNW7%CC=Y%Q=)T1(R=
OS:Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A
OS:%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y
OS:%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR
OS:%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RU
OS:D=G)IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 3.557 days (since Sun Sep 27 05:59:53 2026)
Network Distance: 3 hops
TCP Sequence Prediction: Difficulty=261 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 1723/tcp)
HOP RTT       ADDRESS
1   128.88 ms 192.168.128.1
2   ...
3   131.35 ms 10.114.180.195

Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Sep 30 19:22:40 2026 -- 1 IP address (1 host up) scanned in 37.99 seconds
```

as expected the port **80** is open meaning that a web service 
lets navigate to the web interface and try to see for something interesting 

there was a login page but we have not the username and password so i decided to brute forcing the directories on the server 

## Step 2 Directory Brute Force
for this task i used a tool named **feroxbuster** you can use any other tool you want

``
feroxbuster -u http://<target ip>/ -w /usr/share/wordlists/dirb/common.txt
``
the -u is for the target url -w for the wordlist path for this task i used the common.txt you can use any other wordlist if ypu want

the directories are
`` 
includes
layout
skin
js
``

the checked every directory i found nothing so i decided to go back on the login page and there was mentioned an email address which was this `help@support.thm` 
so i decided to use that email and tired some passwords and all of theme were invalid so i tried to brute force it 

## Step 3 Using Hydra

Hydra is a powerful tool for brute forcing i kept the email same and tried to brute force the password 

`hydra -l 'help@support.thm' -P /usr/share/wordlists/rockyou.txt -s 80 10.114.180.195 http-post-form "/:email=^USER^&password=^PASS^:Employee Authentication" -f
`
i used this command to brute force the login page i used -l because i want to tell hydra that keep the username this and just brute force  password next is -P is for the password wordlist -s fo the port number method is post and -f telling hydra stop after finding the correct password.

the hydra result 

<img width="1527" height="262" alt="image" src="https://github.com/user-attachments/assets/87c75765-2190-46ba-9855-04915b2ecdc3" />

it found the password lets try to login in the web and lets see what we have

<img width="1535" height="648" alt="image" src="https://github.com/user-attachments/assets/bf85bd3a-978a-4d50-b181-1ee7eea12f79" />

<img width="1535" height="250" alt="image" src="https://github.com/user-attachments/assets/ded637a7-1061-40a0-878e-7a811368fadc" />


then i go to the developer options and saw my cookie and there was a parameter `isITUser` and after that there was a `md5` hash then i tried to crack this hash using online tools the most powerful tool is crackstation.net

<img width="1471" height="597" alt="image" src="https://github.com/user-attachments/assets/94d572b6-13b0-4f6c-ba0a-1cd7d05367b1" />

there is a value set to false so tried to cahnge it to true using md5hashgenerator.com
<img width="1302" height="617" alt="image" src="https://github.com/user-attachments/assets/a507ca3f-9c63-4339-bae7-ebde433aaeb4" />

and when i replaced that old md5 value to new i got some extra features

<img width="1535" height="652" alt="image" src="https://github.com/user-attachments/assets/dbed87c4-a25f-42cb-aad6-8f4ac517b4f9" />

let's click on View API Button 

<img width="1535" height="628" alt="image" src="https://github.com/user-attachments/assets/4e0cca2a-cc7f-4121-b901-d8c5525d30bb" />

and there were some more features about the Application API and it was saying that i can access only my /user/3 profile data i tried to change /3 parameter to /1

<img width="1308" height="297" alt="image" src="https://github.com/user-attachments/assets/a1ebfbe3-e115-4702-9f3a-c098271ea7f2" />

and it looks like that it was the admin account and we got his email address now we want have to get his password 
lets go back to `dashboard.php` and tried path traversal in the in `Select Theme` Parameters and change its value to any colour and then perform the path traversal there

<img width="1533" height="622" alt="image" src="https://github.com/user-attachments/assets/69efcbe4-fe3a-450a-a8aa-b685099a4980" />

the application UI changed completely then i click on View Page Source and got some thing very special 

<img width="1411" height="591" alt="image" src="https://github.com/user-attachments/assets/51039ea2-c015-4171-a799-abcb06eff2ed" />

i got the secret password make sure that you type the password without `@` Symbol
and now we have admin credentials let's login into his account 

<img width="1531" height="657" alt="image" src="https://github.com/user-attachments/assets/aafb3e3f-5c33-4c82-8c2c-60e32faee284" />

and we got the admin flag and now we are the admin and with admin priveleges there is one more feature unlocked date and time and when i observed that function i noticed that it is directly exuting this date and time as a system command 
so now i will exploit it 
<img width="1298" height="212" alt="image" src="https://github.com/user-attachments/assets/155a197b-d3ca-477b-9856-6c3e0e8e8691" />

now open the Dev Tools and locate this data option and edit it 

<img width="1317" height="275" alt="image" src="https://github.com/user-attachments/assets/bf0d8447-cc98-472c-9b49-def303d27c4d" />

there was a value parameter inside that parameter Web server is executing that what ever it contains so our task it to reteriew the /home/ubuntu/user.txt content so we can perform the command injection vulnerability attack

<img width="330" height="95" alt="image" src="https://github.com/user-attachments/assets/3dc3be3f-4980-45df-9bff-ffb719e2fa45" />

add this payload 
`
cat /home/ubuntu/user.txt
`
and make sure before entering this payload your option should be selected to time and then edit that date field and then switch to previous date option and it will execute that command 

<img width="1262" height="532" alt="image" src="https://github.com/user-attachments/assets/87fc40ee-13c1-42e5-b017-9516d7d8ffc9" />

and you got another flag 
and your lab has been solved
I Hope that this will help 
