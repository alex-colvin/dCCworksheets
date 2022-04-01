from product import Product
class ShoppingCart:
    def __init__(self) -> None:
        self.products = []
        self.cart_cost = 0
    def calculate_cart_cost(self):
        for item in self.products:
            self.cart_cost += item.price
    def add_to_cart(self, product):
        self.products.append(product)
    def empty_cart(self):
        self.products.clear()
        self.cart_cost = 0

