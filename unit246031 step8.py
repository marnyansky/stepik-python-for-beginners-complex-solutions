n1, n2, s = int(input()), int(input()), input()
if s in ["+", "-", "*", "/"]:
    if s == "/":
        if n2 != 0:
            print(n1 / n2)
        else:
            print("На ноль делить нельзя!")
    else:
        d = {"+": n1 + n2, "-": n1 - n2, "*": n1 * n2}
        print(d[s])
else:
    print("Неверная операция")