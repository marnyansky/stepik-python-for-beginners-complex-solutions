#url: https://stepik.org/lesson/298796/step/3?unit=280623
#На вход программе подается два натуральных числа aa и bb (a < ba< b). Напишите программу, которая находит натуральное число из отрезка [a; \, b][a;b] с максимальной суммой делителей.


a, b = int(input()), int(input())
target, max_summ = -1, -1

for i in range (a, b+1):
    summ = 0
    for j in range (1, i+1):
        if i % j == 0:
            summ += j
        if summ >= max_summ:
            max_summ = summ
            target = j
print(target, max_summ)