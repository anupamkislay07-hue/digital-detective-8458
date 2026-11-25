# Evidence

Supporting output for the nine missions. Every mission README already quotes its commands and
results in text; this folder keeps a captured copy so the evidence can be opened directly.

The assignment allows "selected output" as evidence, so each file here is real terminal output
recorded on the computer, with personal details such as the account name and home-directory path
replaced by `[redacted]`.

## Captured output

| File | Mission | What it shows |
|---|---|---|
| `mission-00-setup/tool-versions.txt` | 00 | `python3 --version`, `git --version`, `brew --version` |
| `mission-02-terminal/terminal-session.txt` | 02 | `pwd`, `mkdir`, `touch`, `cp`, `mv`, `ls -l`, `echo >` vs `echo >>`, `cat`, `stat` permission string |
| `mission-03-operating-system/system-evidence.txt` | 03 | `sw_vers`, `uname -m`, `df -h /`, `ps -ax -o pid,comm`, `stat -f '%Sp %N'` |
| `mission-04-programs/hello-output.txt` | 04 | `python3 hello.py` printing `Hello from Python` |
| `mission-05-numbers-data/converter-runs.txt` | 05 | `number_converter.py` run with 23, 255 and 7, plus `bin()`, `int()`, `hex()`, `ord()` results |
| `mission-06-git-github/git-history.txt` | 06 | `git log --oneline --graph`, `git branch -a`, `git status --short --branch` |
| `mission-07-networking/connectivity.txt` | 07 | `ping`, `nslookup` and `curl -I` for the public example domain |

## Screenshots

Screenshots are optional for this folder. The versions captured on the computer showed the account
name and device name in the prompt, which the assignment forbids, so the text output above is used
instead. If privacy-safe screenshots are taken later, save them in the matching mission folder
(e.g. `mission-02-terminal/`) using names such as `01-terminal-basics.png`, and add them to this
table.

## Rules that were applied

- No computer account name, device name, or personal IP address anywhere in these files.
- Network checks use only the public example domain, never a real site or a real local address.
- Output is copied as it was produced, not rewritten; only identifying paths are replaced with `[redacted]`.
