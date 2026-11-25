# Mission 02 — Terminal and file management

## 1. Task / objective

Become comfortable using the command-line interface (CLI) instead of the mouse: find out where I am, list and inspect folders, create, copy, move, rename and read files safely, understand how flags and pipes change command behaviour, and explain what a package manager does. All practice was done inside my own assignment repository, with no administrator privileges.

## 2. Work completed

### Task 2.1 — Basic Terminal operations

| Operation | Command | What it does | What I observed |
|---|---|---|---|
| Current-directory display | `pwd` | Prints the full path of the folder I am working in. | Printed the complete path ending in `digital-detective-8458`, so I always knew exactly which folder my next command would affect. |
| Directory listing | `ls` | Lists the names of files and folders in the current location. | Showed `README.md`, `evidence` and all `mission-0x-*` folders. |
| Detailed listing | `ls -l` | Lists entries with permissions, owner, size and modification date. | Each line began with a permission string such as `-rw-r--r--`, followed by owner, size and date. |
| Change directory | `cd ..` | Moves to the parent folder. | After `cd ..` the `pwd` output dropped the last folder name, confirming I had moved one level up. |
| Create directory | `mkdir terminal-practice` | Creates a new empty folder. | The folder appeared in the next `ls` listing. |
| Create empty file | `touch notes.txt` | Creates an empty file (or updates its timestamp if it exists). | A zero-byte file appeared inside `terminal-practice`. |
| Copy file | `cp notes.txt notes-backup.txt` | Duplicates a file under a new name, keeping the original. | Two files with identical contents existed side by side. |
| Move / rename file | `mv notes-backup.txt notes-copy.txt` | Moves a file to a new location, or renames it if the location stays the same. | `notes-backup.txt` disappeared and `notes-copy.txt` took its place; contents unchanged. |
| Display file contents | `cat notes.txt` | Prints the whole contents of a file to the screen. | Both lines of the practice file were printed in order. |

### Task 2.2 — Safe file-management practice

Inside my repository I created `mission-02-terminal/terminal-practice/` and worked only inside it:

1. `touch notes.txt` created the empty file.
2. One line was written into it, then a second line was appended **without removing the first line**.
3. `cat notes.txt` confirmed both lines were present.
4. `cp` made a backup copy which `mv` then renamed to `notes-copy.txt`.

Files kept as evidence:

- `terminal-practice/notes.txt` — two lines, written by appending the second.
- `terminal-practice/notes-copy.txt` — the renamed backup copy.

**Answers to the four questions**

1. **Replacing vs. appending.** Using `>` **replaces** a file's contents: the old text is wiped and the file is rewritten from scratch. Using `>>` **appends**: the new text is added after whatever is already there, and nothing is lost.
2. **Copying vs. moving.** `cp` leaves the original in place and creates a second, independent file, so two copies exist. `mv` relocates the file — or renames it in the same folder — so only one copy exists afterwards.
3. **What the current-directory display provides.** `pwd` tells me the absolute path of the folder I am inside. That matters because relative commands like `cp` and `rm` act on the current location, so knowing it prevents me from creating or deleting files in the wrong place.
4. **Why a directory listing is useful.** It shows what actually exists before I act — the exact file names, which are folders, and, with `-l`, their size and permissions. It is how I confirm that a `mkdir`, `cp` or `mv` really did what I intended.

### Task 2.3 — Flags and pipes

**Flags.** I compared a plain `ls` with `ls -lah`:

- `-l` switches to the long format: permissions, owner, size, date.
- `-a` also shows hidden "dot" files such as `.git`.
- `-h` makes sizes human-readable (`448B`, `2.0K`) instead of raw bytes.

The listing itself did not change — the same entries appeared — but each entry carried far more information, and hidden entries became visible.

**Pipes.** I sent a detailed listing into `head`:

```bash
ls -lah | head -n 3
```

