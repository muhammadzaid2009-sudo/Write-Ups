# 🔐 CTF & Security Write-Ups

> Comprehensive repository containing step-by-step walkthroughs and technical documentation for CTF challenges and security labs.

![Write-Ups Count](https://img.shields.io/badge/Write--Ups-4-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Last Updated](https://img.shields.io/badge/Last%20Updated-2024-brightgreen)

---

## 📋 Overview

This repository documents my journey through various cybersecurity challenges, CTF competitions, and security labs. Each write-up provides detailed explanations of vulnerabilities, exploitation techniques, and remediation strategies for real-world security scenarios.

### ✨ Key Highlights
- **Practical Focus**: Real-world vulnerability analysis and exploitation
- **Detailed Walkthrough**: Step-by-step solutions with technical explanations
- **Multiple Platforms**: TryHackMe, Hack The Box, PortSwigger, and more
- **Auto-Updated**: Latest write-ups are automatically indexed

---

## 📚 Write-Ups

<!-- WRITEUPS_START -->

### 🟠 TryHackMe

| Challenge | Difficulty | Topics |
|-----------|-----------|--------|
| [Agent T](./TryHackMe/Agent-T.md) | Medium | Enumeration, Web Security |
| [Relevant CTF WriteUp](./TryHackMe/Relevant-CTF-WriteUp.md) | Hard | Exploitation, Privilege Escalation |
| [RootMe CTF WriteUp](./TryHackMe/RootMe-CTF-WriteUp.md) | Easy | Linux, Privilege Escalation |
| [ToolsRus CTF](./TryHackMe/ToolsRus-CTF.md) | Medium | Enumeration, Web Security |

### 🔴 Hack The Box

*Coming soon...*

### 🟡 PortSwigger Web Security Academy

*Coming soon...*

### 🟢 Other Labs

*Coming soon...*

<!-- WRITEUPS_END -->

---

## 🏷️ Topics Covered

```
Enumeration              Privilege Escalation   Web Security           
Exploitation           Network Security        Linux Security         
Cryptography           Password Cracking       SQL Injection          
Command Injection      Cross-Site Scripting    API Security           
Authentication         Authorization          Malware Analysis       
```

---

## 🛠️ Platforms

| Platform | Status |
|----------|--------|
| 🟠 **TryHackMe** | 4 Write-Ups |
| 🔴 **Hack The Box** | In Progress |
| 🟡 **PortSwigger Web Security Academy** | In Progress |
| 🟢 **Other Authorized Labs** | Available |

---

## 📖 How to Use This Repository

1. **Browse by Platform**: Navigate to the platform-specific folders
2. **Search by Topic**: Use GitHub's search feature to find write-ups by vulnerability type
3. **Read the Walkthroughs**: Each write-up includes:
   - Challenge description
   - Enumeration process
   - Vulnerability analysis
   - Exploitation steps
   - Remediation advice

---

## 🔄 Auto-Update Feature

This repository is designed to automatically index new write-ups as you add them!

### How It Works
1. Add a new write-up file to your platform folder (e.g., `TryHackMe/New-Challenge.md`)
2. Push to the repository
3. A GitHub Action automatically scans and updates the README
4. Your new write-up appears in the index!

### Setting Up Auto-Updates
To enable automatic README updates with a GitHub Action:

1. Create `.github/workflows/auto-update-readme.yml` with this content:
```yaml
name: Auto-Update README

on:
  push:
    branches:
      - main
    paths:
      - '**.md'
      - '!README.md'
  workflow_dispatch:

jobs:
  update-readme:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v3
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: python3 .github/scripts/update_readme.py
      - run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add README.md
          if ! git diff --quiet; then
            git commit -m "docs: auto-update write-ups list"
            git push
          fi
```

2. Add the update script at `.github/scripts/update_readme.py` (see the setup guide below)

---

## 💡 Best Practices for Write-Ups

### File Structure
```
Write-Ups/
├── TryHackMe/
│   ├── Agent-T.md
│   ├── RootMe-CTF-WriteUp.md
│   └── ToolsRus-CTF.md
├── HackTheBox/
│   └── Challenge-Name.md
├── PortSwigger/
│   └── Lab-Name.md
└── OtherLabs/
    └── Lab-Name.md
```

### Write-Up Template

Add this metadata at the top of each write-up for better organization:

```markdown
# Challenge Name

- **Platform**: TryHackMe
- **Difficulty**: Medium
- **Topics**: Enumeration, Web Security
- **Date Completed**: YYYY-MM-DD
- **Tools Used**: nmap, Burp Suite, etc.

## Description
[Challenge overview and objectives]

## Enumeration
[Initial reconnaissance and scanning]

## Exploitation
[Vulnerability discovery and exploitation]

## Privilege Escalation
[Steps to gain higher privileges]

## Lessons Learned
[Key takeaways and remediation]
```

### File Naming Convention
- Use **hyphens** to separate words: `SQL-Injection-Lab.md`
- Be descriptive but concise: `Challenge-Name-CTF.md`
- Avoid special characters: Use only alphanumeric and hyphens
- Examples:
  - ✅ `Agent-Sudor.md`
  - ✅ `SQL-Injection-Basics.md`
  - ❌ `Agent Sudor.md`
  - ❌ `SQL@Injection#Basics.md`

---

## ⚖️ Disclaimer

All activities documented in this repository are intended for **authorized educational environments only**, including:
- Official CTF competitions
- Authorized security labs and training programs
- Personal authorized testing environments
- Academic coursework with proper authorization

**⚠️ Unauthorized access to computer systems is illegal.** Always obtain proper authorization before conducting any security testing.

---

## 📞 Connect With Me

- 💼 **LinkedIn**: [Muhammad Zaid](https://www.linkedin.com/in/muhammad-zaid2009/)
- 🎯 **TryHackMe**: [muhammadzaid2009](https://tryhackme.com/p/muhammadzaid2009)
- ✍️ **Medium**: [@muhammadzaid2009](https://medium.com/@muhammadzaid2009)
- 🐙 **GitHub**: [muhammadzaid2009-sudo](https://github.com/muhammadzaid2009-sudo)

---

## 📜 License

This repository is licensed under the **MIT License** - see the [LICENSE](./LICENSE) file for details.

---

<div align="center">

**⭐ If you find these write-ups helpful, please consider giving this repo a star!**

*Auto-updated by GitHub Actions | Last Update: 2024*

</div>