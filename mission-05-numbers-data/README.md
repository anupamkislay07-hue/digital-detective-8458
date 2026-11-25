# Mission 05 – Numbers & Data

## 1. Mission Objective

Understand binary, octal, decimal, and hexadecimal number systems, perform manual conversions and verify them in Python, build a reusable `number_converter.py` script, and learn how computers encode text using ASCII and Unicode/UTF-8.

---

## 2. Task 5.1 & 5.2 – Manual Conversions and Python Verification

| Conversion | Manual Work | Result | Python Verification |
|---|---|---|---|
| **Decimal 19 → Binary** | `16 + 2 + 1` | `10011` | `bin(19)` → `0b10011` |
| **Decimal 42 → Binary** | `32 + 8 + 2` | `101010` | `bin(42)` → `0b101010` |
| **Decimal 42 → Hex** | `2 × 16 + 10` | `2A` | `hex(42)` → `0x2a` |
| **Binary 10110 → Decimal** | `16 + 4 + 2` | `22` | `int("10110", 2)` → `22` |
| **Hex 2A → Decimal** | `2 × 16 + 10` | `42` | `int("2A", 16)` → `42` |
| **Binary 1110 → Hex** | `8 + 4 + 2 = 14` | `E` | `hex(14)` → `0xe` |

---

## 3. Task 5.3 – Build a Number Converter (`number_converter.py`)

### Program Code

```python
def convert_number(num: int) -> None:
    print(f"Decimal : {num}")
    print(f"Binary  : {bin(num)} ({bin(num)[2:]})")
    print(f"Octal   : {oct(num)} ({oct(num)[2:]})")
    print(f"Hex     : {hex(num).upper().replace('0X', '0x')} ({hex(num)[2:].upper()})")


if __name__ == "__main__":
    raw = input("Enter a decimal integer: ").strip()
    try:
        value = int(raw)
        convert_number(value)
    except ValueError:
        print(f"'{raw}' isn't a valid whole number—try something like 42.")
```

### Observed Test Runs

**Test 1 (`19`):**

```text
Enter a decimal integer: 19
Decimal : 19
Binary  : 0b10011 (10011)
Octal   : 0o23 (23)
Hex     : 0x13 (13)
```

**Test 2 (`42`):**

```text
Enter a decimal integer: 42
Decimal : 42
Binary  : 0b101010 (101010)
Octal   : 0o52 (52)
Hex     : 0x2A (2A)
```

**Test 3 (`abc` — invalid input handling):**

```text
Enter a decimal integer: abc
'abc' isn't a valid whole number—try something like 42.
```

---

## 4. Task 5.4 – How Computers Store Text

Computers only store numbers, so text encodings map characters to number codes. **ASCII** assigns numbers `0–127` to basic English letters, digits, punctuation, and control characters (1 byte per character). **Unicode** expands that to cover over 140,000+ characters across scripts, symbols, and emojis, and **UTF-8** is the variable-width way of encoding those code points into 1 to 4 bytes—staying 100% compatible with plain ASCII while using extra bytes when needed.

Examples of characters outside basic ASCII: `é`, `₹`, and `🚀`.

---

## 5. Reflection

Grouping binary into 4-bit nibbles for hex makes reading big numbers way easier than counting raw ones and zeros—though keeping track of place values and prefixes (`0b`, `0x`) takes a little practice at first.
