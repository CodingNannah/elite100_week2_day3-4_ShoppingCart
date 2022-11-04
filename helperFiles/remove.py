 # Option 3 = remove from cart
    def removeItem(self):
        #  from addItem - 
        self.itemName     
                # self.cart.update({itemName ({itemName["short"]}):{"quantity": itemQuant, "subtotal": itemPrice * itemQuant}})
        remove = input(f"What would you like to remove from your cart, {self.username}? [name of item] ").strip().lowercase()
        removeQty = int(input("How many would you like to remove? "))
        for item in self.cart:
            if remove == self.itemName.strip().lower():
                self.cart.remove(self.itemName*removeQty)
                # ({itemName:{"quantity": itemQuant, "subtotal": itemPrice * itemQuant}})
                return self.cart  
            else:
                print(self.invalidResponse)
        self.showOptions()