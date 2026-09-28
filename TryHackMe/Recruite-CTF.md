# 🛡️ TryHackMe: Recruit-CTF

A hands-on web application security challenge focused on **reconnaissance, directory enumeration, Local File Inclusion (LFI), credential disclosure, SQL injection, and application privilege escalation**.

> ⚠️ **Disclaimer:** This writeup is based on an authorized TryHackMe lab environment and is intended for educational purposes.

---

## 📋 Table of Contents

* Overview.
* Attack Path.
* Reconnaissance.
* Web Application Enumeration
* Directory Enumeration
* Application Information Discovery
* Local File Inclusion
* Authenticated Access
* SQL Injection
* Database Enumeration
* Administrator Access
* Vulnerability Analysis
* Lessons Learned
* Further Investigation
* Conclusion

---

## 🎯 Overview

| Information            | Details                                   |
| ---------------------- | ----------------------------------------- |
| **Platform**           | TryHackMe                                 |
| **Challenge**          | Recruit-CTF                               |
| **Category**           | Web Application Security                  |
| **Target**             | `10.112.173.245`                          |
| **Primary Techniques** | LFI, Credential Disclosure, SQL Injection |

### Objective

The objective was to enumerate the target, identify vulnerabilities in the web application, obtain initial authenticated access, and ultimately gain administrator access.

---

# 🔗 Attack Path

The compromise followed this attack chain:

```text
Network Reconnaissance
        ↓
Web Application Enumeration
        ↓
Directory Discovery
        ↓
Access API Discovery
        ↓
Local File Inclusion
        ↓
Configuration File Disclosure
        ↓
HR Credentials
        ↓
Authenticated Access
        ↓
SQL Injection
        ↓
Database Enumeration
        ↓
Admin Credentials
        ↓
Administrator Access
```

### Key Vulnerabilities

* Local File Inclusion
* Sensitive credential disclosure
* SQL Injection
* Insecure credential storage/exposure

---

# 🔎 Reconnaissance

## Nmap Scan

I started by identifying the services exposed by the target.

```bash
nmap -A -T4 10.112.173.245 -vv -oN scan.txt
```

### Relevant Results

| Port     | Service | Version         |
| -------- | ------- | --------------- |
| `22/tcp` | SSH     | OpenSSH 8.2p1   |
| `53/tcp` | DNS     | ISC BIND 9.16.1 |
| `80/tcp` | HTTP    | Apache 2.4.41   |

> **Note:** Only the relevant results are shown here. The complete scan output was saved to `scan.txt`.

### Analysis

The HTTP service on port `80` was particularly interesting because the challenge focused on web application security.

I therefore prioritized the web application for further enumeration.

---

# 🌐 Web Application Enumeration

Opening the application in a browser presented a login interface.

I first inspected the page source for potentially useful information such as:

* Hidden endpoints
* HTML comments
* Hardcoded credentials
* JavaScript references
* Interesting parameters

No immediately useful information was identified.

Since the visible interface exposed limited functionality, I moved to directory enumeration.

---

# 📁 Directory Enumeration

I used Gobuster to identify directories and resources that were not directly linked from the main application.

```bash
gobuster dir \
-u http://10.112.173.245 \
-w /usr/share/wordlists/dirb/common.txt \
-o recon.txt
```

### Results

The enumeration revealed several interesting directories.

I manually investigated the discovered endpoints rather than assuming that every result was useful.

One of the interesting locations was:

```text
/mail
```

This provided additional application functionality to investigate.

---

# 🔍 Application Information Discovery

While investigating the discovered functionality, I identified an HR account:

```text
Username: hr
```

The application also exposed an **Access API** feature.

At this point, I examined how the API handled user-controlled file paths.

### Why This Was Interesting

Functionality that allows users to specify a file to retrieve can potentially introduce **Local File Inclusion (LFI)** or local file disclosure if the application does not properly validate the supplied path.

