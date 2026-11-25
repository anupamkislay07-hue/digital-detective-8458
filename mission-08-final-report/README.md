# Mission 08 — Final report and submission

## 1. Task / objective

Review the complete repository against the assignment checklist, correct anything found missing or misleading, make sure every mission has its own README in the required format and its own visible commit, and record the final status of each mission before submitting the repository link.

## 2. Work completed

Reviewed every mission folder, its README and its commit history, then made these corrections:

- **Mission 02:** added the `terminal-practice/` folder required by Task 2.2 with its two-line file and renamed copy, and answered all four reflection questions (replacing vs. appending, copying vs. moving, what `pwd` provides, why listing is useful).
- **Mission 03:** added the missing system activity snapshot, a real process list showing PIDs, absolute/relative path examples taken from the assignment folder itself, a permission listing with the owner's `rwx` letters, and the missing "User interface / shell" row.
- **Mission 06:** documented the `update-about` branch and the Pull Request workflow with its commands and status.
- **Mission 07:** replaced the concept table with all eight required concepts (LAN, MAN, WAN, DNS, router, protocol, packet switching, client–server), added real `ping`/`nslookup`/`curl` observations and the seven-step website walkthrough.
- **Mission 04:** `hello.py` now prints the exact required message, "Hello from Python".
- **All missions:** rewrote each README to the eight required headings — task/objective, work completed, commands/tools used, my understanding, difficulties faced, how I resolved them, evidence/files, commit details.
- **Privacy:** replaced the computer account name and home-directory path with `[redacted]` in every recorded output, and used only the public `example.com` results for network observations.

### Mission status

| Mission | Folder | README in required format | Key artefacts | Commit visible |
|---|---|---|---|---|
| 00 — Setup | `mission-00-setup/` | Yes | Repository structure, tool versions | Yes |
| 01 — Computer basics | `mission-01-computer-basics/` | Yes | IPOS, hardware/software, systems tables | Yes |
| 02 — Terminal | `mission-02-terminal/` | Yes | Command reference, `terminal-practice/` files | Yes |
| 03 — Operating system | `mission-03-operating-system/` | Yes | System, process, path and permission notes | Yes |
| 04 — Programs | `mission-04-programs/` | Yes | `hello.py`, compiler vs. interpreter table | Yes |
| 05 — Numbers and data | `mission-05-numbers-data/` | Yes | Conversions, verification, `number_converter.py` | Yes |
| 06 — Git and GitHub | `mission-06-git-github/` | Yes | Git glossary, branch and Pull Request record | Yes |
| 07 — Networking | `mission-07-networking/` | Yes | Concept table, observations, website steps | Yes |
| 08 — Final report | `mission-08-final-report/` | Yes | This review and status table | Yes |

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `git log --oneline` | Confirm each mission has its own commit. |
| `git status` | Confirm the working tree was clean before reviewing. |
| `git ls-tree`, `find` | Confirm every mission folder exists and contains a README. |
| `python3 mission-04-programs/hello.py` | Confirm the program still runs and prints the required message. |
| `python3 mission-05-numbers-data/number_converter.py` | Confirm the converter still runs with test inputs. |
| `grep` | Search the whole repository for the account name to remove personal information. |
| `git add`, `git commit`, `git push` | Commit and publish each corrected mission. |

## 4. My understanding

Reviewing the work at the end was more useful than writing it. Working mission by mission means gaps are invisible while you are inside one folder — a table with five rows instead of six, a task whose output was described but never recorded, a heading that was never filled in. Comparing the folder against the assignment's checklist, one line at a time, was what surfaced them.

Order also matters in Git. Each mission needs its own commit with a message that says what the work was, so the history reads as a record of the process rather than one large unexplained change. The corrections here were committed per mission for exactly that reason.

The privacy rule is part of the work, not an afterthought: Terminal output contains the account name, home path and local addresses by default, so every pasted output has to be edited before it is published.

## 5. Difficulties faced

- Finding the gaps required re-reading the assignment task by task rather than trusting the existing READMEs, because a README can describe a task while the evidence for it is missing.
- The Pull Request for Mission 06 must be opened on GitHub rather than from the Terminal, so its completion depends on an action outside the local repository.
- Deciding how much personal information could stay: my name and USN appear in the root README only because the assignment permits those details when the instructor allows them, while the computer username is never needed and had to be removed.

## 6. How I resolved them

- I worked through the assignment checklist item by item and mapped each requirement to a file, adding whatever was missing rather than rewriting what was already correct.
- I created the `update-about` branch with Git, pushed it, and opened the Pull Request from the branch to `main` on GitHub, recording its status in the Mission 06 README as required when a PR is not merged.
- I re-read the privacy rule, removed the account name from every output, and used a public example domain for all network evidence.

## 7. Evidence / files

- The mission status table in section 2.
- Every mission README, rewritten to the required headings.
- `mission-04-programs/hello.py` and `mission-05-numbers-data/number_converter.py`, both verified to run.

## 8. Commit details

Commit message: **Complete final report and verify assignment submission**

Each correction was committed separately with a mission-specific message, pushed to GitHub, and verified on the repository page. The repository URL has been submitted through the form shared by the instructor.
