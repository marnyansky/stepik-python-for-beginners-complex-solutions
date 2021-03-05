"""
url: https://stepik.org/lesson/327207/step/13?unit=310501
На вход программе подается натуральное число nn и nn строк, а затем число kk. Напишите программу, которая выводит kk-ую букву из введенных строк на одной строке без пробелов.
"""
data = [input() for i in range(int(input()))]
k = int(input())
for i in data:
    if len(i) >= k:
        print(i[k - 1], end='')