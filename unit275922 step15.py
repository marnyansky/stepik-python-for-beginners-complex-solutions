# url: https://stepik.org/lesson/294243/step/15?thread=solutions&unit=275922
# Fibonacci sequence

n = int(input())
a, b = 1, 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b