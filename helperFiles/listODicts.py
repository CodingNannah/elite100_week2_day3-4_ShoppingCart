merch = [
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

# print(merch[0]["name"],":", merch[0]["price"])

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
            {merch[10]["id"]}: {merch[10]["name"]}, {' '*19}{merch[10]["price"]}
            {merch[11]["id"]}: {merch[11]["name"]}, {' '*24}{merch[11]["price"]}
                
            100: None of These 
            ***************************************************
                
            """)
# print(merchTable)

for item in merch:
    print(item)

# merch.clear()
# print(merch)