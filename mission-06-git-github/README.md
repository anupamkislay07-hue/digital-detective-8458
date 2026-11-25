# Mission 06 – Git & GitHub

## 1. Mission Objective

Understand how Git tracks changes, learn the core commands used in version control workflows, and distinguish between local and remote repositories.

---

## 2. Task 6.1 – Git Command Reference

| Command | What It Does |
|---|---|
| `git init` | Turns a regular folder on your computer into a Git repository by creating a hidden `.git` folder to start tracking changes. |
| `git add` | Stages specific changes (or all changes with `.`) so they're lined up and ready to be saved in the next snapshot. |
| `git commit` | Saves a permanent snapshot of your staged changes in your local history along with a short message explaining what changed. |
| `git log` | Shows the history of commits—commit IDs, messages, dates, and authors—so you can see how the project evolved. |
| `git branch` | Lets you view, create, or switch between separate lines of work (like a `main` branch or a feature/mission branch) without messing up working code. |
| `git push` | Uploads your local commits from your Mac up to a remote repository (like GitHub) so they're backed up and shared. |

---

## 3. Task 6.2 – Local vs. Remote Repository

A **local repository** lives right inside your project folder on your Mac—it's fast, works offline, and is where you actively edit files, stage changes, and make commits.

A **remote repository** (like on GitHub) is hosted on a server online, acting as a cloud backup, a sync point across machines, and a place to share or collaborate on code.

---

## 4. Task 6.3 – Why Version Control?

Working through missions bit by bit across different tasks and scripts makes it easy to tweak something or make a messy edit—having commits means you always have clear checkpoints of what worked at each stage instead of relying on duplicated files like `script_v1`, `script_v2`, and `script_final`.

---

## 5. Reflection

The staging step (`git add` before `git commit`) felt clearest once I saw it as packing a box before sealing it—though keeping track of what's staged, committed, and actually pushed to GitHub can still trip you up if you rush.
