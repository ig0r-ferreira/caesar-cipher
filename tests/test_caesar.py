import unittest

from hypothesis import given
from hypothesis.strategies import integers, text

from caesar_cipher import decode, encode


class TestEncoding(unittest.TestCase):
    @given(text(), integers())
    def test_decrypt_should_return_the_original_text(
        self, string: str, shift: int
    ) -> None:
        self.assertEqual(decode(encode(string, shift), shift), string)
