import unittest

from cipher import decode, encode


class TestCipher(unittest.TestCase):
    def test_decode_simple(self):
        self.assertEqual(decode("070411111426152419071413"), "hello python")

    def test_encode_simple(self):
        self.assertEqual(encode("hello python"), "070411111426152419071413")

    def test_round_trip(self):
        text = "hello python"
        encoded = encode(text)
        decoded = decode(encoded)
        self.assertEqual(decoded, text)

    def test_decode_lowercase_only(self):
        self.assertEqual(decode("00010226252524"), "abc zzy")

    def test_encode_mixed_case(self):
        self.assertEqual(encode("Hello Python"), "070411111426152419071413")

    def test_decode_invalid_length(self):
        with self.assertRaises(ValueError):
            decode("123")  # нечётная длина

    def test_decode_non_digit(self):
        with self.assertRaises(ValueError):
            decode("12a3")

    def test_decode_out_of_range(self):
        with self.assertRaises(ValueError):
            decode("99")  # 99 > 26

    def test_encode_invalid_char(self):
        with self.assertRaises(ValueError):
            encode("hello!")  # '!' недопустим

    def test_encode_empty(self):
        self.assertEqual(encode(""), "")

    def test_decode_empty(self):
        self.assertEqual(decode(""), "")

    def test_encode_decode_spaces(self):
        self.assertEqual(decode(encode("a b c")), "a b c")

    def test_decode_only_space(self):
        self.assertEqual(decode("26"), " ")

    def test_encode_only_space(self):
        self.assertEqual(encode(" "), "26")


if __name__ == "__main__":
    unittest.main()
