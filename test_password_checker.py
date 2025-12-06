import unittest

from password_checker import check_password


class TestCheckPassword(unittest.TestCase):
    def test_valid_passwords(self):
        """Тестирование корректных паролей."""
        valid_passwords = [
            "o58anuahaunH!",
            "aaaAAA111!!!",
            "A1b2C3d4_",
            "Passw0rd@",
            "12ABcd!@_",
            "XyZ9876%$",
        ]
        for pwd in valid_passwords:
            with self.subTest(password=pwd):
                is_valid, message = check_password(pwd)
                self.assertTrue(
                    is_valid,
                    f"Пароль '{pwd}' должен быть валидным, но получил: {message}",
                )

    def test_invalid_length(self):
        """Тестирование паролей с неправильной длиной."""
        self.assertFalse(check_password("A1b2C!")[0])  # 6 символов — слишком коротко
        self.assertFalse(
            check_password("A1b2C3d4e5F6g7h8!")[0]
        )  # 18 символов — слишком длинно

    def test_missing_character_types(self):
        """Тестирование отсутствия обязательных типов символов."""
        self.assertIn("нет цифр", check_password("abcDEF!@_")[1])
        self.assertIn("нет строчных букв", check_password("ABC123!@_")[1])
        self.assertIn("нет прописных букв", check_password("abc123!@_")[1])
        self.assertIn("нет специальных символов", check_password("abcABC123")[1])

    def test_invalid_characters(self):
        """Тестирование наличия запрещённых символов."""
        is_valid, message = check_password("abcABC123*")  # '*' не входит в SPECIAL
        self.assertFalse(is_valid)
        self.assertIn("запрещённые символы", message)
        self.assertIn("'*'", message)

        is_valid, message = check_password("abc ABC123!")  # пробел запрещён
        self.assertFalse(is_valid)
        self.assertIn("запрещённые символы", message)
        self.assertIn("' '", message)

    def test_edge_case_min_length(self):
        """Пароль длиной ровно 8 символов — должен пройти, если есть все типы."""
        is_valid, _ = check_password("A1b2C3d!")
        self.assertTrue(is_valid)

    def test_edge_case_max_length(self):
        """Пароль длиной ровно 15 символов — должен пройти, если есть все типы."""
        is_valid, _ = check_password("A1b2C3d4E5f6G7!")
        self.assertTrue(is_valid)

    def test_all_same_type_invalid(self):
        """Пароль из одних цифр — недопустим."""
        is_valid, message = check_password("12345678")
        self.assertFalse(is_valid)
        self.assertIn("нет строчных букв", message)
        self.assertIn("нет прописных букв", message)
        self.assertIn("нет специальных символов", message)


if __name__ == "__main__":
    unittest.main()
