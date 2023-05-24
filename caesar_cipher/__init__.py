from string import ascii_lowercase, ascii_uppercase


def encode(text: str, shift: int) -> str:
    """Encode a text according to the number of positions to be shifted."""
    encoded_text = ''
    for character in text:
        character_shifted = character

        alphabet = ascii_lowercase if character.islower() else ascii_uppercase
        index_character = alphabet.find(character)

        if index_character != -1:
            new_index = (index_character + shift) % 26
            character_shifted = alphabet[new_index]

        encoded_text += character_shifted

    return encoded_text


def decode(text: str, shift: int) -> str:
    """Decode a text according to the number of positions to be shifted."""
    return encode(text, shift * (-1))
