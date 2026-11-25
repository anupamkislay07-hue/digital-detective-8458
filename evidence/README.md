# Evidence — screenshots

This folder holds privacy-safe screenshots of the commands and output described in
each mission README. Every mission README already quotes the same output as text, so
these screenshots are supporting proof, not the only evidence.

Screenshots are grouped by mission. Each cell in the table names the exact file to save
in that folder.

## What to capture

| Mission | File to save | What the screenshot must show |
|---|---|---|
| 02 — Terminal | `mission-02-terminal/01-terminal-basics.png` | The terminal with `pwd`, `ls -lah`, `whoami`-free flag comparison (`ls -l` vs `ls -lah`) |
| 02 — Terminal | `mission-02-terminal/02-file-operations.png` | `cp`, `mv`, `cat` of `terminal-practice/notes.txt`, and the appended second line plus `notes-copy.txt` |
| 03 — Operating system | `mission-03-operating-system/01-system-and-storage.png` | macOS version (`sw_vers`) and free disk space (`df -h`) |
| 03 — Operating system | `mission-03-operating-system/02-processes.png` | `top -l 1` snapshot and `ps -ax -o pid,comm` rows with a few PIDs |
| 03 — Operating system | `mission-03-operating-system/03-permissions.png` | `ls -l` output showing the `-rw-r--r--` permission string |
| 04 — Programs | `mission-04-programs/01-hello-python.png` | `python3 hello.py` printing `Hello from Python` |
| 05 — Numbers and data | `mission-05-numbers-data/01-converter.png` | `python3 number_converter.py` run with three different values |
| 05 — Numbers and data | `mission-05-numbers-data/02-python-expressions.png` | Python `bin()`, `hex()`, `int(..., 2)`, `int(..., 16)` and `ord()` results |
| 06 — Git and GitHub | `mission-06-git-github/01-git-history.png` | `git log --oneline --graph`, `git branch` and `git status` |
| 06 — Git and GitHub | `mission-06-git-github/02-pull-request-merged.png` | The GitHub page of Pull Request #1 showing the **Merged** state |
| 07 — Networking | `mission-07-networking/01-connectivity.png` | `ping`, `nslookup` and `curl` output for the public example domain |

## Rules for every screenshot

- **No computer account name.** Hide the name that appears before `~` or `$` in the prompt.
- **No device name.** Blur the host name shown next to the prompt or in `sw_vers`/`hostname` output.
- **No IP address or Wi-Fi name.** Local addresses and network names must not be visible.
- Network evidence uses a public example domain only, never a real site or a real address.
- Keep the command and its output readable — a cropped, unreadable screenshot proves nothing.

## Status

None of the screenshots above have been added yet. All eleven entries are outstanding;
drop the image files into the matching folder with the names in the table and they will be
committed with the rest of the repository.
