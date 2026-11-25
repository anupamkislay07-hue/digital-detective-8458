# Mission 03 — Operating system, processes and permissions

## 1. Task / objective

Find out which operating system and account I am using, how much storage is free, and what the system is doing right now; understand what a process and a PID are; tell absolute paths from relative ones and read file permissions; then explain the main responsibilities of an operating system in my own words.

## 2. Work completed

### Task 3.1 — System information, account, storage and activity

| Information explored | What it tells me | My observation (privacy-safe) |
|---|---|---|
| Operating system / system details | Which OS family, version, build and CPU architecture I am running, which decides which commands and installers apply. | `sw_vers` → `macOS 27.2.1`, build `26B131`; `uname -srm` → `Darwin 27.2.0 arm64` (Apple Silicon). |
| Current account identity | Which user I am logged in as, and therefore which files I own and which permissions I inherit. | `whoami` → `[redacted]`. `id -un` confirmed the same account. |
| Available and used storage | How much disk space is free, so I know whether downloads, builds or commits can succeed. | `df -h /` → `926Gi` size, `13Gi` used, `805Gi` available, `2%` capacity on `/`. |
| System activity snapshot | How loaded the machine is right now: process count and CPU idle share. | `top -l 1` → `885 total` processes (`2 running`, `883 sleeping`, `4131 threads`); CPU `2.48% user, 8.86% sys, 88.65% idle`; load average `1.70, 2.31, 2.19`; memory `13G used`, `2103M unused`. |

The storage row and the activity row answer different questions: `df` is about disk *capacity*, while `top` is about *current work* — how many processes exist and whether the CPU is busy or idle.

### Task 3.2 — Processes and the PID

Observed with `ps -ax -o pid,comm` (full paths shortened):

```text
  PID COMM
    1 /sbin/launchd
  331 /usr/libexec/logd
  336 .../fseventsd
  345 /usr/libexec/configd
```

A **process** is a program that is currently loaded in memory and running — the same application can be many processes at once. The **PID** column is the unique number the operating system gives each process so it can schedule it, give it resources and stop it.

Two example processes on my computer: **`launchd`** (`PID 1`, the first process the system starts, which launches and supervises other services) and **`configd`** (`PID 345`, which manages network configuration changes in the background). Opening Chrome or VS Code in the GUI added many more rows in `top`, one per tab, renderer or helper — which is why a single app can appear dozens of times.

### Task 3.3 — Paths and permissions

**Absolute path** — the full address from the root `/`, valid from anywhere. Example from my assignment folder:

```text
/Users/[redacted]/digital-detective-8458/mission-03-operating-system
```

**Relative path** — an address interpreted from wherever I currently am. From the repository root:

```text
./mission-03-operating-system
```

and from inside that folder, `../mission-02-terminal` reaches the sibling mission folder. I confirmed this by running `pwd` inside each location and watching the path grow or shrink by one segment per `cd`.

**Permissions for a file inside my practice area:**

```text
-rw-r--r--@ 1 [redacted]  staff  2038 Nov 26 01:05 README.md
```

The first character `-` means it is a regular file (a `d` would mean directory). The next nine characters are three groups of three: owner, group, others. For the owner (`rw-`) the answer is: **read — yes, write — yes, execute — no.** The file can be opened and edited by me but not run as a program. Owners of directories usually also have `x`, which is what allows entering the folder.

| Permission | Meaning | Example |
|---|---|---|
| `r` — read | Contents can be read. | Opening `notes.txt` with `cat`. |
| `w` — write | Contents can be changed. | Editing the README. |
| `x` — execute | The file can be run; on a folder it allows traversal. | Running `python3 hello.py`. |

No system permissions were changed. `chmod` alters these `rwx` bits and `chown` changes ownership; both were only read about, never used.

### Task 3.4 — Operating-system responsibilities

| Responsibility | My explanation | Example |
|---|---|---|
| **Process management** | Decides which running program gets the CPU and for how long, and starts or stops processes. | Music keeps playing while Xcode compiles in another process. |
| **Memory management** | Hands out RAM to processes, reclaims it when they exit, and moves inactive data to disk when RAM runs out. | Dozens of Safari tabs stay alive via compressor/swap instead of crashing. |
| **Device management** | Talks to hardware through drivers and hides the differences between devices behind one interface. | Audio is routed to AirPods, input arrives from the trackpad. |
| **File management** | Organises data into files and folders, tracks where blocks live, and enforces who may read or write them. | Finder and APFS storing documents and their metadata. |
| **User interface / shell** | Provides the layer a human uses to give instructions — graphical windows or a typed command line — and passes those requests to the system. | The Terminal running `ls`, or Finder showing the same folder. |
| **Security and permissions** | Keeps users separate, sandboxes apps and asks before sensitive access is granted. | A prompt before an app uses the microphone or camera. |

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `sw_vers` | Show macOS product name, version and build. |
| `uname -srm` | Show kernel name, release and machine architecture. |
| `whoami`, `id -un` | Show the currently active account name. |
| `df -h /` | Show total, used and available storage in human-readable units. |
| `top -l 1` | Take a single snapshot of processes, CPU load and memory use. |
| `ps -ax -o pid,comm` | List all processes with their PID and command name. |
| `pwd`, `cd` | Show and change the current location, to compare absolute and relative paths. |
| `ls -l` | Read permission letters, owner, group and size for a file. |

## 4. My understanding

The operating system is the layer between hardware and every program I run. It decides which process gets the processor, which memory each one may touch, how hardware is reached, where data lives on disk, and who is allowed to read or change it — and it exposes all of that through a user interface or shell. Permissions are the visible edge of that control: `-rw-r--r--` is the OS telling me exactly what my account may do with a file, and the same bits on a folder control whether I can enter it at all.

Paths are how the file system is addressed. An absolute path starts at `/` and works from anywhere; a relative path depends on the current directory, which is why `pwd` matters before any file command. Processes are the live form of programs, each with a PID so the system can manage it individually — the reason one frozen browser tab does not take the whole browser down.

## 5. Difficulties faced

- `top -l 1` printed many lines and several statistics blocks, so it took a moment to find the process count and the CPU idle figure.
- Reading permission strings like `-rw-r--r--@` was slow at first, especially the trailing `@` and the difference between file and directory leading characters.
- The absolute path of this project is long and contains hidden folders, which made it easy to lose track of where a relative `cd` would land.

## 6. How I resolved them

- I used `top`'s `-stats pid,command,cpu,mem` option to print a short, readable table instead of the default screenful, and read the summary lines separately.
- I broke permissions into three fixed groups (owner, group, others) of `rwx` and checked them against `ls -l`, which made the pattern predictable; I learned `d` means directory and `@` means extended attributes.
- I ran `pwd` after every `cd` until the relative paths became intuitive, and I now use absolute paths in scripts.

## 7. Evidence / files

- System, storage, process and permission outputs quoted in this README, with the account name and home directory replaced by `[redacted]`.
- No personal identifiers, hostnames or network addresses are recorded.

## 8. Commit details

Commit message: **Document operating system, processes and permissions**

Pushed to GitHub on the `main` branch and verified the updated README on the repository page.
