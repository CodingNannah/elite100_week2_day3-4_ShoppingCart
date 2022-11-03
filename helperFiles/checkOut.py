 """
        #UT sales tax = 6.1% or .061
tax = float(subtotal) * .061
total = subtotal + float(tax)


print(f'+++++Thank you, {name}, for shopping at Coding Nannah\'s Stationery Store!+++++')
print('Here is your receipt. It was a pleasure to serve you!')
print(f""" 

        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                              
                    {name}", you found some great products today! 
                
                        You purchased {cart}.
            
                        Your subtotal = $(%.2f{subtotal})
                    
                        +         tax = ${tax}
                        ___________________________
                            
                                total = $(%.2f{total})

                Follow the link to securely pay for your merchandise.
                            
            We hope you enjoyed your experience and visit us again soon!
                        
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

""")

        """