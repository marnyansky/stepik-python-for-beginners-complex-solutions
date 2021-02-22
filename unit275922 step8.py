# url: https://stepik.org/lesson/294243/step/8?thread=solutions&unit=275922

s = 0
for i in range(1, int(input()) + 1):
    if i ** 2 % 10 in [2, 5, 8]:
        s += i
print(s)