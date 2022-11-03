from cmath import pi #auto-generated from Import math
from colorama import Fore, Style

def circumference():
    print("\n******** Welcome to the Circle Circumference Calculator! ********")

    choice = input("Do you have a radius or a diameter? ")
    if choice == "radius":
        radius = input('Type in the number of your radius without the label (numbers after a decimal are fine): ')
        circumference = (2 * float(radius) * pi) 
        print(f"\n{Fore.GREEN}The circumference for radius {float(radius)} is: {circumference:.2f}.{Style.RESET_ALL}")
    else:
        diameter = input('Type in the number of your diameter without the label (numbers after a decimal are fine): ')
        circumference = (float(diameter) * pi) 
        print(f"\n{Fore.GREEN}The circumference for diameter {float(diameter)} is: {circumference:.2f}.{Style.RESET_ALL}")

    print("\nDon't forget to add your label (feet, inches, etc.) at the end!")

    print("\n*********** Thanks for visiting the Circle Circumference Calculator! ***********")
    print("Good-bye!")

circumference()