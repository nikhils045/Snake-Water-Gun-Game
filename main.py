import random

choices = ["Snake", "Water", "Gun"]

userWins = 0
computerWins = 0

def playGame():
    global userWins, computerWins

    while True:
        userChoice = input("Enter Your choice: Snake, Water, Gun (or 'q' to quit): ").capitalize().strip()
        if userChoice == 'Q':
            print("Thanks for playing!")
            print(f"Final Score: You - {userWins}, Computer - {computerWins}\n")
            return
        if userChoice not in choices:
            print("Invalid choice. Please try again.\n")
            continue

        computerChoice = random.choice(choices)
        print(f"Computer chose: {computerChoice}")
        
        if userChoice == computerChoice:
            print("It's a tie!")
        elif (userChoice == "Snake" and computerChoice == "Water") or \
             (userChoice == "Water" and computerChoice == "Gun") or \
             (userChoice == "Gun" and computerChoice == "Snake"):
            print("You Win!")
            userWins += 1
        else:
            print("You Lose!")
            computerWins += 1
        print(f"Score: You - {userWins}, Computer - {computerWins}\n")

playGame()