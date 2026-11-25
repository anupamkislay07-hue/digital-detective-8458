# Mission 05 — Numbers, data and text encoding

## 1. Task / objective

Convert values between decimal, binary and hexadecimal by hand showing the working, verify each conversion with Python, build a small working converter program, and explain how computers store text with ASCII and UTF-8.

## 2. Work completed

### Task 5.1 — Conversions by hand

**1. Decimal 13 → binary** (repeated division by 2)

| Division | Quotient | Remainder |
|---|---:|---:|
| 13 ÷ 2 | 6 | 1 |
| 6 ÷ 2 | 3 | 0 |
| 3 ÷ 2 | 1 | 1 |
| 1 ÷ 2 | 0 | 1 |

Reading remainders bottom to top: `13 = 1101₂`

**2. Decimal 25 → binary**

| Division | Quotient | Remainder |
|---|---:|---:|
| 25 ÷ 2 | 12 | 1 |
| 12 ÷ 2 | 6 | 0 |
| 6 ÷ 2 | 3 | 0 |
| 3 ÷ 2 | 1 | 1 |
| 1 ÷ 2 | 0 | 1 |

`25 = 11001₂`

**3. Binary 1010 → decimal**

= 1 × 2³ + 0 × 2² + 1 × 2¹ + 0 × 2⁰ = 8 + 0 + 2 + 0 = **10**

**4. Binary 1101 → decimal**

= 1 × 2³ + 1 × 2² + 0 × 2¹ + 1 × 2⁰ = 8 + 4 + 0 + 1 = **13**

**5. Hexadecimal A → decimal**

A = 10, and this is a single digit in the 16⁰ place, so **A = 10**

**6. Hexadecimal 1F → decimal**

= 1 × 16¹ + 15 × 16⁰ = 16 + 15 = **31**

**7. Binary 1111 → hexadecimal**

1111₂ = 8 + 4 + 2 + 1 = 15, and 15 in hexadecimal is F, so **1111₂ = F₁₆**

### Task 5.2 — Verification with Python

| Expression | Result | Matches manual work? |
|---|---|---|
| `bin(13)` | `0b1101` | Yes |
| `bin(25)` | `0b11001` | Yes |
| `int("1010", 2)` | `10` | Yes |
| `int("1101", 2)` | `13` | Yes |
| `int("A", 16)` | `10` | Yes |
| `int("1F", 16)` | `31` | Yes |
| `hex(15)` | `0xf` | Yes |

### Task 5.3 — The number converter

`number_converter.py` in this folder:

```python
# Decimal to Binary and Hexadecimal Converter

number = int(input("Enter a decimal number: "))

binary = bin(number)
hexadecimal = hex(number)

print("Decimal:", number)
print("Binary:", binary)
print("Hexadecimal:", hexadecimal)
```

Run from this folder with `python3 number_converter.py`. Test results:

| Test input | Binary output | Hexadecimal output |
|---|---|---|
| `13` | `0b1101` | `0xd` |
| `25` | `0b11001` | `0x19` |
| `31` | `0b11111` | `0x1f` |

All three match the hand calculations in Task 5.1.

### Task 5.4 — How text is stored

- **ASCII decimal codes:** uppercase `A` = **65**, lowercase `a` = **97**.
- **Why an encoding standard is needed:** a computer can only store numbers, so an encoding defines which number represents which character. Without an agreed standard, the same bytes would be shown as different characters on different machines and text could not be exchanged reliably.
- **Characters outside basic ASCII:** `₹` (Indian rupee sign), `अ` (Devanagari letter) and `😊` (emoji) are all outside the 128 basic ASCII characters and are represented using Unicode encodings such as UTF-8.

## 3. Commands / tools used

| Command / tool / function | Purpose |
|---|---|
| `python3` (interactive shell) | Test conversion expressions one at a time. |
| `bin(n)` | Convert an integer to a binary string with the `0b` prefix. |
| `hex(n)` | Convert an integer to a hexadecimal string with the `0x` prefix. |
| `int(string, base)` | Interpret a string as a number in a given base (2 for binary, 16 for hex). |
| `input()` | Read the number typed by the user as text. |
| `int()` | Convert that text into an integer. |
| `print()` | Display the decimal, binary and hexadecimal results. |
| `ord()` | Checked character codes while verifying ASCII values. |

## 4. My understanding

Positional number systems all work the same way: each position is worth the base raised to a power, and hexadecimal is simply base 16 where the digits after 9 are A–F. That is why decimal 25 becomes `11001₂` (16 + 8 + 1) and hexadecimal `1F` becomes 31 (16 + 15).

Converting to binary by repeated division collects remainders in reverse order; converting back multiplies each bit by its power of two. `bin()` and `hex()` do that work and mark the base with `0b` and `0x`, while `int(text, base)` goes the other way. The converter program is just those three steps plus input and output.

Text is numbers too. ASCII covers 128 characters where `A` is 65 and `a` is 97, so case is a difference of 32. That small set cannot hold other alphabets or emoji, which is why Unicode and UTF-8 exist: a wider set of characters, stored with a variable number of bytes so plain English stays compact.

## 5. Difficulties faced

- Understanding the different bases and writing the division tables in the correct order.
- Converting binary to hexadecimal at first, until I realised four binary bits map to exactly one hex digit.
- Mixing up the `0b`/`0x` prefixes that Python prints with the actual digits, when comparing results to my manual answers.

## 6. How I resolved them

- I used repeated division for decimal → binary and always read the remainders from the bottom upward, which made `13` and `25` come out correct.
- I grouped `1111` into one group of four bits, saw it equals 15, and wrote `F` — the four-bits-per-hex-digit rule made every later conversion quick.
- I compared only the digits after the prefix, so `0b1101` was checked against my `1101` working rather than treated as an error.

## 7. Evidence / files

- `number_converter.py` — the working converter used for the tests above.
- This README with the manual working, Python verification table and test results.

## 8. Commit details

Commit message: **Build number converter and practise data representation**

Pushed to GitHub on the `main` branch and verified that `number_converter.py` and this README are visible in the repository.
