# Four Assignments Here:
    * Shopping Cart as shop.py
    * Function for Square Footage as square_footage.py
    * Function for Circumference as circumference.py
    * Class with two String Methods as class_string_methods.py

    Wednesday_My_Homework.ipynb = previous non-working iterations

### Build a Shopping Cart
Create a Shopping Cart, using either lists or dictionaries. 

The program should have the following capabilities:

1) Takes in input - ask the user 5 bits of input:
    * Do you want to: Add/Show/Delete/Clear or Quit?   
2) Stores user input into a dictionary or list
    cart = ["item", "price"]
    cart = {"item": '', "price": ''}
3) The User can add or delete items
    * empty shopping cart (list or dictionary)
4) The User can see current shopping list
5) The program Loops until user 'quits'
6) Upon quitting the program, print out all items in the user's list


### Square Footage Calculator
Create a function to calculate the square footage of a house by taking in user 
input and imported functions.

* Reminder of Formula: Length X Width == Area

* input: user in string? to floats
* output: square feet in float or ave up integer
* function: def square_footage
* constraint: use imported function


### Circumference Calculator
Create a function to calculate the circumference of a circle by taking in user 
input and imported functions.

* input: user radius or diameter or area in integer(s) or float(s)
* output: circumference in integer or float
* constraint: use imported function = math pi
* knowledge: circumference is distance around the circle (not area!)
    uses pi * 1 diameter or 2 radius:
    *  c = pi(d) or c = 2pi(r)
    *  if area is provided: c = 2 * ((square root of) (pi*a))
* def function = def circumference_of_circle():
* calculate circumference:
    * float '%.2f' % num or '{:.2f}'.format(num) 
https://stackoverflow.com/questions/6149006/how-to-display-a-float-with-two-decimal-places


### Class String Methods
Write a Python class which has two methods: get_String and print_String. 
* get_String accepts a string from the user.
* print_String print the string in upper case


#### Personal Notes
How to treat quantities? - fixed: within the cart dict
* watch for strings & int/floats!

Call from other functions within the class:
* "You need an instance of your class and use the instance to do .. instance.method_name(parameters) ...get your instance by doing instance = ClassName(params_for_init_method)" 
                                    - Kevin, the Almighty Dev

Add "small name" to items for merch dict; use interchangeably with cart dict
* easier for user to del later, while maintaining integrity of full name
