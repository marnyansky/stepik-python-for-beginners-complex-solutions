# url: https://stepik.org/lesson/265122/step/10?thread=solutions&unit=246071
# Цифры в числе в обратном порядке отсортированы по неубыванию (пример: 76544322)

n = input()
print('YES' if sorted(n, reverse=True) == list(n) else 'NO')