"""
На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
Строчные буквы при этом остаются строчными, а прописные – прописными.
Sample input: Day, mice. "Year" is a mistake!
Sample output: Gdb, qmgi. "Ciev" ku b tpzahrl!
URL: https://stepik.org/lesson/352860/step/10?unit=336821
"""

LATIN = [chr(i) for i in range(65, 91)] + [chr(j) for j in range(97, 123)]
CYRILLIC = [chr(i) for i in range(1040, 1104)]

LEN_LATIN = 26
LEN_CYRILLIC = 32

MESSAGE_TITLE = '~ Caesar Cipher 2 ~'
MESSAGE_ENTER_TEXT = 'Please, enter the text you want to encrypt or decrypt:'


def apply_cipher(word):
    word_alphabetic = ''.join(x for x in word if x.isalpha())
    shift_value = len(word_alphabetic)

    for ch in word:
        if ch.isalpha():
            alphabet = LATIN if ch in LATIN else CYRILLIC
            len_alpha = LEN_LATIN if ch in LATIN else LEN_CYRILLIC
            if ch.isupper():
                target_indx = (alphabet.index(ch) + shift_value) % len_alpha
            else:
                target_indx = (alphabet.index(ch) + shift_value) % len_alpha + len_alpha
            print(alphabet[target_indx], end='')
        else:
            print(ch, end='')


class CaesarCipher2:

    def __init__(self):
        print(MESSAGE_TITLE)
        print(MESSAGE_ENTER_TEXT)
        user_text = input()
        self.crypt(user_text)

    def crypt(self, user_text):
        words = user_text.strip().split()
        for word in words:
            apply_cipher(word)
            print(' ', end='')


if __name__ == '__main__':
    cesar_cipher_adv = CaesarCipher2()
