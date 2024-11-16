# Create a function named calculate_discount(price, discount_percent) 
# that calculates the final price after applying a discount. 
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters.
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.


def calculate_discount(price, discount_percent):
  price = 300.0
  discount_percent = 0.30
  if discount_percent < 0.20:
    return price
  else:
    return price - (discount_percent * price) 
x = calculate_discount(1,1)
print(x)

# Using the calculate_discount function, prompt the user to enter the original price of an item 
# and the discount percentage. 
# Print the final price after applying the discount, 
# or if no discount was applied, print the original price.


def calculate_discount(price, discount_percent):
  price = float(input("Enter the Price in decimals:"))
  discount_percent = float(input("Enter the discount_percent in decimals:"))
  if discount_percent < 0.20:
    return price
  else:
    return price - (discount_percent * price) 
x = calculate_discount(1,1)
print(x)
