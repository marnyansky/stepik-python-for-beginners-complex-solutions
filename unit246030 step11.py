# url: https://stepik.org/lesson/265082/step/11?thread=solutions&unit=246030
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if b1 >= a2:
    if b1 == a2:
        print (b1)
    elif a1 == b2:
        print (a1)
    elif b1 > a2:
        print(str(a2) + " " + str(b1))
    elif b2 > a1:
        print(str(a1) + " " + str(b2))
else:
    print('пустое множество')