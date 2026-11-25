# Mission 04 — How programs run

## 1. Task / objective

Write a small Python program inside the mission folder, run it from the Terminal, and compare how a compiler and an interpreter turn source code into something the computer can execute.

## 2. Work completed

### Task 4.1 — Create and run a Python program

Created `hello.py` inside this mission folder:

```python
import platform
from datetime import datetime

print("Hello from Python")
print("Running Python:", platform.python_version())
print("Current time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
```

The first line prints the required greeting; the extra two lines were added so the run also proves which Python interpreter executed the file and when.

Command used:

```bash
python3 mission-04-programs/hello.py
```

Observed output:

```text
Hello from Python
Running Python: 3.14.7
Current time: 2026-11-25 23:37:10
```

The message appeared immediately, with no separate build step in between.

### Task 4.2 — Compiler vs. interpreter

| Point | Compiler | Interpreter |
|---|---|---|
| **When translation / execution happens** | Translates the whole source file before the program runs. | Reads and executes the code line by line at runtime. |
| **Typical output** | A separate executable or binary file that can be run on its own. | No separate file — the program runs directly from source. |
| **One example** | C, C++, Swift | Python, Ruby, JavaScript |
| **One advantage** | Fast execution once built, because translation is already done. | Fast to test and change, because there is no build step between edits and results. |

**Difference explained in my own words.** A compiler translates the entire program before anything runs, producing an executable that the computer can start directly; mistakes in syntax stop the build, so errors appear before the program ever executes. An interpreter translates and executes at the same time, line by line, so it starts almost instantly but must do the translation work during the run. A compiled program is typically faster at runtime while an interpreted one is faster to iterate on. Most real implementations mix both — Python, for instance, compiles source to bytecode first and then interprets that bytecode.

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `python3 file.py` | Run the Python script with the Python 3 interpreter. |
| `python3 --version` | Confirm which interpreter version executes the file. |
| `print()` | Display text in the program's output. |
| `platform.python_version()` | Read the running interpreter's version from inside the program. |
| VS Code | Write and save `hello.py`. |

## 4. My understanding

Running `python3 hello.py` took one step, while a compiled language would need a build step first. That difference is the whole story: the interpreter translated and executed my code on the fly, so editing the file and re-running showed the new result instantly.

The trade-off is speed and packaging. A compiled program pays the translation cost once and then runs fast without needing the compiler or language tools on the machine; an interpreted program pays it every run but needs no build and can be tested immediately. That is why Python is common for scripts and learning, and compiled languages for software where performance matters.

## 5. Difficulties faced

- The first attempt ran `python hello.py` and failed, because on this machine the command is `python3`.
- Changing the printed message did not change the file at first, because the editor had not saved it before the command ran.

## 6. How I resolved them

- I checked `python3 --version` and switched to the `python3` command, which is the correct name for the interpreter installed here.
- I saved the file before running it and re-ran the same command, which is now part of my habit: save, then run, then read the output.

## 7. Evidence / files

- `hello.py` — the program created for this mission.
- The command and its observed output, quoted in section 2.

## 8. Commit details

Commit message: **Compare compilers and interpreters**

Pushed to GitHub on the `main` branch and verified that `hello.py` and this README are visible on the repository page.
