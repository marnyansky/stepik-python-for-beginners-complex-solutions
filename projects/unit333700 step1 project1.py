"""
Проект:
    "Угадайка чисел" / "Guess the Number"
Описание проекта:
    Программа генерирует случайное число в диапазоне от 1 до 100 и просит пользователя угадать это число.
    Если догадка пользователя больше случайного числа, то программа должна вывести сообщение 'Слишком много,
    попробуйте еще раз'. Если догадка меньше случайного числа, то программа должна вывести сообщение 'Слишком мало,
    попробуйте еще раз'. Если пользователь угадывает число, то программа должна поздравить его и вывести сообщение
    'Вы угадали, поздравляем!'.
"""

import random

left_border = 1
right_border = 100
attempts = 1

MESSAGE_SUCCESS = 'Вы угадали, поздравляем!'
MESSAGE_TOO_BIG = 'Слишком много, попробуйте еще раз'
MESSAGE_TOO_SMALL = 'Слишком мало, попробуйте еще раз'


class GuessRandomNumber:

    def __init__(self):
        self.guess_target_number_until_success()

    def verify_and_return_number(self, x):
        try:
            if left_border <= int(x) <= right_border:
                return int(x)
            print(f'Ошибочное число! Введите целое число от {left_border} до {right_border}')
            return False
        except ValueError:
            print(f'Ошибка ввода! Введите целое число от {left_border} до {right_border}')
            return False

    def compare_numbers(self, attempt_number, target_number):
        if attempt_number == target_number:
            print(MESSAGE_SUCCESS)
            exit()
        elif attempt_number < target_number:
            print(MESSAGE_TOO_SMALL)
        elif attempt_number > target_number:
            print(MESSAGE_TOO_BIG)
        return False

    def guess_target_number_until_success(self):
        target_number = random.randint(left_border, right_border)
        print(f'Мы загадали число от {left_border} до {right_border} включительно - отгадайте его!')

        while True:
            global attempts
            print(f'Попытка №{attempts}: ', end='')
            attempts += 1
            attempt_number = self.verify_and_return_number(input())
            if attempt_number:
                self.compare_numbers(attempt_number, target_number)


if __name__ == '__main__':
    new_random = GuessRandomNumber()
