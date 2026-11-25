# Mission 03 – Operating System

## 1. Mission Objective

Understand how an operating system manages hardware and software resources, inspect system information on macOS using the Terminal, and learn how processes, paths, and file permissions work.

---

## 2. Task 3.1 – Exploring System Information

### Observed Outputs on My Mac

- `sw_vers`: `macOS 27.2.1` (Build `26B131`)
- `uname -srm`: `Darwin 27.2.0 arm64`
- `whoami`: `anupamkislay`
- `df -h /`:

```text
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   926Gi    13Gi   805Gi     2%    487k  4.3G    0%   /
```

---

## 3. Task 3.2 – Understanding Running Processes

A process is a running instance of a program in memory, and its PID (Process ID) is the unique number macOS gives it to track and manage it. Checking running apps like Chrome or VS Code shows dozens of processes instead of just one—splitting tabs, extensions, renderers, and background helpers into separate processes keeps the whole app from crashing when one tab freezes and lets work run more safely and in parallel.

---

## 4. Task 3.3 – Paths and File Permissions

- **Absolute vs. Relative Paths:** An absolute path gives the full address starting from the root `/` (like `/Users/anupamkislay/Desktop/notes.txt`), whereas a relative path starts from wherever your Terminal currently sits (like `./notes.txt` or `../Desktop`).
- **Permissions (`r`, `w`, `x`):** `r` (read), `w` (write/edit), and `x` (execute/run or enter a folder) control what can be done to a file or directory.
- **`chmod` vs. `chown`:** `chmod` changes those `rwx` permission bits, while `chown` changes who owns the file (and its group).

---

## 5. Task 3.4 – Operating System Responsibilities

| Responsibility | What It Does | macOS Example |
|---|---|---|
| **Process Management** | Schedules and isolates active tasks. | Letting Music play in the background while Xcode compiles code. |
| **Memory Management** | Allocates RAM and swaps inactive data to the SSD. | Keeping dozens of Safari tabs alive without running out of memory. |
| **File Management** | Organizes data into folders and tracks locations on disk. | Finder and APFS handling documents and metadata. |
| **Device Management** | Talks to hardware through drivers. | Routing audio to AirPods or cursor input from the trackpad. |
| **Security Management** | Enforces user accounts, sandboxing, and permission prompts. | Asking before an app accesses the mic, camera, or Screen Recording. |

---

## 6. Reflection

What stood out most is how much defensive isolation happens quietly—one frozen tab doesn't have to take down a whole browser, and permission boundaries keep apps from silently rummaging through everything. Getting used to permission numbers and path rules takes a second, but it makes the system feel way more predictable.
