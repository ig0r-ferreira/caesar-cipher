import unittest

from hypothesis import given
from hypothesis.strategies import integers, text

from caesar_cipher import decrypt, encrypt


class TestEncoding(unittest.TestCase):
    @given(text(), integers())
    def test_decrypt_should_return_the_original_text(
        self, string: str, shift: int
    ) -> None:
        self.assertEqual(decrypt(encrypt(string, shift), shift), string)
