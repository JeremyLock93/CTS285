# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:42:44 2021

@author: Super
"""
# =============================================================================
# CTS 285
# M1HW Calculator V.1
# Jeremy Locklear
# 08/27/21
# =============================================================================
# =============================================================================
# # The purpose of this program is a simple menu driven caluculator, when prompted
# # the user will calculate numbers in which they input and will be given an output
# # from the choice that they made on the main menu. They then can repeat or leave.
# 
# =============================================================================

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
            addition()
        elif choice == 2:
            subtraction()
        elif choice == 5:
            keep_going = 'n'
            print("Exit")
            
        else:
            print("Invalid Choice. Enter a Valid option.")
            input("Press any key to continue.")

def addition():
    num = int(input("Enter a number: "))
    num1 = int(input("Enter another number: "))
    addition = num + num1
    print(num, '+', num1, '=', addition)
    validationAddition()
    


def validationAddition():
    keep_on = 0
    while (keep_on == 0):
        print("1) Repeat")
        print("2) Main Menu")
        user_input = int(input("Make your choice: "))
        if user_input == 1:
            keep_on == 0
            addition()
        elif user_input == 2:
            keep_on += 1
            main()
        else:
            keep_on += 1
            
def subtraction():
    num = int(input("Enter a number: "))
    num1 = int(input("Enter another number: "))
    subtraction = num - num1
    print(num, '-', num1, '=', subtraction)
    validationSubtraction()
    


def validationSubtraction():
       keep_on = 0
       while (keep_on == 0):
        print("1) Repeat")
        print("2) Main Menu")
        user_input = int(input("Make your choice: "))
        if user_input == 1:
            keep_on == 0
            subtraction()
        elif user_input == 2:
            keep_on += 1
            main()
        else:
            keep_on += 1
            
def multiplication():
    num = int(input("Enter a number: "))
    num1 = int(input("Enter another number: "))
    multiplication = num * num1
    print(num, '*', num1, '=', multiplication)
    validationMultiplication()
    

    
def validationMultiplication():
        keep_on = 0
        while (keep_on == 0):
            print("1) Repeat")
            print("2) Main Menu")
            user_input = int(input("Make your choice: "))
            if user_input == 1:
                keep_on == 0
                multiplication()
            elif user_input == 2:
                keep_on += 1
                main()
            else:
                keep_on += 1
                
def division():
    num = int(input("Enter a number: "))
    num1 = int(input("Enter another number: "))
    multiplication = num * num1
    print(num, '*', num1, '=', multiplication)
    if num1 == 0:
        print("Error Division by Zero")
    else:
        validationMultiplication()

    
def validationDivision():
    keep_on = 0
    while (keep_on == 0):
        print("1) Repeat")
        print("2) Main Menu")
        user_input = int(input("Make your choice: "))
        if user_input == 1:
            keep_on == 0
            division()
        elif user_input == 2:
            keep_on += 1
            main()
        else:
            keep_on += 1         
            
    
if __name__ == "__main__":
    main()