"""
Safe Password Generator
accepts parameters:
- amount of passwords to generate
- minimum password length
- maximum password length
- include lowercase letters? Y/N
- include uppercase letters? Y/N
- include special characters? Y/N
- include characters that is not easy to differentiate? Y/N
"""

import random

NUM_MIN = 1
NUM_MAX = 100
LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SPECIAL_CHARS = '!#$%&*+-=?@^_'
OPTIONAL_CHARS = 'il1Lo0O'


def get_number_strict(x):
    try:
        if NUM_MIN <= int(x) <= NUM_MAX:
            return int(x)
        else:
            print(f'Error! A number should be in range {NUM_MIN}-{NUM_MAX}!')
            exit()
    except ValueError:
        print(f'Error! I expected a number in range {NUM_MIN}-{NUM_MAX}!')
        exit()


def is_answer_positive(x):
    try:
        return x.strip().upper()[0] == 'Y'
    except IndexError as e:
        print('Input error! Type: ' + e.__str__())
        return False


def get_chars_for_password(lwr, upr, spc, hrd):
    pw_chars = ''
    if lwr:
        pw_chars += LOWERCASE
    if upr:
        pw_chars += UPPERCASE
    if spc:
        pw_chars += SPECIAL_CHARS
    if hrd:
        pw_chars += OPTIONAL_CHARS
    return pw_chars


def generate_password(amount, minlen, maxlen, lwr, upr, spc, hrd):
    all_passwords = []

    pw = ''
    for _ in range(amount):
        pw_length = random.randrange(minlen, maxlen) if maxlen > minlen else maxlen
        for _ in range(pw_length):
            chars_str = get_chars_for_password(lwr, upr, spc, hrd)
            pw += random.choice(chars_str) if len(chars_str) > 0 else ''
        all_passwords.append(pw)
        pw = ''

    return all_passwords


class SafePassword:

    def __init__(self):
        self.set_user_preferences()

    def set_user_preferences(self):
        print('* * * Safe Password Generator * * *')

        print(f'How many passwords you want me to generate ({NUM_MIN}-{NUM_MAX})? ', end='')
        pw_amount = get_number_strict(input())
        print(f'Please, set minimum password length ({NUM_MIN}-{NUM_MAX}): ', end='')
        pw_min_length = get_number_strict(input())
        print(f'Please, set maximum password length ({NUM_MIN}-{NUM_MAX}): ', end='')
        pw_max_length = get_number_strict(input())

        print('Use lowercase letters? Y/N: ', end='')
        use_lowercase = is_answer_positive(input())
        print('Use uppercase letters? Y/N: ', end='')
        use_uppercase = is_answer_positive(input())
        print(f'Use special characters {SPECIAL_CHARS} ? Y/N: ', end='')
        use_special_chars = is_answer_positive(input())
        print(f'Use characters such as {OPTIONAL_CHARS} ? Y/N: ', end='')
        use_hard_read_chars = is_answer_positive(input())

        all_passwords = generate_password(pw_amount, pw_min_length, pw_max_length,
                                          use_lowercase, use_uppercase, use_special_chars, use_hard_read_chars)
        print(*all_passwords, sep='\n')


if __name__ == '__main__':
    safe_password = SafePassword()
