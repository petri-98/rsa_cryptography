'''ASCII encoding schemes.
More info in README.md
'''

def text_to_int(text: str) -> int:
    """Returns the ASCII encoding of the given string.

    Args:
        text (str): String to encode.

    Returns:
        int: Encoded string.
    """
    number = 0
    i = 0
    for character in text:
        number += ord(character) * (256**i)
        i += 1
    return number


def intToText(number: int) -> str:
    """Returns the string corresponding to the given encoded input.

    Args:
        number (int): Encoded string.

    Returns:
        str: Decoded string.
    """
    text = ""
    while number > 0:
        next_letter = number % 256
        text += chr(next_letter)
        number = (number - next_letter) // 256
    return text