This led me to test whether the API could be manipulated to access files stored on the server.

---

# 📂 Local File Inclusion

## Identifying the Vulnerability

The application accepted a file parameter through the API.

I tested whether the parameter could be manipulated to retrieve a local file from the target.

The following request successfully accessed a local configuration file:

```text
http://10.112.173.245/file.php?cv=file:///var/www/html/config.php
```

### Result

The application disclosed the contents of:

```text
/var/www/html/config.php
```

### Why This Mattered

Configuration files frequently contain sensitive application information, including:

* Database credentials
* Application secrets
* Service credentials
* Configuration parameters

In this case, the disclosed configuration exposed credentials for the HR account.

```text
Username: hr
Password: hrpassword123
```

> 🔑 **Finding:** The LFI vulnerability resulted in sensitive credential disclosure.

---

# 🔐 Authenticated Access

Using the credentials obtained from the exposed configuration file, I authenticated to the application as the HR user.

```text
Username: hr
Password: hrpassword123
```

This provided access to functionality that was not available from the unauthenticated interface.

### Next Objective

The next step was to determine whether the authenticated application contained additional vulnerabilities that could allow access to a higher-privileged account.

I therefore continued enumerating the authenticated functionality.

---

# 💉 SQL Injection

## Identifying the Injection Point

While investigating the authenticated application, I identified a search functionality that accepted user-controlled input.

I initially tested the parameter manually by modifying the request and observing how the application responded.

A single quote was added to the parameter:

```text
'
```

The resulting change in application behavior suggested that the input was being incorporated into a backend SQL query.

### Burp Suite

I captured the request using Burp Suite and saved it as:

```text
req.txt
```

The saved request could then be supplied directly to SQLMap for further database enumeration.

> **Finding:** The search functionality appeared vulnerable to SQL injection.

---

# 🗄️ Database Enumeration

## Enumerating Databases

I used the captured request with SQLMap:

```bash
sqlmap -r req.txt --dbs
```

The application exposed the following relevant database:

```text
recruit_db
```

---

## Enumerating Tables

I then enumerated the tables within `recruit_db`:

```bash
sqlmap -r req.txt -D recruit_db --tables
```

The `users` table was particularly interesting because it was likely to contain application account information.

---

## Dumping the Users Table

I enumerated the contents of the `users` table:

```bash
sqlmap -r req.txt -D recruit_db -T users --dump
```

The table contained administrator credentials:

```text
Username: admin
Password: admin@001admin
```

> 🔑 **Finding:** SQL injection allowed database enumeration and extraction of administrator credentials.

---

# 👑 Administrator Access

Using the discovered administrator credentials, I returned to the application's login page and authenticated as the administrator.

```text
Username: admin
Password: admin@001admin
```

This provided the required administrator-level access and allowed me to retrieve the final flag.

> ✅ **Objective completed:** Administrator access was successfully obtained.

---

# 🛡️ Vulnerability Analysis

## 1. Local File Inclusion

**Type:** Local File Inclusion / Local File Disclosure

### Root Cause

The application allowed a user-controlled file path to be supplied to the server without sufficient validation or restriction.

### Impact

An attacker could potentially access sensitive files stored on the server.

In this challenge, the vulnerability resulted in the disclosure of a configuration file containing valid credentials.

### Recommended Remediation

* Avoid accepting arbitrary file paths from users.
* Use an allowlist of permitted files where file retrieval is required.
* Validate and canonicalize file paths.
* Prevent access to sensitive application configuration files.
* Store secrets outside web-accessible locations.

---

## 2. SQL Injection

**Type:** SQL Injection

### Root Cause

The application's search functionality incorporated user-controlled input into a database query without sufficient protection against SQL injection.

### Impact

The vulnerability allowed database enumeration and extraction of sensitive account information.

An attacker could potentially:

