# TryHackMe: Agent T

> **Room:** [Agent T](https://tryhackme.com/room/agentt)  
> **Platform:** TryHackMe  
> **Difficulty:** Easy  
> **Category:** Web Exploitation / Remote Code Execution / Privilege Escalation

## Introduction

This write-up covers the **Agent T** room on TryHackMe.

The main objective of the room is to identify a vulnerable PHP version, exploit a known backdoor to obtain remote command execution, and retrieve the flag from the target machine.

> **Note:** The techniques demonstrated here are performed against the intentionally vulnerable TryHackMe machine.

---

# 1. Reconnaissance

The first step is to perform an Nmap scan against the target machine.

### Nmap Command

```bash
nmap -A -T4 <LAB-MACHINE-IP> -vv -oN scan.txt
Command Breakdown
Option	Description
-A	Enables aggressive scanning features such as OS detection, version detection, script scanning, and traceroute.
-T4	Sets the timing template to 4, providing a faster scan while maintaining reasonable accuracy.
-vv	Enables very verbose output.
-oN scan.txt	Saves the scan results in normal Nmap format to scan.txt.

The scan reveals that the target is running a web server using:

PHP 8.1.0-dev

This version is particularly interesting because PHP 8.1.0-dev was distributed with a backdoor that could allow remote command execution.

2. Identifying the Vulnerability

After discovering the PHP version, searching for:

PHP 8.1.0-dev exploit

leads to a known exploit published on Exploit Database.

Exploit Database

PHP 8.1.0-dev - 'User-Agentt' Remote Code Execution

The vulnerability is associated with a malicious User-Agentt header that can be used to execute commands on vulnerable installations.

The exploit was publicly documented as:

PHP 8.1.0-dev - 'User-Agentt' Remote Code Execution

The vulnerability affects the development version:

PHP 8.1.0-dev
3. Understanding the Exploit

The exploit works by sending a specially crafted HTTP header:

User-Agentt: zerodiumsystem('<command>');

The vulnerable PHP development build processes this header and executes the supplied command.

The Python exploit provides a simple interactive interface for sending commands to the target.

Save the exploit as:

backdoor.py

For example:

nano backdoor.py

Paste the exploit code into the file and save it.

4. Making the Exploit Executable

Give the Python script executable permissions:

chmod +x backdoor.py

You can then execute it with:

python3 backdoor.py

The script asks for the target URL.

Enter the IP address of the TryHackMe machine, for example:

http://<LAB-MACHINE-IP>

If the target is vulnerable, the exploit establishes an interactive pseudo-shell.

You should see output similar to:

Interactive shell is opened on http://<LAB-MACHINE-IP>
Can't access tty; job control turned off.

At this point, commands can be executed on the target machine.

5. Finding the Flag

Now that command execution has been obtained, search the filesystem for the flag.

Use:

find / -type f -name "flag.txt"

The command searches from the root directory / for files named:

flag.txt

The search reveals:

/flag.txt
6. Reading the Flag

Read the contents of the file with:

cat /flag.txt

The flag is:

flag{4127d0530abf16d6d23973e3df8dbecb}
7. Attack Chain

The complete attack path can be summarized as:

Nmap Enumeration
       ↓
PHP 8.1.0-dev Identified
       ↓
Known PHP Backdoor Discovered
       ↓
User-Agentt RCE
       ↓
Remote Command Execution
       ↓
Filesystem Enumeration
       ↓
/flag.txt
       ↓
Flag Retrieved
8. Key Takeaways

This room demonstrates several important penetration-testing concepts:

Service enumeration using Nmap
Version identification
Vulnerability research
Exploit Database usage
Remote Code Execution (RCE)
Understanding HTTP headers as an attack surface
Post-exploitation enumeration
Linux filesystem searching
Retrieving sensitive files after gaining command execution

The most important lesson is that version enumeration is not just about identifying software. It can provide the information needed to research known vulnerabilities and determine whether a service is potentially exploitable.

References
TryHackMe - Agent T
Exploit Database - PHP 8.1.0-dev RCE
PHP Official Website
Conclusion

The Agent T room demonstrates a straightforward penetration-testing workflow:

Enumerate the target.
Identify the running service and version.
Research the discovered version for known vulnerabilities.
Exploit the vulnerable PHP development build.
Obtain remote command execution.
Enumerate the filesystem.
Retrieve the flag.

This is a good example of how reconnaissance, vulnerability research, and exploitation work together during a penetration test.

Happy hacking! 🔐
