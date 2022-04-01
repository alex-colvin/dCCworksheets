from shopping_cart import ShoppingCart
class Customer:
    def __init__(self, name) -> None:
        self.name = name
        self.cart = ShoppingCart()
    def add_item_to_cart(self, product):
        self.cart.add_to_cart(product)
    def view_cart(self):
        if len(self.cart.products) == 0:
            print("Your cart is empty :(") 
        for item in self.cart.products:
            print(item.name)