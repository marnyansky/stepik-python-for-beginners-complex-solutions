# url: https://stepik.org/lesson/298796/step/1?unit=280623
# Дано натуральное число nn. Напишите программу, которая печатает численный треугольник с высотой равной nn

height = int(input())
disp_num = 1
count = 1
for i in range(height):
    for j in range(count):
        print(disp_num, end=' ')
        disp_num += 1
    print()
    count += 1