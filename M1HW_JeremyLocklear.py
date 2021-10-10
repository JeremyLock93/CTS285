# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 17:20:43 2021

@author: Super
"""

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

def addition():
    print("To add use + after entering first number")
    
    num = int(input(" "))
    plusSign = input(" ")
    num1 = int(input(" "))
    
   
    
    return num, num1
   
    



def validationAddition(num, num1):
    addition = num + num1
    print("_" * 10)
    print(addition)
    
def subtraction():
    num = int(input(" "))
    subtactionSign = (" ")
    num1 = int(input(" "))
    
    return num, num1




def validationSubtraction(num, num1):
     subtraction = num - num1
     print("_" * 10)
     print(subtraction)
      

def multiplication():
    num = int(input(" "))
    multiply = input(" ")
    num1 = int(input(" "))
    
    return num, num1
    
    


def validationMultiplication(num, num1):
       multiplication = num * num1
       print("_" * 10)
       print(multiplication)

def division():
    num = int(input(" "))
    divisionSign = input(" ")
    num1 = int(input(" "))
    if num1 == 0:
        print("Error Division by Zero")
    else:
        return num, num1


def validationDivision(num, num1):
    division = num / num1
    print("_" * 10)
    print(division)


if __name__ == "__main__":
    main() 