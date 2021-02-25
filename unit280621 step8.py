#url: https://stepik.org/lesson/298794/step/8?unit=280621

#my solution:
limit = int(input())
i = 1
for i in range (1, limit + 1):
    if i not in range(5, 10):
        if i not in range(17, 38):
            if i not in range(78, 88):
                print(i)

#alternative solution:
n = int(input())
for i in range(1, n+1):
    if i in range(5, 10) or i in range(17, 38) or i in range(78, 88):
        continue  # переходим на следующую итерацию
    print(i)