import math
from colorama import Fore, Style

def square_footage():
        print("\n***************** Welcome to the Square Footage Calculator! *****************")
        # def square_footage:
        #     while True:
        #         if input == float(input) or input == int(input):
        length = input('\nType in the number of the length without the label (numbers after a decimal are fine): ')
        # length = float(input())
        # if input == str(input):
        #     print("That did not compute. Please try again.")
        # else:
        width = input('Type in the number of the width without the label (numbers after a decimal are fine): ')
        # width = float(input())
        # if input == str(input):
        #     print("That did not compute. Please try again.")
                # continue

        area = float(length) * float(width)

        print("*************************************************************************************")
        print(f"\n{Fore.GREEN}The area for length {float(length)} and width {float(width)} is: {area:.2f}.{Style.RESET_ALL}")
        print("\nDon't forget to add your label (feet, inches, etc.) at the end with the superscript 2 for 'squared'!")

        print("\n*********** Thanks for visiting the Square Footage Calculator! ***********")
        print("Good-bye!")

square_footage()
