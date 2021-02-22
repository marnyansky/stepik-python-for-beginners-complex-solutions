# url: https://stepik.org/lesson/265121/step/8?thread=solutions&unit=246070
# print str while str not value

# v1:
while True:
    s = input()
    if s == 'КОНЕЦ':
        break
    print(s)

# v2:
print(*iter(input, 'КОНЕЦ'), sep='\n')