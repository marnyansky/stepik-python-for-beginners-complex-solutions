"""
https://stepik.org/lesson/298796/step/2?unit=280623
Дано натуральное число nn. Напишите программу, которая печатает численный треугольник с высотой равной nn, в соответствии с примером:
1
121
12321
1234321
123454321
"""

# v1
n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print(j + 1, end="")
    for j in range(i, 1, -1):
        print(j - 1, end="")
    print()

# v2
numbers = []
for i in range(1, height+1):
     numbers.append(str(i))
     print(''.join(numbers + numbers[-2::-1]))