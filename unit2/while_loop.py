# Loop - a loop is a construct (speciaal function) that repeats itself. 
# In programming, a loop allows to repeat code instructions.

# There are two types of loops: For loop and While loop

# While loop- a type of loop where so long as a condition is equal to true it will keep running "forever"

# the key word is while --> do while

# syntax
num = 4 
while 2+2 == num: # conditon --> operations - muat be TRUE 
    print ("the program is running...")
    num = int (input("please type in a number:")) 

    # while loops will ALWAYS run unless you change the conditiona!
    # we can do this by writing instructions to manually change it.

    def guessingGame():
        CorrectAnswer == 12
        attempts = 0
       
print ("Guessing game has started")
userguess = input ("please guess a number between 1 and 50.")

while userGuess == correctAnswer:
    print("Incorrect. Please try again...")
    attempts +=1 
    print("Guess attempts: " + str(attempts))
    userguess = input ("please guess a number between 1 and 50.")

print("Congrats! you guessed the right number!")

# Question 1
# password reset function. Your function should take in a user password as an input.
# within the function there should be a variable that contains the correct password.
# the user should be able to attempt to enter the password 4 times. On the fourth attempt
# of getting the password inccorect, it should print out a message telling the user that their account 
# has been locked. If the user gets the password correct it should print out a message telling them
# they can access their account.

# Question 2
# Create a shots made-to-attempts function. your function should prompt the user to enter if they
# made or missed a shot. If they enter made, it will give the user 2 points. else if they miss it 
# will not give them points. Every shot must be recorded. If your user enters the letter "q", it 
# will show how many points they made as well as the number of attempts they've made

def password_reset():
    correct_password = "Python123"
    attempts = 0

    while attempts < 4:
        password = input("Enter your password: ")

        if password == correct_password:
            print("Correct password! You can access your account.")
            return
        else:
            attempts += 1
            print("Incorrect password. Try again.")

    print("Your account has been locked.")

password_reset()