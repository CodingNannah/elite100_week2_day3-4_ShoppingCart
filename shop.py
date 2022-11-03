"""
1) Takes in input - ask the user 5 bits of input:
    * Do you want to: Add/Show/Delete/Clear or Quit?   
2) Stores user input into a dictionary or list
    cart = ["item", "price"]
    cart = {"item": '', "price": ''}
3) The User can add or delete items
    * empty shopping cart (list or dictionary)
    * removed all .strip(), elif or else should cover them
4) The User can see current shopping list
5) The program Loops until user 'quits'
6) Upon quitting the program, print out all items in the user's list
"""

class ShoppingCart():

    def __init__(self):
        self.bizname = "Coding Nannah's Stationery Store"
        self.username = self.run("username")
        self.invalidResponse = "That was not a valid response. Please try again."
        self.cart = {}
        

    def showMerch(self):
        merch = [
            {
                "id": "a",
                "name": 'Parker© Pen (blue)',
                "desc": 'blue + refill', 
                "price": 14.95
            },
            {
                "id": "b",
                "name": 'Parker© Pen (black)',
                "desc": 'black + refill', 
                "price": 14.95
            },
            {
                "id": "c",
                "name": 'Prismacolor© Drawing Pencils',
                "desc": 'multicolors', 
                "price": 42.97
            },
            {
                "id": "d",
                "name": 'Profession© Sketch Pencils',
                "desc": '6B to 4H black', 
                "price": 14.95
            },
            {
                "id": "e",
                "name": 'Mr. Pen© 8-pack Gel Highlighters',
                "desc": 'multi-colors', 
                "price": 8.95
            },
            {
                "id": "f",
                "name": 'Strathmore© Sketch Pad',
                "desc": '100 sheets', 
                "price": 14.95
            },
            {
                "id": "g",
                "name": 'Nannah© Planner',
                "desc": 'weekly', 
                "price": 17.95
            },
            {
                "id": "h",
                "name": 'Nannah© Journal',
                "desc": 'hardbound 500 pages', 
                "price": 21.95
            },
            {
                "id": "i",
                "name": 'Nannah© Notebook-D',
                "desc": '100 sheets - dots', 
                "price": 14.95
            },
            {
                "id": "j",
                "name": 'Nannah© Notebook-L',
                "desc": '100 sheets - lined', 
                "price": 14.95
            },
            {
                "id": "k",
                "name": 'Nannah© Notebook-G',
                "desc": '100 sheets - graphed', 
                "price": 14.95
            },
            {
                "id": "l",
                "name": 'Altoids© Mints',
                "desc": 'peppermint', 
                "price": 2.99
            }
        ]

        merchTable = (f"""
                
            *********** Merchandise for Sale Today ***********
            {merch[0]["id"]}: {merch[0]["name"]}, {' '*20}{merch[0]["price"]}
            {merch[1]["id"]}: {merch[1]["name"]}, {' '*19}{merch[1]["price"]}
            {merch[2]["id"]}: {merch[2]["name"]}, {' '*10}{merch[2]["price"]}
            {merch[3]["id"]}: {merch[3]["name"]}, {' '*12}{merch[3]["price"]}
            {merch[4]["id"]}: {merch[4]["name"]}, {' '*7}{merch[4]["price"]}
            {merch[5]["id"]}: {merch[5]["name"]}, {' '*16}{merch[5]["price"]}
            {merch[6]["id"]}: {merch[6]["name"]}, {' '*23}{merch[6]["price"]}
            {merch[7]["id"]}: {merch[7]["name"]}, {' '*23}{merch[7]["price"]}
            {merch[8]["id"]}: {merch[8]["name"]}, {' '*20}{merch[8]["price"]}
            {merch[9]["id"]}: {merch[9]["name"]}, {' '*20}{merch[9]["price"]}
            {merch[10]["id"]}: {merch[10]["name"]}, {' '*20}{merch[10]["price"]}
            {merch[11]["id"]}: {merch[11]["name"]}, {' '*25}{merch[11]["price"]}
                
            z: None of These 
            ***************************************************
                
            """)

        print(merchTable)
        self.addItem("itemLetter")
    
    # Option 0 = exit
    def leave(self):
        # if cart, you must check out first!
        if self.cart:
            print(f"\n{self.username}, there are items in your cart. You must check out first!")
            self.showOptions()
        else:
            print(f"\n{self.username}, thank you for visiting {self.bizname}. Have an awesome day! ")


    # Option 1 = add merch
    def addItem(self, merch):
        self.showMerch() 
        # total = 0 
        itemLetter = input('Type the letter of the item you would like to place in your cart: ').strip().lower()
        for item in merch:
            if itemLetter == merch["id"]:
                itemName = merch["name"]
                itemPrice = float(merch["price"])
                print(f"{self.username}, you have chosen to add {itemName} for {itemPrice} to your cart.")
                itemQuant = int(input(f"How many would you like to add? "))
                self.cart.update({itemName:{"quantity": itemQuant, "subtotal": itemPrice * itemQuant}})
                self.showCart()
            else:
               print(self.invalidResponse)
        
    
    # Option 2 = show cart
    def showCart(self):
        print(f"\n{self.username}, here are the items currently in your cart:")
        # format cart to show
        print(self.cart)
        self.showOptions()

    # Option 3 = remove from cart
    def removeItem(self):
        pass    
    
    # Option 4 = clear cart
    def emptyCart(self):
        pass

    # Option 5 = checkout
    def checkOut(self):
        # calculate prices
        pass
        
    def showOptions(self):
        options = ("""   

        ***** Online Shopping Menu *****
            1: Add Merchandise
            2: Show Cart
            3: Remove Merchandise
            4: Clear Cart
            5: Check Out
            0: Quit
        ********************************* 

        """)
        print(options)
        choices = input(f"\n{self.username}, type the number of what you would you like to do? ")
        
        if choices == 0:
            self.leave()
        elif choices == 1:
            self.addItem()
        elif choices == 2:
            self.showCart()
        elif choices == 3:
            self.removeItem()
        elif choices == 4:
            self.emptyCart()
        elif choices == 5:
            self.checkOut()
        else:
            print(self.invalidResponse)

    # run the program! + welcome/start --> showOptions (action choices)
    def run(self):
        print(f"""
        \n+++++ +++++ +++++ Welcome to {self.bizname}! +++++ +++++ +++++\n""")
        
        # username obtained here in run - use everywhere!
        username = input("What's your name? ").strip().title()
        print(f"\nIt's a pleasure to serve you today, {username}!")

        self.showOptions()



shop = ShoppingCart()
shop.run()
