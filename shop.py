class ShoppingCart():

    def __init__(self):
        self.bizname = "Coding Nannah's Stationery Store"
        username = None
        itemName = None
        self.invalidResponse = "That was not a valid response. Please try again."
        self.cart = {}

        self.merch = [
            {
                "id": 0,
                "name": 'Parker© Pen (blue)',
                "desc": 'blue + refill', 
                "price": 14.95
            },
            {
                "id": 1,
                "name": 'Parker© Pen (black)',
                "desc": 'black + refill', 
                "price": 14.95
            },
            {
                "id": 2,
                "name": 'Prismacolor© Drawing Pencils',
                "desc": 'multicolors', 
                "price": 42.97
            },
            {
                "id": 3,
                "name": 'Profession© Sketch Pencils',
                "desc": '6B to 4H black', 
                "price": 14.95
            },
            {
                "id": 4,
                "name": 'Mr. Pen© 8-pack Gel Highlighters',
                "desc": 'multi-colors', 
                "price": 8.95
            },
            {
                "id": 5,
                "name": 'Strathmore© Sketch Pad',
                "desc": '100 sheets', 
                "price": 14.95
            },
            {
                "id": 6,
                "name": 'Nannah© Planner',
                "desc": 'weekly', 
                "price": 17.95
            },
            {
                "id": 7,
                "name": 'Nannah© Journal',
                "desc": 'hardbound 500 pages', 
                "price": 21.95
            },
            {
                "id": 8,
                "name": 'Nannah© Notebook-D',
                "desc": '100 sheets - dots', 
                "price": 14.95
            },
            {
                "id": 9,
                "name": 'Nannah© Notebook-L',
                "desc": '100 sheets - lined', 
                "price": 14.95
            },
            {
                "id": 10,
                "name": 'Nannah© Notebook-G',
                "desc": '100 sheets - graphed', 
                "price": 14.95
            },
            {
                "id": 11,
                "name": 'Altoids© Mints',
                "desc": 'peppermint', 
                "price": 2.99
            }
        ]
        

    def showMerch(self):
        merchTable = (f"""  
            *********** Merchandise for Sale Today ***********

            {self.merch[0]["id"]}: {self.merch[0]["name"]}, {' '*20}{self.merch[0]["price"]}
            {self.merch[1]["id"]}: {self.merch[1]["name"]}, {' '*19}{self.merch[1]["price"]}
            {self.merch[2]["id"]}: {self.merch[2]["name"]}, {' '*10}{self.merch[2]["price"]}
            {self.merch[3]["id"]}: {self.merch[3]["name"]}, {' '*12}{self.merch[3]["price"]}
            {self.merch[4]["id"]}: {self.merch[4]["name"]}, {' '*7}{self.merch[4]["price"]}
            {self.merch[5]["id"]}: {self.merch[5]["name"]}, {' '*16}{self.merch[5]["price"]}
            {self.merch[6]["id"]}: {self.merch[6]["name"]}, {' '*23}{self.merch[6]["price"]}
            {self.merch[7]["id"]}: {self.merch[7]["name"]}, {' '*23}{self.merch[7]["price"]}
            {self.merch[8]["id"]}: {self.merch[8]["name"]}, {' '*20}{self.merch[8]["price"]}
            {self.merch[9]["id"]}: {self.merch[9]["name"]}, {' '*20}{self.merch[9]["price"]}
            {self.merch[10]["id"]}: {self.merch[10]["name"]}, {' '*19}{self.merch[10]["price"]}
            {self.merch[11]["id"]}: {self.merch[11]["name"]}, {' '*24}{self.merch[11]["price"]}
                
            100: None of These 

            ***************************************************
            """)

        print(merchTable)
        self.addItem()
    

    # Option 0 = exit
    def leave(self):
        # if cart, you must check out first!
        if self.cart:
            print(f"\n{self.username}, there are items in your cart. You must check out first!")
            self.showOptions()
        else:
            print(f"\n{self.username}, thank you for visiting {self.bizname}. Have an awesome day! ")


    # Option 1 = add merch
    def addItem(self):
        # total = 0 
        itemNumber = input('Type the Number of the item you would like to place in your cart: ').strip().lower()
        itemNumber = int(itemNumber)
        for item in self.merch:
            if itemNumber == 100:
                self.showOptions()
            elif itemNumber >=0 and itemNumber <= 11:
                itemName = self.merch[itemNumber]["name"]
                itemPrice = (self.merch[itemNumber]["price"])
                print(f"{self.username}, you have chosen to add {itemName} for {itemPrice:.2f} to your cart.")
                itemQuant = int(input(f"How many would you like to add? No commas, please. "))
                self.cart.update({itemName:{"quantity": itemQuant, "subtotal": itemPrice * itemQuant}})
                self.showCart()
            else:
               print(self.invalidResponse)
        contShop = input("Would you like to continue shopping? [y/n] ")
        if contShop == ("y","Y", "yes", "Yes"):
            self.addItem()
        else:
            self.showOptions()

    
    # Option 2 = show cart
    def showCart(self):
        print(f"\n{self.username}, here are the items currently in your cart:")
        # format cart to show
        print(self.cart)
        returnChoices = input("What would you like to do, now? [Options/Checkout] ")
        if returnChoices.strip().lower() == "options":
            self.showOptions()
        elif returnChoices.strip().lower() == "checkout":
            self.checkOut()
        else:
            print(self.invalidResponse)


    # Option 3 = remove from cart
    def removeItem(self):
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

    
    # Option 4 = clear cart
    def emptyCart(self):
        verifyEmpty = input(f"{self.username}, are you sure you want to empty your entire cart? [y/n] ")
        if verifyEmpty == ("y","Y", "yes", "Yes"):
            self.merch.clear()
            print(self.cart)
        else:
            self.showOptions()


    # Option 5 = checkout
    def checkOut(self):
        # calculate prices: UT sales tax = 6.1% or .061
        tax = float(subtotal) * .061
        # total = subtotal + float(tax)


        print(f'+++++Thank you, {self.name}, for shopping at Coding Nannah\'s Stationery Store!+++++')
        print('Here is your receipt. It was a pleasure to serve you!')
        print(f""" 
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                              
                    {self.name}", you found some great products today! 
                
                        You purchased {self.cart}.
            
                        Your subtotal = $({subtotal:.2f})
                    
                        +         tax = ${tax}
                        ___________________________
                            
                                total = $({total:.2f})

                Follow the link to securely pay for your merchandise.
            We hope you enjoyed your experience and visit us again soon!
                        
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""")
        
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
        choice = int(choices)

        if choice == 0:
            self.leave()
        elif choice == 1:
            self.showMerch() 
        elif choice == 2:
            self.showCart()
        elif choice == 3:
            self.removeItem()
        elif choice == 4:
            self.emptyCart()
        elif choice == 5:
            self.checkOut()
        else:
            print(self.invalidResponse)

    # run the program! + welcome/start --> showOptions (action choices)
    def run(self):
        print(f"""\n
         +++++ Welcome to {self.bizname}! +++++ """)
        
        # username obtained here in run - use everywhere!
        self.username = input("What's your name? ").strip().title()
        print(f"\nIt's a pleasure to serve you today, {self.username}!")

        self.showOptions()



shop = ShoppingCart()
shop.run()
