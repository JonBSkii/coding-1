# conditional if/else logic- these are keywords that instruct your program to do specific instructions based on specific data or 
conditions.

# conditional syntax (how is it written)
bill_amount + int(input("Please type in a bill tender (1s, 5s, or 10s): "

# if usually indicates that something is a possible option if bill_amount == 1:
print("here are 4 quarters")

# elif allows us to indicate that there are more possible options you can have as many elif as you want
elif bill_amount == 5:
 print ("here are 20 quarters")
 elif bill_amount == 10:
  print "here are 40 quarters")
  elif bill_amount == 50
  print ("sorry we do not accept 50s. please enter an accepted amount")
  elif bill_amount == 100
    print ("sorry we do not accept 100s. please enter an accepted amount")
    
 # else is ALWAYS your last option.
  else:
  print ("sorry that type of bill is not accepted.")

  create a calculator function that uses if/else logic to allow the user to change or select different arithmetic operations.
  # example: an input where if the usr enter 1, it will do addition, 2 will do subtraction 3 will do multiplication and 4 division

def calculator():
    print("Select an arithmetic operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = int(input("Enter your choice (1-4): "))

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == 1:
        print("The answer is:", num1 + num2)

    elif choice == 2:
        print("The answer is:", num1 - num2)

    elif choice == 3:
        print("The answer is:", num1 * num2)

    elif choice == 4:
        if num2 != 0:
            print("The answer is:", num1 / num2)
        else:
            print("Sorry, you cannot divide by zero.")

    else:
        print("Sorry, that is not a valid option.")

calculator()
How it works
if checks whether the user selected addition (1).

elif checks the other options: subtraction (2), multiplication (3), and division (4).

else runs if the user enters an invalid choice, such as 5.

input() asks the user to enter information.

int() converts the operation choice into a whole number.

float() allows the user to enter numbers with decimals, such as 5.5.

num2 != 0 checks that the second number is not zero before dividing.

Example output
text
Select an arithmetic operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
Enter your choice (1-4): 1
Enter the first number: 10
Enter the second number: 5
The answer is: 15.0