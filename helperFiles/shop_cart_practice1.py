cartItems = []
cartTotal = 0

def addItem(itemName, itemPrice):
    cartItems.append(itemName)
    # cartTotal += itemPrice
    return itemPrice

# cartSummary = {"Item": "Quantity"}

# for i in range(0, len(cartItems)):
#     # prints all in a line
#     print(cartItems[i])

# for item in cartItems:
#     # prints all in a line
#     print(item)

cartSummary = dict((item, cartItems.count(item))for item in cartItems)
print(cartSummary)
print(cartTotal)