* Enumerate databases
* Enumerate tables
* Read sensitive records
* Extract credentials
* Compromise additional application accounts

### Recommended Remediation

* Use parameterized queries / prepared statements.
* Avoid dynamically constructing SQL queries with untrusted input.
* Apply strict input validation where appropriate.
* Restrict database account privileges.
* Avoid storing passwords in plaintext.

---

# 📊 Findings Summary

|  # | Finding              | Category               | Impact                           |
| -: | -------------------- | ---------------------- | -------------------------------- |
|  1 | Local File Inclusion | File Handling          | Configuration file disclosure    |
|  2 | Credential Exposure  | Information Disclosure | HR account compromise            |
|  3 | SQL Injection        | Injection              | Database compromise              |
|  4 | Credential Exposure  | Sensitive Data         | Administrator account compromise |

---

# 📚 Lessons Learned

## Technical Lessons

* Web applications should be thoroughly enumerated before exploitation.
* Exposed APIs can introduce additional attack surfaces that are not obvious from the main interface.
* Configuration files can contain highly sensitive credentials.
* User-controlled file paths should always be treated as untrusted input.
* SQL injection can expose application data far beyond the initially vulnerable parameter.
* Credentials discovered during one phase of an assessment can become the starting point for the next phase.

## Methodology Lessons

One of the most important lessons from this machine was that the vulnerabilities were connected.

The initial foothold did not directly provide administrator access.

Instead, information obtained during one stage guided the next stage:

```text
Directory Enumeration
        ↓
API Discovery
        ↓
LFI
        ↓
Credential Disclosure
        ↓
HR Account
        ↓
SQL Injection
        ↓
Database Enumeration
        ↓
Administrator Credentials
        ↓
Administrator Access
```

This demonstrates why enumeration should be treated as an **iterative process** rather than a single step performed only at the beginning of an assessment.

---

# 🔬 Further Investigation

If this were an authorized real-world assessment rather than a controlled lab, I would also investigate:

* Whether the LFI could access files outside the web application's directory.
* Whether other sensitive configuration files were exposed.
* Whether the disclosed credentials were reused elsewhere.
* Whether the SQL injection affected additional application functionality.
* Whether authorization controls properly separated HR and administrator roles.
* Whether sensitive credentials were securely stored in the database.
* Whether other API endpoints exposed similar file-handling functionality.

---

# 📝 Conclusion

Recruit-CTF demonstrated how multiple weaknesses can be chained together to compromise a web application.

The attack began with reconnaissance and directory enumeration, which led to the discovery of an Access API. Testing this functionality revealed a Local File Inclusion vulnerability that exposed a configuration file containing valid HR credentials.

After obtaining authenticated access, further application enumeration revealed a SQL injection vulnerability. SQLMap was then used to enumerate the database and extract administrator credentials, ultimately leading to administrator access.

The key lesson was not a particular tool or payload, but the process of continuously using information discovered during enumeration to determine the next investigation step.

### Final Attack Chain

**LFI → Credential Disclosure → HR Access → SQL Injection → Database Enumeration → Administrator Credentials → Administrator Access**

---

# 🛠️ Tools Used

* [Nmap](https://nmap.org/)
* [Gobuster](https://github.com/OJ/gobuster)
* [Burp Suite](https://portswigger.net/burp)
* [SQLMap](https://sqlmap.org/)

---

# 🔗 References

* [TryHackMe - Recruit-CTF](https://tryhackme.com/)
* [OWASP - Local File Inclusion](https://owasp.org/www-community/attacks/Path_Traversal)
* [OWASP - SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)

---

## 👤 Author

**Muhammad Zaid**

* [GitHub](https://github.com/muhammadzaid2009-sudo)
* [LinkedIn](https://www.linkedin.com/in/muhammad-zaid2009/)
* [TryHackMe](https://tryhackme.com/p/muhammadzaid2009)
* [Medium](https://medium.com/@muhammadzaid2009)
