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

        # check: string contains chars from specified alphabet
        if alphabet == LATIN and not any(
                ('A' <= chr(ord(ch)) <= 'Z') or ('a' <= chr(ord(ch)) <= 'z') for ch in user_string):
            return f'String does not contain any {LATIN} character'
        if alphabet == CYRILLIC and not any(
                ('А' <= chr(ord(ch)) <= 'Я') or ('а' <= chr(ord(ch)) <= 'я') for ch in user_string):
            return f'String does not contain any {CYRILLIC} character'

        # encryption / decryption
        result = ''
        if operation_type == 'decrypt':
            alpha_shift = -alpha_shift
        if len(user_string) > 0:
            for ch in user_string:
                raw_ch = chr(ord(ch) + alpha_shift)  # check for shift outside alphabet
                if ch in LATIN_UPPER:
                    if raw_ch < 'A':
                        result += chr(ord(ch) + alpha_len + alpha_shift)
                    elif raw_ch > 'Z':
                        result += chr(ord(ch) - alpha_len + alpha_shift)
                    else:
                        result += chr(ord(ch) + alpha_shift)
                elif ch in LATIN_LOWER:
                    if raw_ch < 'a':
                        result += chr(ord(ch) + alpha_len + alpha_shift)
                    elif raw_ch > 'z':
                        result += chr(ord(ch) - alpha_len + alpha_shift)
                    else:
                        result += chr(ord(ch) + alpha_shift)
                elif ch in CYRILLIC_UPPER:
                    if raw_ch < 'А':
                        result += chr(ord(ch) + alpha_len + alpha_shift)
                    elif raw_ch > 'Я':
                        result += chr(ord(ch) - alpha_len + alpha_shift)
                    else:
                        result += chr(ord(ch) + alpha_shift)
                elif ch in CYRILLIC_LOWER:
                    if raw_ch < 'а':
                        result += chr(ord(ch) + alpha_len + alpha_shift)
                    elif raw_ch > 'я':
                        result += chr(ord(ch) - alpha_len + alpha_shift)
                    else:
                        result += chr(ord(ch) + alpha_shift)
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
