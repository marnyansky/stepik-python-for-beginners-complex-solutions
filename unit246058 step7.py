# url: https://stepik.org/lesson/265110/step/7?thread=solutions&unit=246058
from math import sqrt

a, b, c = float(input()), float(input()), float(input())
discr = b**2 - 4*a*c

if discr < 0:
    print('Нет корней')
elif discr == 0:
    print(-b / (2*a))
elif d > 0:
    x1 = (-b - discr ** 0.5) / (2*a)
    x2 = (-b + discr ** 0.5) / (2*a)
    print(min(x1, x2))
    print(max(x1, x2))