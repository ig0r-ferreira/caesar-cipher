from string import ascii_lowercase, ascii_uppercase


def encrypt(text: str, shift: int) -> str:
    """Encrypt a text."""
    encrypted_text = ''
    for character in text:
        character_shifted = character

        alphabet = ascii_lowercase if character.islower() else ascii_uppercase
        index_character = alphabet.find(character)

        if index_character != -1:
            new_index = (index_character + shift) % 26
            character_shifted = alphabet[new_index]

        encrypted_text += character_shifted

    return encrypted_text


def decrypt(text: str, shift: int) -> str:
    """Decrypt a text."""
    return encrypt(text, shift * (-1))
