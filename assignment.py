def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        print (price*discount_percent/100)
    else:
        print(price)

print(calculate_discount(300, 40))
