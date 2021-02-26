#url: https://stepik.org/lesson/298796/step/7?unit=280623
#На вход программе подается два натуральных числа a и b (a < b). Напишите программу, которая находит все простые числа от a до b включительно.

a, b = int(input()), int(input())

for i in range(a, b+1):
    num_total_divs = 1 # все числа делятся на 1
    for j in range(2, b + 1): # перебираем делители
        if i < j:
            break # сокращаем количество итераций примерно на 49,5%
        if i % j == 0:
            num_total_divs += 1
    if num_total_divs == 2:
        print(i)