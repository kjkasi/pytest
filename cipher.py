def decode(encoded_str: str) -> str:
    if not isinstance(encoded_str, str): # pyright: ignore[reportUnnecessaryIsInstance]
        raise ValueError("Входные данные должны быть строкой.")
    
    if len(encoded_str) % 2 != 0:
        raise ValueError("Длина строки должна быть чётной (каждый символ — две цифры).")
    
    if encoded_str and not encoded_str.isdigit():
        raise ValueError("Строка должна содержать только цифры.")
    
    result = []
    for i in range(0, len(encoded_str), 2):
        num_str = encoded_str[i:i+2]
        num = int(num_str)
        if 0 <= num <= 25:
            result.append(chr(ord('a') + num)) # pyright: ignore[reportUnknownMemberType]
        elif num == 26:
            result.append(' ') # pyright: ignore[reportUnknownMemberType]
        else:
            raise ValueError(f"Некорректный код: {num_str}. Допустимые значения: 00–26.")
    
    return ''.join(result) # pyright: ignore[reportUnknownArgumentType]


def encode(plain_text: str) -> str:
    if not isinstance(plain_text, str): # pyright: ignore[reportUnnecessaryIsInstance]
        raise ValueError("Входные данные должны быть строкой.")

    result = []
    for ch in plain_text:
        if "a" <= ch <= "z":
            result.append(f"{ord(ch) - ord('a'):02d}") # pyright: ignore[reportUnknownMemberType]
        elif "A" <= ch <= "Z":
            result.append(f"{ord(ch) - ord('A'):02d}") # pyright: ignore[reportUnknownMemberType]
        elif ch == " ":
            result.append("26") # pyright: ignore[reportUnknownMemberType]
        else:
            raise ValueError(
                f"Недопустимый символ для шифрования: '{ch}'. "
                "Разрешены только буквы a–z (регистронезависимо) и пробел."
            )

    return "".join(result) # pyright: ignore[reportUnknownArgumentType]
