class Order:
    def __init__(self, item, price):
        self.item = item
        self.price =  price

    def __gt__(self, price):
        return self.price > order2.price

order1 = Order("poteto chips", 63)
order2 = Order("tea", 50)


print(order1 > order2)