"""
Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии
с алгоритмом Цезаря. Она должна запрашивать у пользователя следующие данные:
- направление: шифрование или дешифрование;
- язык алфавита: русский или английский;
- шаг сдвига (со сдвигом вправо).
Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).
Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.
Примечание 3. Сохраните регистр символов. Например, текст: "Умом Россию не понять"
при сдвиге на одну позицию вправо будет преобразован в: "Фнпн Спттйя ож рпоауэ".
URL: https://stepik.org/lesson/352860/step/4?unit=336821
"""

LATIN = [chr(i) for i in range(65, 91)] + [chr(j) for j in range(97, 123)]
CYRILLIC = [chr(i) for i in range(1040, 1104)]

LEN_LATIN = 26
LEN_CYRILLIC = 32

MESSAGE_TITLE = '### Caesar Cipher Advanced ###'
MESSAGE_WELCOME = 'Please, enter a shift value for encryption (>0) or decryption (<0): '
MESSAGE_ENTER_TEXT = 'Please, enter the text you want to encrypt/decrypt:'


def is_number(x):
    try:
        if int(x) != 0:
            return int(x)
        else:
            print('You entered a wrong shift value!')
            exit()
    except ValueError:
        print("Shift value should have been a number!")
        exit()


class CaesarCipherAdv:

    def __init__(self):
        print(MESSAGE_TITLE)
        self.crypt()

    def crypt(self):
        print(MESSAGE_WELCOME, end='')
        shift_value = is_number(input())
        print(MESSAGE_ENTER_TEXT)
        user_text = input()

        for ch in user_text:
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


if __name__ == '__main__':
    cesar_cipher_adv = CaesarCipherAdv()
