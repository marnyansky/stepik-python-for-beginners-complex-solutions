"""
URL: https://stepik.org/lesson/334150/step/4?unit=317559
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое число большее числа num (т. е. для числа 7 функция должна возвращать 11)
"""

# my solution:
def get_next_prime(num):
    while True:
        num += 1
        factors = [i for i in range(1, num+1) if num % i == 0]
        if len(factors) == 2:
            return num

# alternative solution:
def get_next_prime(num):
    num += 1
    for i in range(2, num):
        if num % i == 0:
            return get_next_prime(num)
    return num
