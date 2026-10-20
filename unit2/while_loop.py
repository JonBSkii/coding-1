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

