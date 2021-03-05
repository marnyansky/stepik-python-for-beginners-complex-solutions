"""
url: https://stepik.org/lesson/313233/step/7?thread=solutions&unit=295750
На вход программе подается строка текста. Напишите программу, которая удаляет из нее все символы, кратные 3, то есть символы с индексами 0, 3, 6, ....
"""

# v1:
s = input()
for i in range(len(s)):
    if i % 3 != 0:
        print(s[i], end='')

# v2:
s = list(input())
del s[0::3]
print(*s, sep='')

# v3:
s = input()
for k,v in enumerate(s):
    if k % 3 != 0:
        print(s, end='')