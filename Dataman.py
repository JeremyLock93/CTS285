import random


## The purpose of the program is to act as a calculator/answer checker from a program from the 70's called data man.
## This is only the first version of many features in which will be introduced in the next coming sprint. For the time
## being the calculator function is accessed through a menu system to allow the user to input numbers and the desired
##opperator. The Number Guesser is part of this larger program as trying to get things to work in seperate files
## Did not work well together so putting everything together into one main file

def main():
    keep_going = 'y'
    while (keep_going.lower()=='y'):
        print()
        print("DataMan Main Menu")
        print()
        print('-' *20)
        print("1) Basic Calculator")
        print("2) Answer Checker")
        print("3) Memory Bank")
        print("4) Number Guesser")
        print("5) Exit")
        choice = int(input('Enter your choice: '))
        #Getting choices
        if choice == 1:
            calculator()    
        elif choice == 2:
            answerChecker()
        elif choice == 3:
            memoryBankStorage()
        elif choice == 4:
            numberGuesser()
        elif choice == 5:
            print("Exited, Program Terminated")
            keep_going = 'n'
        else:
            print("Invalid Choice. Enter a Valid option.")
            input("Press any key to continue.")


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


def answerChecker():
    """This function acts as the initalizer for the answer checker. By asking the user
    how many questions in which they wish to answer. This function will iterate through
    a loop for x number of questions and will send them to the storage in memory function
    called answerBank"""
    print("The Answer Checker")
    equations_list, answers_list = [],[]
    
    m = int(input("How many questions would you like to Answer?"))

    for _ in range(m):
        x = input("Enter equation(s) here > ")
        equations_list.append(x)
        answer = core_calc(x)
        answers_list.append(answer[2])

        answerBank(equations_list, answers_list, m)

def answerBank(equations_list, answers_list, m):
    """This function is the storage bank iterations for the answer checker. It will
    give the user how many correct and incorrect using the information provided from the 
    answerChecker() and displays that information to the user in the form of x correct,
    y incorrect"""
    equations_list = equations_list
    answers_list = answers_list
    index, count, correct, incorrect = 0, 0, 0, 0
    
    
    while len(answers_list) > 0:
        while len(answers_list) > 0:
            print(equations_list[index],"=?")
            a = int(input("Answer: "))

            if a == answers_list[0]:
                print("Correct")
                correct += 1
                index += 1
                del answers_list[0]
                break
            elif count == 2:
                print("The correct answer was:", answers_list,"\n")
                incorrect += 1
                count = 0
                index += 1
                del answers_list[0]
            elif a != answers_list[0]:
                print("Sorry that is incorrect")
                count += 1

    print("\nYou gotten", correct, "correct and", incorrect, "incorrect out of", a)
    return


def memoryBankStorage():
    """This is the function that allows for the later storage of questions. Division is 
    a lot more diffcult to implement currently and will be added in a later update of 
    program, but will be able to store addition, subtraction, and multipliaction. For
    they don't require too much work to get working correctly.
    
    How it works is will be taking user input and setting them into a memoryBankCore
    Which will read the functions from the storage. Using the most commonly taught ints
    1-12 and eventually in future updates go further beyond that."""

    print("Welcome to the Memory Bank")
    int_ranges = ['0','1','2', '3', '4', '5', '6', '7', '8','9','10','11','12']
    equations_list, answers_list, x,y,z = [],[],[],[],[]
    m = int(input("How many questions would you like to store?"))

    for count in range(m):
        #first variables in the question
        r = random.randint(0,12)
        d = int_ranges[r]
        x.append(d)

        #Operations
        operator = ['+', '-', '*']
        r = random.randint(0,2)
        d = operator[r]
        z.append(d)

        #Second Variable
        r = random.randint(0,12)
        d = int_ranges[r]
        y.append(d)

        #Final set up for the way the equations will be listed and checked against
        r = ''.join([x[count],z[count],y[count]])
        answer = core_calc(r)
        answers_list.append(answer[2])
        equations_list.append(r)

    answerBank(equations_list,answers_list,m)

        
def numberGuesser():
    """This function is a simple number guesser from 1-100 and will say if the number is too
    high or low, and give the amount of guesses it took to get to correct number"""
    print("Number Guesser")
    
    while True:

        guess = int(input("Enter a number between 1 and 100: "))
        num = random.randint(1,100)
        count = 1

        while num != guess:

            if num > guess:
                print ("Too low Try Again")
                guess = int(input("Enter a number between 1 and 100: "))
                count += 1

            elif num < guess:
                print ("Too high Try again")
                guess = int(input("Enter a number between 1 and 100: "))
                count += 1

            else:
                print("Congratulations!")
                False

        print("It took this many guesses", count)


if __name__ == "__main__":
    main()