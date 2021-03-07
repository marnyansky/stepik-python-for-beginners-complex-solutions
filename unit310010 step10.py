"""
url: https://stepik.org/lesson/326725/step/10?unit=310010
На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая выводит все цифровые символы данной строки.
"""

#my solution:
print(*[int(i) for i in input() if '0' <= i <= '9'], sep='')

#alternative solution:
print(*(i for i in input() if i.isdigit()), sep='')