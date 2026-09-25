#!/usr/bin/env python3
"""
Auto-update README.md with discovered write-ups
Scans platform directories and updates the WRITEUPS section
"""

import os
import re
from pathlib import Path
from collections import defaultdict

# Get the repo root
REPO_ROOT = Path(__file__).parent.parent.parent

# Platforms to scan
PLATFORMS = ['TryHackMe', 'HackTheBox', 'PortSwigger', 'OtherLabs']

# Emoji mapping for platforms
PLATFORM_EMOJI = {
    'TryHackMe': '🟠',
    'HackTheBox': '🔴',
    'PortSwigger': '🟡',
    'OtherLabs': '🟢',
}

def get_writeups_by_platform():
    """Scan directories and collect write-ups organized by platform"""
    writeups = defaultdict(list)
    
    for platform in PLATFORMS:
        platform_dir = REPO_ROOT / platform
        
        if not platform_dir.exists():
            continue
        
        # Find all markdown files in platform directory
        md_files = sorted(platform_dir.glob('*.md'))
        
        for md_file in md_files:
            # Get relative path from repo root
            rel_path = md_file.relative_to(REPO_ROOT)
            
            # Extract challenge name from filename
            challenge_name = md_file.stem.replace('-', ' ')
            
            # Try to extract metadata from file
            difficulty = "Medium"  # default
            topics = "Security"    # default
            
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Look for metadata in markdown
                    difficulty_match = re.search(r'[Dd]ifficulty[:\s]+([\w]+)', content)
                    if difficulty_match:
                        difficulty = difficulty_match.group(1).capitalize()
                    
                    topics_match = re.search(r'[Tt]opics?[:\s]+([^\n]+)', content)
                    if topics_match:
                        topics = topics_match.group(1).strip()
            except:
                pass
            
            writeups[platform].append({
                'name': challenge_name,
                'path': str(rel_path),
                'difficulty': difficulty,
                'topics': topics
            })
    
    return writeups

def generate_writeup_section(writeups):
    """Generate the write-ups section content"""
    lines = []
    
    for platform in PLATFORMS:
        if platform not in writeups or not writeups[platform]:
            continue
        
        emoji = PLATFORM_EMOJI.get(platform, '🔷')
        lines.append(f"### {emoji} {platform}\n")
        lines.append("| Challenge | Difficulty | Topics |")
        lines.append("|-----------|-----------|--------|")
        
        for writeup in writeups[platform]:
            challenge_link = f"[{writeup['name']}](./{writeup['path']})"
            line = f"| {challenge_link} | {writeup['difficulty']} | {writeup['topics']} |"
            lines.append(line)
        
        lines.append("")
    
    # Add section for platforms with no write-ups yet
    for platform in PLATFORMS:
        if platform not in writeups or not writeups[platform]:
            emoji = PLATFORM_EMOJI.get(platform, '🔷')
            lines.append(f"### {emoji} {platform}\n")
            lines.append("*Coming soon...*\n")
    
    return '\n'.join(lines)

def update_readme():
    """Update the README.md file with discovered write-ups"""
    readme_path = REPO_ROOT / 'README.md'
    
    if not readme_path.exists():
        print("❌ README.md not found!")
        return False
    
    # Read current README
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get write-ups
    writeups = get_writeups_by_platform()
    
    # Generate new write-ups section
    new_section = generate_writeup_section(writeups)
    
    # Replace content between markers
    pattern = r'(<!-- WRITEUPS_START -->)(.*?)(<!-- WRITEUPS_END -->)'
    new_content = re.sub(
        pattern,
        rf'\1\n{new_section}\n\3',
        content,
        flags=re.DOTALL
    )
    
    # Write back if changed
    if new_content != content:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        # Count write-ups for badge
        total_writeups = sum(len(v) for v in writeups.values())
        print(f"✅ README updated! Found {total_writeups} write-ups across {len(writeups)} platforms.")
        return True
    else:
        print("ℹ️  No changes needed. README is already up to date.")
        return False

if __name__ == '__main__':
    update_readme()
