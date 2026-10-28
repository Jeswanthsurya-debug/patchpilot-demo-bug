def apply_discount(price, percent):
    return price - price * percent


def cart_total(items):
    return sum(i["price"] * i["qty"] for i in items)
