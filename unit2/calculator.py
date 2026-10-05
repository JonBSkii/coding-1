# step 1: create a function that will addd 2 numbers together
# step 2: the numbers should be typed in by a user

# phase 1 of function: function def- actual code-does nothing 
def calculate_add():
    print ("program has started: type in 2 to add:")
    num1= input()
    num2= input()
    print(num1 + num2)
    print("program has ended.")

    phase 2 of function: function call- actually runs and does something
    calculate_add()

    #make a function for subtraction, multiplication, and division

    # Subtraction
def calculate_subtract():
    print("Program has started: type in 2 numbers to subtract:")
    num1 = int(input())
    num2 = int(input())
    print(num1 - num2)
    print("Program has ended.")


# Multiplication
def calculate_multiply():
    print("Program has started: type in 2 numbers to multiply:")
    num1 = int(input())
    num2 = int(input())
    print(num1 * num2)
    print("Program has ended.")


# Division
def calculate_divide():
    print("Program has started: type in 2 numbers to divide:")
    num1 = int(input())
    num2 = int(input())
    print(num1 / num2)
    print("Program has ended.")


# Function calls
calculate_add()
calculate_subtract()
calculate_multiply()
calculate_divide()