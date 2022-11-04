# Big, Expandable Program
# Shelved for later: time crunch issues!

class Store():
    def __init__(self):
        # global variables:
        self.store = "Coding Nannah's Stationery Store"
        self.invalidResponse = "That was not a valid response. Please try again."
        self.cartItems = []
        self.cartTotal = 0
        self.merch = [
            {
                "id": 'a',
                "name": 'Parker© Pen - blue',
                "desc": 'blue + refill', 
                "price": 14.95
            },
            {
                "id": 'b',
                "name": 'Parker© Pen - black',
                "desc": 'black + refill', 
                "price": 14.95
            },
            {
                "id": 'c',
                "name": 'Prismacolor© Drawing Pencils',
                "desc": 'multicolors', 
                "price": 42.97
            },
            {
                "id": 'd',
                "name": 'Profession© Sketch Pencils',
                "desc": '6B to 4H black', 
                "price": 14.95
            },
            {
                "id": 'e',
                "name": 'Mr. Pen© 8-pack Gel Highlighters',
                "desc": 'multi-colors', 
                "price": 8.95
            },
            {
                "id": 'f',
                "name": 'Strathmore© Sketch Pad',
                "desc": '100 sheets', 
                "price": 14.95
            },
            {
                "id": 'g',
                "name": 'Nannah© Planner',
                "desc": 'weekly', 
                "price": 17.95
            },
            {
                "id": 'h',
                "name": 'Nannah© Journal',
                "desc": 'hardbound 500 pages', 
                "price": 21.95
            },
            {
                "id": 'i',
                "name": 'Nannah© Notebook-D',
                "desc": '100 sheets - dots', 
                "price": 14.95
            },
            {
                "id": 'j',
                "name": 'Nannah© Notebook-L',
                "desc": '100 sheets - lined', 
                "price": 14.95
            },
            {
                "id": 'k',
                "name": 'Nannah© Notebook-G',
                "desc": '100 sheets - graphed', 
                "price": 14.95
            },
            {
                "id": 'l',
                "name": 'Altoids© Mints',
                "desc": 'peppermint', 
                "price": 2.99
            }
        ]

    def exit(self):
        print("**************************************************************")
        print(f"\nThank you for visiting {self.store}! Have a terrific day!")

    def showCart(self):
        print(cart)

    def showMerch(self):
        merchTable = ("""
                
            *********** Merchandise for Sale Today ***********
            a: Parker© Pen - blue 
            b: Parker© Pen - black
            c: Prismacolor© Drawing Pencils - multicolors
            d: Profession© Sketch Pencils - 6B to 4H black
            e: Mr. Pen© 8-pack Gel Highlighters - multi-colors
            f: Strathmore© Sketch Pad - 100 pages
            g: Nannah© Planner - weekly
            h: Nannah@ Journal - hardbound, 500 pages
            i: Nannah© Notebook - 100 pages, dots
            j: Nannah© Notebook - 100 pages, lined
            k: Nannah© Notebook - 100 pages, graphed
            l: Altoids© Mints - peppermint
                
            z: None of These 
            ***************************************************
                
            """)
        print(merchTable)

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

    def run(self):    
        while True:
            # Welcome message/start:
            name = input('What is your name? ').title().strip()
            

            print(f'\n+++++ Welcome, {self.name}, to {self.store}! +++++\n')            
            
            print(self.options)
            optchoice = input('Type the number of what you would like to do: ')
            
            if optchoice == "0":
                self.exit()
                break
            
            elif optchoice == "1":
                self.addItem()

            elif optchoice == "2":
                # calc totals
                # show cart
                # back to optchoiceions
                pass

            elif optchoice == "3":
                # optchoiceion how many?
                # msg of removal
                # calc totals
                # show cart
                # back to optchoiceions
                pass

            elif optchoice == "4":
                # clear cart
                # show cart
                # back to optchoiceions
                pass

            elif opt == "5":
                # calc totals
                # show cart
                # msg to link
                # thanks
                # end
                pass

            else:
                # not a valid option
                pass


# #UT sales tax = 6.1% or .061
# tax = float(subtotal) * .061
# total = subtotal + float(tax)


# print(f'+++++Thank you, {name}, for shopping at Coding Nannah\'s Stationery Store!+++++')
# print('Here is your receipt. It was a pleasure to serve you!')
# print(f""" 

#         +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                              
#                     {name}", you found some great products today! 
                
#                         You purchased {cart}.
            
#                         Your subtotal = $(%.2f{subtotal})
                    
#                         +         tax = ${tax}
#                         ___________________________
                            
#                                 total = $(%.2f{total})

#                 Follow the link to securely pay for your merchandise.
                            
#             We hope you enjoyed your experience and visit us again soon!
                        
#         +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# """)
