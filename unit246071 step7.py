"""
https://stepik.org/lesson/265122/step/7?unit=246071
Дано натуральное число. Напишите программу, которая вычисляет:
+ сумму его цифр;
+ количество цифр в нем;
+ произведение его цифр;
+ среднее арифметическое его цифр;
+ его первую цифру;
+ сумму его первой и последней цифры.
"""

# best solution:

from functools import reduce
n = [int(i) for i in input()]
print(sum(n), len(n), reduce(lambda x, y: x * y, n), sum(n) / len(n), n[0], n[0] + n[-1], sep='\n')

# my solution:

num_str = input()
num = int(num_str)

amount_num = len(num_str)
num_last_is_first = -1
sum_num, avg_num, sum_first_last_nums = 0, 0, 0
mult_num = 1

num_tmp = num
while num_tmp > 0:
    sum_num += num_tmp % 10
    mult_num *= num_tmp % 10
    num_last_is_first = num_tmp
    num_tmp = num_tmp // 10
    
avg_num = sum_num / amount_num
sum_first_last_nums = num_last_is_first + (num % 10)

print(sum_num, amount_num, mult_num, avg_num, num_last_is_first, sum_first_last_nums, sep = '\n')