Observed output (usernames replaced with `[redacted]`):

```text
total 8
drwxr-xr-x@ 14 [redacted]  staff   448B Nov 26 01:05 .
drwxr-xr-x@  5 [redacted]  staff   160B Nov 26 01:05 ..
```

The pipe symbol `|` connects two commands: the **left** side (`ls -lah`) produces the output, and the **right** side (`head -n 3`) receives that output as its input and keeps only the first three lines. Nothing is written to a temporary file — the data flows straight from one program to the next, which is how small commands are combined into a single useful result.

### Task 2.4 — Package managers (Homebrew)

- `which brew` → `/opt/homebrew/bin/brew`
- `brew --version` → `Homebrew 7.0.16`
- `brew list` (sample) → `coreutils`, `ffmpeg`, `gcc`, `gh`, `git`, `openssl@3`, `python@3.14`, `sqlite`

Nothing was installed or removed for this assignment; only the version and package list were inspected.

A package manager is useful because it installs, updates and removes software from one trusted source instead of hunting for installers on different websites. It also tracks dependencies, so a tool that needs a library gets it automatically, and one command keeps everything current. Because it records what it installed, removing software cleanly is possible too.

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `pwd` | Show the full path of the current folder. |
| `ls`, `ls -l`, `ls -lah` | List entries; long format; long format with hidden files and readable sizes. |
| `cd`, `cd ..` | Change directory, including moving to the parent folder. |
| `mkdir` | Create a folder (`terminal-practice`). |
| `touch` | Create an empty file. |
| `cp` | Copy a file. |
| `mv` | Rename or move a file. |
| `cat` | Print a file's contents. |
| `>`, `>>` | Redirect output into a file, replacing it or appending to it. |
| `\|`, `head -n 3` | Pipe output into another command and show only the first lines. |
| `which`, `brew --version`, `brew list` | Inspect the Homebrew package manager without changing anything. |
| macOS Terminal | The CLI used for every operation above. |

## 4. My understanding

The Terminal is the same file system as Finder, addressed by typed commands instead of clicks. Every command works relative to a current directory, which is why `pwd`, `ls` and `cd` come first: they establish where I am and what is there.

Flags are options that change how a command behaves without changing what it acts on — `ls -lah` listed the same folder, just in far more detail. Pipes are different: they connect commands so the output of one becomes the input of the next. That composition is the real strength of the CLI, because dozens of small single-purpose commands can be chained into one step.

Redirection is the most dangerous part I practised. `>` destroys existing content silently, while `>>` adds to it — the difference between losing work and extending it. Copying and moving are likewise easy to confuse: `cp` duplicates, `mv` relocates.

Finally, package managers keep software consistent. Homebrew knows which tools are installed and where, which removes the guesswork of manual installers.

## 5. Difficulties faced

- `ls -lah` initially printed a `total 8` line and `.`/`..` entries that I did not expect, which made the output look cluttered.
- I had to be careful with `>` because it silently overwrote a file during an early attempt at adding a second line.
- Remembering the difference between `cp` and `mv` when a rename was needed, rather than a duplicate.

## 6. How I resolved them

- I learned that `total` is the disk usage of the listed blocks and that `.`/`..` are the current and parent directories, so the extra lines became readable rather than confusing.
- I switched to `>>` for appending and re-checked the file with `cat` after every write, which is now my habit before committing.
- I settled on a simple rule: if two files should exist afterwards it is `cp`; if the old name should disappear it is `mv`.

## 7. Evidence / files

- `mission-02-terminal/terminal-practice/notes.txt` — two-line practice file.
- `mission-02-terminal/terminal-practice/notes-copy.txt` — renamed backup copy.
- Command outputs in section 2.3, with the computer username replaced by `[redacted]`.

## 8. Commit details

Commit message: **Complete Terminal and file management mission**

Pushed to GitHub on the `main` branch and verified that the folder and README are visible in the repository.
