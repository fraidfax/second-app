# second-app
This is a demo password generator program with loading effect.
My basic tutorial (further update)
1. The Tools
git: The engine installed on your computer that tracks file versions. You need this.
gh: The GitHub CLI. It is optional. You can do everything gh does by using the GitHub website instead.
2. The Core Concepts (The 3 Zones)
Before code is saved history, it moves through three stages:
Working Directory: The files you are currently editing.
Staging Area (git add): The "Shopping Cart." You pick what you want to save.
Repository (git commit): The "Purchase History." A permanent snapshot saved to the database.
3. The Professional Workflow ("The Golden Rule")
Never work directly on the main branch after the initial setup.
Main Branch: This is your stable "Trunk." It should always work.
Feature Branches: Where you do work. You create a copy of main, break things, fix them, and save them.
Pull Request (PR): The bridge between the branch and main. This happens on the Website, not the terminal.
4. Your Command Cheat Sheet
Phase 1: First Time Setup (Creating the Base)
git init → Turn the folder into a repo.
git add . → Stage all files (Fixes "Untracked files" error).
git commit -m "msg" → Save the snapshot.
git branch -M main → Rename default branch to standard main.
git remote add origin <URL> → Connect to GitHub.
git push -u origin main → Upload to GitHub and remember the connection.
If you see "Rejected/Fetch First": Use git push -f origin main to overwrite the server's empty README.
Phase 2: Daily Routine (Adding Features)
Create new space: git checkout -b feature-login
Work: Edit files.
Stage: git add .
Save: git commit -m "Added login"
Upload: git push -u origin feature-login
Merge: Go to GitHub.com -> Click "Compare & pull request" -> Merge.
5. Key "Why" Questions You Asked
Why use -u?
It stands for "Upstream." It saves the link between your PC and GitHub so next time you can just type git push without typing the full name.
Why no automatic Pull Request?
git push only saves files. A Pull Request is a human administrative step to ask for a code review. You must do this manually on the browser.
Why master vs main?
master is the old default name. main is the new standard. We rename it to avoid confusion because GitHub uses main.