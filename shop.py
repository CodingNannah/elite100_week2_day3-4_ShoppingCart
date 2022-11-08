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
                "short": 'Parker bu',
                "desc": 'blue + refill', 
                "price": 14.95
            },
            {
                "id": 1,
                "name": 'Parker© Pen (black)',
                "short": 'Parker bk',
                "desc": 'black + refill', 
                "price": 14.95
            },
            {
                "id": 2,
                "name": 'Prismacolor© Drawing Pencils',
                "short": 'Prisma',
                "desc": 'multicolors', 
                "price": 42.97
            },
            {
                "id": 3,
                "name": 'Profession© Sketch Pencils',
                "short": 'Pro sketch',
                "desc": '6B to 4H black', 
                "price": 14.95
            },
            {
                "id": 4,
                "name": 'Mr. Pen© 8-pack Gel Highlighters',
                "short": 'Mr Pen',
                "desc": 'multi-colors', 
                "price": 8.95
            },
            {
                "id": 5,
                "name": 'Strathmore© Sketch Pad',
                "short": 'Strath',
                "desc": '100 sheets', 
                "price": 14.95
            },
            {
                "id": 6,
                "name": 'Nannah© Planner',
                "short": 'Nan P',
                "desc": 'weekly', 
                "price": 17.95
            },
            {
                "id": 7,
                "name": 'Nannah© Journal',
                "short": 'Nan J',
                "desc": 'hardbound 500 pages', 
                "price": 21.95
            },
            {
                "id": 8,
                "name": 'Nannah© Notebook-D',
                "short": 'Nan D',
                "desc": '100 sheets - dots', 
                "price": 14.95
            },
            {
                "id": 9,
                "name": 'Nannah© Notebook-L',
                "short": 'Nan L',
                "desc": '100 sheets - lined', 
                "price": 14.95
            },
            {
                "id": 10,
                "name": 'Nannah© Notebook-G',
                "short": 'Nan G',
                "desc": '100 sheets - graphed', 
                "price": 14.95
            },
            {
                "id": 11,
                "name": 'Altoids© Mints',
                "short": 'Mints',
                "desc": 'peppermint', 
                "price": 2.99
            }
        ]


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
                
            -1: None of These 

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
            if itemNumber == -1:
                self.showOptions()
            elif itemNumber >=0 and itemNumber <= 11:
                itemName = self.merch[itemNumber]["name"] 
                itemPrice = self.merch[itemNumber]["price"]
                shortName = self.merch[itemNumber]["short"]
                print(f"\n{self.username}, you have chosen to add {itemName} for {itemPrice} to your cart.")
                
                # how many?
                itemQuant = int(input(f"\nHow many would you like to add? (Type without commas. System doesn't accept them.) "))
                # fix decimal spaces 
                itemSubtotal = "{:.2f}".format((itemPrice) * int(itemQuant))

                # update cart with quantity & price - no separate Total to track
                self.cart.update({itemName:{"short": shortName,"quantity": itemQuant, "price": itemPrice, "subtotal": itemSubtotal}})
                self.showCart()
            else:
               print(self.invalidResponse)


    # Option 2 = show cart
    def showCart(self):
        print(f"\n{self.username}, here are the items currently in your cart:")
        # format cart to show
        print(self.cart)
        returnChoices = input("What would you like to do, now? [Options/Checkout/Shop] ")
        if returnChoices.strip().lower() == "options":
            self.showOptions()
        elif returnChoices.strip().lower() == "checkout":
            self.checkOut()
        elif returnChoices.strip().lower() == "shop":
            self.addItem()
        else:
            print(self.invalidResponse)


    # Option 3 = remove from cart
    def removeItem(self):
        # warning
        print("*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*")
        print(
            f"\n*!*!  WARNING: At this time, {self.username}, 'Remove Item' is under construction.")
        print("*!*!  Any item you remove will remove ALL of that item from your cart.")
        print("*!*!  If you wish to retain a lesser amount of that item in your cart,")
        print("*!*!  you will be required to add it again to your cart.")
        print("*!*!  In the event your item is not removed from the cart, contact the Service Desk.")
        print('')
        print("*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!")
        understand = input(f"\nDo you understand the repercussions of removing an item from your cart? [y/n]")
        if understand == ("n", "N", "no", "No"):
            self.showOptions()

        # check remove (input[y/n])
        checkRemove = input(f"\nDo you wish to proceed and remove all of a particular item from your cart? [y/n] ")
        if checkRemove == ("n", "N", "no", "No"):
            self.showOptions()

        print(f"\nHere are the items currently in your cart, {self.username}:")
        print(self.cart)
        removeItem = input(f"Type the short name of the item you wish to remove from your cart: ").strip().lower()
        removeQuant = int(input("How many would you like to remove? "))
        itemName = self.merch[removeItem]["name"] 

        try:
            if itemName in self.cart:
                self.cart.delete(itemName)
                # ({itemName:{"quantity": itemQuant, "subtotal": itemPrice * itemQuant}})
                print(f"{self.username}, you have chosen to remove all of {removeItem} from your cart.")
                print(self.cart) 
                self.showOptions()
        except:
            self.showOptions()

    
    # Option 4 = clear cart
    def emptyCart(self):
        verifyEmpty = input(f"{self.username}, are you sure you want to empty your entire cart? [y/n] ")
        if verifyEmpty == ("y","Y", "yes", "Yes"):
            self.cart.clear()
            print(self.cart)
            self.showOptions()
        else:
            self.showOptions()


    # Option 5 = checkout
    def checkOut(self):
            verifyCheckOut = input(f"{self.username}, are you sure you want to checkout now? [y/n] ")
            if verifyCheckOut == ("n","N", "no", "No"):
                self.showOptions()
            else:
                for item in self.cart:
                    itemName = self.merch[itemName]
                    itemPrice = "{:.2f}".format(self.merch[itemName]["price"])
                    itemQuant = self.cart[itemName]["quantity"]
                    itemSubtotal = "{:.2f}".format((itemPrice) * int(itemQuant))
                    tax = float(itemSubtotal) * .061
                    total = "{:.2f}".format(itemSubtotal) + "{:.2f}".format(tax)

                # self.cart.update({itemShort:{"quantity": itemQuant, "subtotal": itemSubtotal}}) 
                # calculate prices: UT sales tax = 6.1% or .061
                

                print("\n")
                print(f""" 
                ++++++++++++++++++ Sales Receipt ++++++++++++++++++                            
                        
                        {self.username}, you purchased {self.cart}.
                                Your tax is {tax}.
                            For a total of ${total}.
                                           
                                    
                Thank you for shopping at Coding Nannah\'s Stationery Store!
                        It was a pleasure serving you, {self.username}!

                    +++++++++++++++++++++++ +++++++++++++++++++++++ 
            """)    
                
   
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
