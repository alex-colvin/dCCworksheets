from customer import Customer
from product import Product
customer = Customer('Alex')
avocado = Product("avocado", 4.99, "produce")
tomato = Product("tomato", .99, "produce")
onion = Product("onion", .59, "produce")
# 1. Print the customer’s name to the terminal
print(customer.name)
# Alex
# 2. Call the customer’s add product to shopping cart method three times and add the three products objects you created
customer.add_item_to_cart(avocado)
customer.add_item_to_cart(tomato)
customer.add_item_to_cart(onion)
# 3. Call the customer’s view products method
customer.view_cart()
# avocado
# tomato
# onion
# 4. Call the customer’s shopping cart’s get cart total method. Capture the total the method returns in a variable and print to the terminal
customer.cart.calculate_cart_cost()
total_cost = customer.cart.cart_cost
print(total_cost)
# 6.57
# 5. Call the customer’s shopping cart’s empty cart method
customer.cart.empty_cart()
# 6. Check if all products have been removed from the shopping cart
customer.view_cart()
# Your cart is empty :(