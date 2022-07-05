import sys
import pyperclip

def multiplication():
    try:
        print("Please input the number that you want to multiply:")
        first = int(input())
        print("Please input the second number:")
        second = int(input())
        return first * second
    except ValueError:
        print("Please input a number")
        print("Error terminating the program")
        sys.exit()

def addition():
    try:
        print("Please input a number that you want to add:")
        first = int(input())
        print("Please input the second number")
        second = int(input())
        return first + second
    except ValueError:
        print("Please input a number")
        print("Error terminating the program")
        sys.exit()

def subtraction():
    try:
        print("Please input a number that you wanted to be subtracted:")
        first = int(input())
        print("Plpease input the second number that you want to be subtracted:")
        second = int(input())
        return first - second
    except ValueError:
        print("Please input a number")
        print("Error terminating the program")
        sys.exit()

def division():
    try:
        print("Please input a number that you want to be divided")
        first = int(input())
        print("Please type the second number that you want to be divided")
        second = int(input())
        return first / second
    except:
        print("Please input a valid number")
        print("Error terminating the program")
        sys.exit()
        
print("Welcome to a calculator that was made by Gab")
print("0 - Exit the app \n1 - Addition \n2 - Subtraction \n3 - Multiplication \n4 - Division")
try:
    selection = int(input())
    
    if selection == 0:
        sys.exit()   
    elif selection == 1:
        added = addition()
        print("The answer that the machine stated is " + str(added))
        print("Do you want to copy the answer to your clipboard> \nInput 1 if yes \nInput 2 if no")
        answer = input()
        answer_int = int(answer)
        if answer_int == 1:
            pyperclip.copy(str(added))
        else:
            sys.exit()
    elif selection == 2:
        subtracted = subtraction()
        print("The answer that the machine stated is " + str(subtracted))
        print("Do you want to copy the answer to your clipboard> \nInput 1 if yes \nInput 2 if no")
        answer = input()
        answer_int = int(answer)
        if answer_int == 1:
            pyperclip.copy(str(subtracted))
        else:
            sys.exit()

    elif selection == 3:
        multiplied = multiplication()
        print("The answer that the machine stated is " +str(multiplied))
        print("Do you want to copy the answer to your clipboard> \nInput 1 if yes \nInput 2 if no")
        answer = input()
        answer_int = int(answer)
        if answer_int == 1:
            pyperclip.copy(str(multiplied))
        else:
            sys.exit()

    elif selection == 4:
        divided = division()
        print("The answer that the machine states is "+str(divided))
        print("Do you want to copy the answer to your clipboard> \nInput 1 if yes \nInput 2 if no")
        answer = input()
        answer_int = int(answer)
        if answer_int == 1:
            pyperclip.copy(str(divided))
        else:
            sys.exit()

    else:
        print("Please select the number with the selection range")
except ValueError:
    print("Please input a number not a letter")


