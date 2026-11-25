# Mission 02 – Terminal

## 1. Mission Objective

Become comfortable navigating directories, managing files safely, combining command flags and pipes, and inspecting package managers in the macOS Terminal.

---

## 2. Task 2.1 & 2.2 – File Operations, Redirection, and Moving Files

### Basic Commands Reference

| Operation | Command | Purpose |
|---|---|---|
| Current directory | `pwd` | Prints the full path of the working directory. |
| Directory listing | `ls` / `ls -l` | Lists files and folders (with permissions, owner, size, and date using `-l`). |
| Change directory | `cd` | Moves to another directory (e.g., `cd ..` for parent). |
| Create folder / file | `mkdir` / `touch` | Creates a directory or an empty file. |
| Copy / Move / Read | `cp` / `mv` / `cat` | Duplicates, moves/renames, or prints a file's contents. |

### Redirection (`>` vs `>>`)

`>` overwrites whatever is in the file (or creates a new one) with fresh text—wiping out old contents—while `>>` tacks new text onto the end without touching what's already there.

### Copy vs Move (`cp` vs `mv`)

`cp` makes a duplicate in a new spot or under a new name while keeping the original intact, whereas `mv` picks up the file and moves it somewhere else—or renames it if you give it a new name in the same folder—leaving just one copy behind.

---

## 3. Task 2.3 – Flags and Pipes

### Flags (`ls -lah`)

- `-l` gives the long list view (permissions, owner, size, date).
- `-a` includes hidden "dot" files (like `.`, `..`, `.git`).
- `-h` makes file sizes human-readable (like `KB` or `MB` instead of raw bytes).

### Pipes (`|`)

A pipe (`|`) hands the output of one command straight into the next command as input—so `ls -lah | head -n 3` lists everything in detail and then slices off just the top 3 lines.

#### Observed Output in Repository

`ls -lah | head -n 3`:

```text
total 8
drwxr-xr-x@ 14 anupamkislay  staff   448B Nov 25 22:36 .
drwxr-xr-x@  5 anupamkislay  staff   160B Nov 25 22:35 ..
```

`ls -lah | tail -n 3`:

```text
drwxr-xr-x@  3 anupamkislay  staff    96B Nov 25 22:36 mission-06-git-github
drwxr-xr-x@  3 anupamkislay  staff    96B Nov 25 22:36 mission-07-networking
drwxr-xr-x@  3 anupamkislay  staff    96B Nov 25 22:36 mission-08-final-report
```

---

## 4. Task 2.4 – Package Managers (Homebrew)

### Observed Homebrew Setup

- `which brew`: `/opt/homebrew/bin/brew`
- `brew --version`: `Homebrew 7.0.16`
- `brew list` (sample installed formulae): `coreutils`, `ffmpeg`, `gcc`, `gh`, `git`, `openssl@3`, `python@3.14`, `sqlite`

### Why Homebrew Is Useful

Homebrew saves you from hunting down installers on random websites, clicking through setup wizards, and updating tools one by one—you can install, update, or remove command-line tools and apps cleanly from one place.

---

## 5. Reflection

Once I started chaining small commands together with pipes, the terminal felt less like memorizing magic spells and more like snapping building blocks together—though getting tripped up by paths, spaces, or accidentally overwriting a file with `>` is easy until you slow down and check where you are.
