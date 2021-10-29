 def main():
 keep_going = 'y'
    while (keep_going.lower()=='y'):
        print()
        print("Main Menu")
        print()
        print('-' *20)
        print("1) Addition")
        print("2) Subractions")
        print("3) Multiplication")
        print("4) Division")
        print("5) Exit")
        choice = int(input('Enter your choice: '))
        #Getting choices
        if choice == 1:
            num, num1 = addition() 
            validationAddition(num, num1)
        elif choice == 2:
            num, num1 = subtraction()
            validationSubtraction(num, num1)
        elif choice == 3:
            num, num1 = multiplication()
            validationMultiplication(num, num1)
        elif choice == 4:
            num, num1 = division()
            validationDivision(num, num1)
        elif choice == 5:
            keep_going = 'n'
            print("Exit")

        else:
            print("Invalid Choice. Enter a Valid option.")
            input("Press any key to continue.")