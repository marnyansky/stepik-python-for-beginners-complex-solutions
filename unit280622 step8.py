# url: 
# Дано нечетное натуральное число nn. Напишите программу, которая печатает равнобедренный звездный треугольник с основанием, равным nn

n = int(input())
for i in range (1, (n+1)//2 + 1):
    print(i * '*')
for i in range ((n-1)//2, 0, -1):
    print(i * '*')