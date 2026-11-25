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
