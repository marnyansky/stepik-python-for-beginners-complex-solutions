"""
url: https://stepik.org/lesson/352860/step/4?unit=336821
Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря. Она должна запрашивать у пользователя следующие данные:
- направление: шифрование или дешифрование;
- язык алфавита: русский или английский;
- шаг сдвига (со сдвигом вправо).
Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).
Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.
Примечание 3. Сохраните регистр символов. Например, текст: "Умом Россию не понять" при сдвиге на одну позицию вправо будет преобразован в: "Фнпн Спттйя ож рпоауэ".
"""


LATIN_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LATIN_LOWER = 'abcdefghijklmnopqrstuvwxyz'
CYRILLIC_UPPER = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
CYRILLIC_LOWER = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

LEN_ALPHA_LAT = 26
LEN_ALPHA_CYR = 32

LATIN = 'Latin'
CYRILLIC = 'Cyrillic'


class CaesarCipher:

    def __init__(self):
        self.interact()

    def validate_shift_value(self, language, value):
        try:
            value = int(value)
        except ValueError:
            print('Error! Here should be a number')
            return False
        if language == LATIN and 1 <= value <= LEN_ALPHA_LAT - 1:
            return True
        if language == CYRILLIC and 1 <= value <= LEN_ALPHA_CYR - 1:
            return True
        return False

    def crypt_string(self, user_string, operation_type, alphabet, alpha_len, alpha_shift):
        user_string = user_string.strip()
        if len(user_string) == 0:
            return ''

        # check: string contains chars from specified alphabet
        if alphabet == LATIN and not any(ch in [*LATIN_UPPER, *LATIN_LOWER] for ch in user_string):
            return f'String does not contain any {LATIN} character'
        if alphabet == CYRILLIC and not any(ch in [*CYRILLIC_UPPER, *CYRILLIC_LOWER] for ch in user_string):
            return f'String does not contain any {CYRILLIC} character'

        # encryption / decryption
        result = ''
        if operation_type == 'decrypt':
            alpha_shift = -alpha_shift

        for ch in user_string:
            raw_ch = chr(ord(ch) + alpha_shift)
            # if alphabet shift outside alphabet (numeric char value is too small)
            if (ch in LATIN_UPPER and raw_ch < LATIN_UPPER[0]) \
                    or (ch in LATIN_LOWER and raw_ch < LATIN_LOWER[0]) \
                    or (ch in CYRILLIC_UPPER and raw_ch < CYRILLIC_UPPER[0]) \
                    or (ch in CYRILLIC_LOWER and raw_ch < CYRILLIC_LOWER[0]):
                result += chr(ord(ch) + alpha_len + alpha_shift)
            # elif alphabet shift outside alphabet (numeric char value is too large)
            elif (ch in LATIN_UPPER and raw_ch > LATIN_UPPER[-1]) \
                    or (ch in LATIN_LOWER and raw_ch > LATIN_LOWER[-1]) \
                    or (ch in CYRILLIC_UPPER and raw_ch > CYRILLIC_UPPER[-1]) \
                    or (ch in CYRILLIC_LOWER and raw_ch > CYRILLIC_LOWER[-1]):
                result += chr(ord(ch) - alpha_len + alpha_shift)
            # elif alphabet shift inside alphabet
            elif ch in [*LATIN_UPPER, *LATIN_LOWER, *CYRILLIC_UPPER, *CYRILLIC_LOWER]:
                result += chr(ord(ch) + alpha_shift)
            # else no alphabet shift for non-latin and non-cyrillic characters
            else:
                result += ch
        return result

    def interact(self):
        print('# Caesar Cipher #')
        print('Please, choose operation type (D)ecryption / (E)ncryption: ', end='')
        x1 = input()
        operation_type = 'decrypt' if x1.isalpha() and x1.upper() == 'D' else 'encrypt'

        print('Please, choose alphabet (L)atin / (C)yrillic: ', end='')
        x2 = input()
        alphabet = CYRILLIC if x2.isalpha() and x2.upper() == 'C' else LATIN
        alpha_len = LEN_ALPHA_CYR if alphabet == CYRILLIC else LEN_ALPHA_LAT

        print(f'Please, define shift value (1-25 for {LATIN}, 1-31 for {CYRILLIC}): ')
        x3 = input()
        alpha_shift = int(x3) if self.validate_shift_value(alphabet, x3) else 1

        print(f"Launching Caesar Cipher with parameters: "
              f"'{operation_type}', '{alphabet}', '{str(alpha_shift)}'...")
        print(f'Please, enter the text you wish to {operation_type}')
        print(self.crypt_string(input(), operation_type, alphabet, alpha_len, alpha_shift))


if __name__ == '__main__':
    caesar_cipher = CaesarCipher()
