from shop import apply_discount, cart_total


def test_discount():
    assert apply_discount(200, 10) == 180


def test_total():
    assert cart_total([{"price": 10, "qty": 2}, {"price": 5, "qty": 1}]) == 25
