# Mission 04 – Programs

## 1. Mission Objective

Understand how programs are executed on a computer, write and run a Python script from the Terminal, and compare compiled vs. interpreted execution models.

---

## 2. Task 4.1 – Create and Run a Python Program

### Program Created (`hello.py`)

```python
import platform
from datetime import datetime

print("Hello from Mission 04! Python is up and running.")
print("Running Python:", platform.python_version())
print("Current time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
```

### Command Used

```bash
python3 mission-04-programs/hello.py
```

### Observed Output

```text
Hello from Mission 04! Python is up and running.
Running Python: 3.14.7
Current time: 2026-11-25 23:37:10
```

---

## 3. Task 4.2 – Compiler vs. Interpreter

| Point | Compiler | Interpreter |
|---|---|---|
| **When translation happens** | Translates the entire codebase upfront before execution. | Reads and executes code on the fly at runtime. |
| **Output produced** | Outputs a standalone executable/binary file. | Runs directly without producing a separate binary first. |
| **Examples** | C++, Swift | Python, Ruby |
| **Trade-off / Advantage** | Blazing-fast execution once built, though you wait to recompile after edits. | Fast, effortless testing and tweaking, though typically slower at runtime than compiled code. |

### Summary

A compiler translates your entire codebase upfront before you run it, spitting out a standalone executable file (like C++ or Swift). The upside is blazing-fast execution once built, though you have to wait for it to recompile every time you tweak something. An interpreter reads and runs your code on the fly at runtime without creating a separate binary first (like Python or Ruby), making testing and tweaking code super fast and effortless, even if it runs a bit slower than compiled code.

---

## 4. Reflection

It really clicked for me how every language is just a trade-off between how fast I can write and test code versus how fast the computer can run it—and seeing Python run a script instantly made the whole execution layer feel way less abstract.
