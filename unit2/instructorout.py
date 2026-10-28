# Rock, Paper, Scissors is a game played between two players. In this game, each player chooses one of three options: rock, paper,
#  or scissors. The goal is to choose an option that beats the other player's choice.
# The game uses a set of rules to determine who wins, loses, or ties.

def rockPaperScissors():
    rounds = 0
    playerScore = 0
    cpuScore = 0

    while rounds < 3:
        player = input("Enter r for rock, p for paper, s for scissors, or q to quit: ").lower()

        if player == "q":
            print("You quit the game!")
            break

        if player != "r" and player != "p" and player != "s":
            print("Invalid choice. Please try again.")
            continue

        cpuNumber = random.randint(1, 3)

        if cpuNumber == 1:
            cpu = "r"
        elif cpuNumber == 2:
            cpu = "p"
        else:
            cpu = "s"

        print("You chose:", player)
        print("CPU chose:", cpu)

        if player == cpu:
            print("It's a tie!")
        elif (player == "r" and cpu == "s") or \
             (player == "p" and cpu == "r") or \
             (player == "s" and cpu == "p"):
            print("You win this round!")
            playerScore += 1
        else:
            print("CPU wins this round!")
            cpuScore += 1

        rounds += 1
        print("Your score:", playerScore)
        print("CPU score:", cpuScore)

    print("Game over!")
    print("Final player score:", playerScore)
    print("Final CPU score:", cpuScore)

rockPaperScissors()

# Thursday "Instructor"

def vendingMachine():
    choice = ""

    print("Vending Machine has started!")

    while choice != "q":
        choice = input(
            "Enter a vending machine number (B3, G4, G7, D3, G5) or q to quit: "
        ).upper()

        if choice == "B3":
            print("You selected Nacho Chips!")

        elif choice == "G4":
            print("You selected BBQ Chips!")

        elif choice == "G7":
            print("You selected Plain Chips!")

        elif choice == "D3":
            print("You selected Water!")

        elif choice == "G5":
            print("You selected Cola Soda!")

        elif choice == "Q":
            print("Vending machine has stopped!")

        else:
            print("Invalid selection. Please try again.")

    print("Thank you for using the vending machine!")

# Friday "Instructor"

def diceRollingGame():
    score = 0
    choice = ""

    print("Dice Rolling Game has started!")

    while choice != "q":
        choice = input("Enter r to roll the dice or q to quit: ").lower()

        if choice == "r":
            dice = random.randint(1, 7)
            print("You rolled:", dice)

            if dice == 7:
                print("Congratulations! You won 10 points!")
                score += 10
            else:
                print("Sorry! You lost 5 points.")
                score -= 5

            print("Your score:", score)

        elif choice == "q":
            print("You quit the game!")

        else:
            print("Invalid choice. Please enter r or q.")

    print("Game over!")
    print("Your final score:", score)


diceRollingGame()

