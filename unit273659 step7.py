#url: https://stepik.org/lesson/292172/step/7?thread=solutions&unit=273659

x1, x2, y1, y2 = int(input()), int(input()), int(input()), int(input())
if (abs(x1 - y1) == 1 and abs(x2 - y2) == 2) or (abs(x1 - y1) == 2 and abs(x2 - y2) == 1):
    print("YES")
else:
    print("NO")