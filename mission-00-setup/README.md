# Mission 00 — Setup and workspace

## 1. Task / objective

Create a public GitHub repository named with the assignment name and the last four digits of my USN, build the full mission folder structure with a README in every folder, verify that the required tools are installed, write the root README, and publish the repository so later missions have somewhere to be committed.

## 2. Work completed

- Created the local project folder `digital-detective-8458`, matching the repository name exactly.
- Created one folder per mission (`mission-00-setup` through `mission-08-final-report`) plus `evidence/`, each mission folder containing its own `README.md`.
- Wrote the root `README.md` with the project title, an introduction, a mission index linking every mission README, the tools and versions in use, and the repository structure.
- Verified Python 3 and Git are installed and recorded their versions.
- Initialised Git, made the initial commit and published the repository to GitHub as a public repository with the same name.

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `mkdir` | Create the mission folders and `evidence/`. |
| `touch README.md` | Create the empty Markdown files that were then filled in. |
| `python3 --version` | Confirm Python 3 is installed and record its version. |
| `git --version` | Confirm Git is installed and record its version. |
| `sw_vers`, `uname -srm` | Record the operating system and architecture. |
| `git init`, `git add`, `git commit` | Start version control and save the first snapshot. |
| `git remote add origin`, `git push` | Connect the local folder to GitHub and publish it. |
| VS Code / text editor | Write the Markdown files. |

## 4. My understanding

A **repository** is a project folder whose entire history is tracked: every saved version (commit), the messages describing them, and the branches they belong to all live inside the hidden `.git` folder. That means earlier states can be inspected or restored instead of relying on copies named `final_v2`, and a remote copy on GitHub makes the work backed up and reviewable by someone else.

The folder structure is organised by mission because each mission is graded separately and must be committed separately. One folder per mission keeps the work, its evidence and its README in one predictable place, gives every mission its own commit that is easy to find in the history, and matches the structure the assignment asks for, so an instructor can navigate straight to the mission they want to review.

## 5. Difficulties faced

- The repository name has to match the assignment naming rule exactly, including the last four USN digits, so the local folder name and the GitHub repository name had to be identical.
- GitHub offers to add a README when creating a repository, which would have conflicted with the README I had already written locally.
- Getting the local folder connected to the remote and pushing the first commit took a couple of attempts because the default branch name had to match.

## 6. How I resolved them

- I used the assignment naming rule (`digital-detective-` followed by the USN digits) for both the folder and the repository, and checked them side by side.
- I created the GitHub repository empty, without a README, `.gitignore` or licence, so the first push could not conflict.
- I confirmed the branch name before pushing and verified on GitHub that the folders and the initial commit were visible.

## 7. Evidence / files

- `README.md` — root overview, mission index and structure.
- One `README.md` in each of the nine mission folders.
- `evidence/` — folder reserved for privacy-safe screenshots and outputs.

## 8. Commit details

Commit message: **Set up Digital Detective mission structure**

Pushed to GitHub and confirmed on the repository page that the folder structure and the commit are visible.
