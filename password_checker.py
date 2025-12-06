import string as st

DIGITS = st.digits
LOWERCASE = st.ascii_lowercase
UPPERCASE = st.ascii_uppercase
SPECIAL = "_!@#$%^&"


def check_password(password: str) -> tuple[bool, str]:
    """
    Проверяет пароль на соответствие требованиям.

    Требования:
    - Длина от 8 до 15 символов включительно
    - Обязательно хотя бы один символ из каждого из 4 наборов:
        * цифры
        * строчные латинские буквы
        * прописные латинские буквы
        * специальные символы '_!@#$%^&'
    - Пароль может содержать ТОЛЬКО символы из этих 4 наборов

    Возвращает кортеж: (валиден_ли, пояснение)
    """
    reasons = []

    if len(password) < 8:
        reasons.append("слишком короткий (менее 8 символов)")
    elif len(password) > 15:
        reasons.append("слишком длинный (более 15 символов)")

    # Проверка наличия символов из каждого набора
    has_digit = False
    has_lower = False
    has_upper = False
    has_special = False

    # Проверка, что все символы из разрешённых наборов
    allowed_chars = DIGITS + LOWERCASE + UPPERCASE + SPECIAL
    invalid_chars = []

    for char in password:
        if char in DIGITS:
            has_digit = True
        elif char in LOWERCASE:
            has_lower = True
        elif char in UPPERCASE:
            has_upper = True
        elif char in SPECIAL:
            has_special = True
        else:
            if char not in invalid_chars:
                invalid_chars.append(char)

    if invalid_chars:
        reasons.append(
            f"содержит запрещённые символы: {', '.join(repr(c) for c in invalid_chars)}"
        )

    if not has_digit:
        reasons.append("нет цифр")
    if not has_lower:
        reasons.append("нет строчных букв")
    if not has_upper:
        reasons.append("нет прописных букв")
    if not has_special:
        reasons.append("нет специальных символов")

    if reasons:
        return False, "; ".join(reasons)
    else:
        return True, "пароль подходит"


def main():
    """
    Основная функция для взаимодействия с пользователем.
    """
    max_attempts = 5

    for attempt in range(1, max_attempts + 1):
        print(f"\nПопытка {attempt} из {max_attempts}")
        password = input("Введите пароль: ")

        is_valid, message = check_password(password)

        if is_valid:
            print("пароль подходит")
            return
        else:
            print(f"пароль не подходит -> {message}")

    print("\nПревышено максимальное количество попыток.")


if __name__ == "__main__":
    main()
