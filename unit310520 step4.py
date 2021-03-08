"""
URL: https://stepik.org/lesson/327221/step/4?unit=310520
Напишите программу, которая определяет является ли введенная строка корректным телефонным номером (форматы: 012-345-6789 и 7-012-345-6789)
"""

#my solution:
answer = 'NO'
lst = [int(i) for i in input().split('-') if i.isdigit()]
if len(lst) == 3 or (len(lst) == 4 and (lst[0] == 7)):
    if 1000 <= lst[-1] <= 9999:
        if 100 <= lst[-2] <= 999:
            if 100 <= lst[-3] <= 999:
                answer = 'YES'
print(answer)

#alternative solution:
n = input().split("-")
c = [len(i) for i in n] 
if c == [3, 3, 4] and ''.join(n).isdigit(): 
    print("YES")
elif c == [1, 3, 3, 4] and ''.join(n).isdigit() and n[0] == '7': 
    print("YES")
else:
    print("NO")