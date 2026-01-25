import random

choices = ["Rock", "Paper", "Scissors"]

playerChoise = input("Choose a number between the following list: 1-Rock, 2-Paper, 3-Scissors: ")

playerChoise = int(playerChoise)
#input check
if playerChoise < 1 or playerChoise > 3:
    print ("error: You should choose a number between 1 and 3!")
else:
    #develope the game logic through if/elif/else
    computerChoice = random.randint (1, 3)
    print (playerChoise, computerChoice)

    if playerChoise == computerChoice:
        print("it's a tie!")
    elif playerChoise == 1 and computerChoice == 3:
        print("Rock beats scissors - you win!")
    elif playerChoise == 2 and computerChoice ==1:
        print("paper beats rock- you win")
    elif playerChoise == 3 and computerChoice == 3: 
        print("scissors beats paper- you win")
    else:
        print("you lose!")

