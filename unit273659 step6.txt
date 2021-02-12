# https://stepik.org/lesson/292172/step/6?thread=solutions&unit=273659
# Условие x1 - y1 == x2 - y2 соответствует одной диагонали, а условие x1 + y1 == x2 + y2 -- другой диагонали. Так как слон ходит по обоим диагоналям, то используем логическую операцию or:

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2):
    print('YES')
else:
    print('NO')