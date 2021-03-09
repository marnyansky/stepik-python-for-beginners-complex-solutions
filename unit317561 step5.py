"""
URL: https://stepik.org/lesson/334152/step/5?unit=317561
Интернет-магазин осуществляет экспресс-доставку своих товаров по цене 1000 рублей за первый товар и 120 рублей за каждый последующий товар
"""

def get_shipping_cost(quantity):
    return 120 * (quantity - 1) + 1000 if quantity > 0 else 0