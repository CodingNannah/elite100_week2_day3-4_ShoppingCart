def addItem(self, itemName, itemPrice):
        # fix this! empty cart & empty total every time addItem() starts
        
        self.showMerch()
        item = input('Type the letter of the item you would like to place in your cart: ').strip().lower()

        if item == "a":
            pass
        #{
        #     a: Parker© Pen - blue 
        #     b: Parker© Pen - black
        #     c: Prismacolor© Drawing Pencils - multicolors
        #     d: Profession© Sketch Pencils - 6B to 4H black
        #     e: Mr. Pen© 8-pack Gel Highlighters - multi-colors
        #     f: Strathmore© Sketch Pad - 100 pages
        #     g: Nannah© Planner - weekly
        #     h: Nannah@ Journal - hardbound, 500 pages
        #     i: Nannah© Notebook - 100 pages, dots
        #     j: Nannah© Notebook - 100 pages, lined
        #     k: Nannah© Notebook - 100 pages, graphed
        #     l: Altoids© Mints - peppermint
        # }
            
            quantity = input(f"How many of item {item} would you like? ") 
            # quantity is a number string
            if quantity > 0:
                print(f"You have added {quantity} of item {item} to your cart.")
                # add total quantity of items to cart
                cart.append(item * quantity)
                # add total cost of items to total
                total.append(price * quantity)
            elif quantity == 0:
                self.showMerch()
            else:
                print(self.invalidResponse)
        elif item == "z":
            self.showOptions()
        else:
            print(self.invalidResponse)