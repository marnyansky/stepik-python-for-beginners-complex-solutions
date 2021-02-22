# url: https://stepik.org/lesson/265115/step/9?thread=solutions&unit=246063

l = sorted([len(input()) for _ in '123'])
print('YES' if l[2] - l[1] == l[1] - l[0] else 'NO')