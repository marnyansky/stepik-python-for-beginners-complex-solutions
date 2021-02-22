# url: https://stepik.org/lesson/265121/step/14?thread=solutions&unit=246070
# coins: 25, 10, 5, 1. How many coins to pay an amount?

x = int(input())
coin = 0
while x != 0:
    for i in (25, 10, 5, 1):
        coin = coin + (x // i)
        x %= i
print(coin)