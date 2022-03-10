"""
Ceaser Cipher
"""
def ceasar_cipher(text, shift):
    """
    Ceaser Cipher
    """
    plain = ""
    ciph = ""
    letters = 26
    for i in text.upper():
        if i.isupper():
            plain = ord(i)
            plain = plain + shift
            if plain > ord('Z'):
                plain = plain - letters
            elif plain < ord('A'):
                plain = plain + letters
            ciph = ciph + chr(plain)
        else:
            ciph = ciph + " "
    return ciph


if __name__ == '__main__':
    PLAIN_TEXT = "abcd xyzzzz ZZZZ"
    CIPHER_TEXT = "EFGH BCDDDD DDDD"
    print(ceasar_cipher(PLAIN_TEXT,4))
    print(CIPHER_TEXT)
