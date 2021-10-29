# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 17:20:43 2021

@author: Super
"""

## The purpose of the program is to act as a calculator/answer checker from a program from the 70's called data man.
## This is only the first version of many features in which will be introduced in the next coming sprint. For the time
## being the calculator function is accessed through a menu system to allow the user to input numbers and the desired
##opperator. The menu is broken up into addition, subtraction, mulplication, and division for the sake of testing
##a menu function for later use that will require one.
## This will be its own file rather than one large program
## Attempting to break code for different files for different purposes



def calculator():
   keep_going = True
   while keep_going == True:
       equateable = input("Enter an equation or exit: ")
       valdation_print = core_calc(equateable)
       if len (valdation_print) > 0:
           x,y,z = valdation_print[0],valdation_print[1], valdation_print[2]
           operation_sign = valdation_print[3]
           print(x, operation_sign, y, "=", z)
       else:
            break

def core_calc(equateable):
    """This function will be used to valdiate the calcualtor's information
    given the user input from the calcuatlor() function above. 
    The operator that the user inputs will select from the nested if 
    statements to determine how to calculate."""

    split_equateable, return_V = [],[]

    #Addition calculations
    if "+" in equateable:
        split_equateable = equateable.split("+")
        x = int(split_equateable[0])
        y = int(split_equateable[1])
        z = x + y
        return_V.extend((x,y,z))
        return_V.append("+")
        return return_V

    #Subtraction calculations
    elif "=" in equateable:
        split_equateable = equateable.split("-")
        x = int(split_equateable[0])
        y = int(split_equateable[1])
        z = x - y
        return_V.extend((x,y,z))
        return_V.append("-")
        return return_V

    #Multiplication calculations
    elif "*" in equateable:
        split_equateable = equateable.split("*")
        x = int(split_equateable[0])
        y = int(split_equateable[1])
        z = x * y
        return_V.extend((x,y,z))
        return_V.append("*")
        return return_V

    #Division calculations
    elif "/" in equateable:
        split_equateable = equateable.split("/")
        x = int(split_equateable[0])
        y = int(split_equateable[1])
        try:
            z = x / y
            return_V.extend((x,y,z))
            return_V.append("+")
            return return_V
        except ZeroDivisionError:
            print("Undefined")
        return

    elif equateable == "exit" or "quit":
        return_V
    
    else:
        print("That is not a valid equation please try again")
           



