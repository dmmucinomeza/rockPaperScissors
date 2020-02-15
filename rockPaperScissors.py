keepPlaying = True

while (keepPlaying == True):
    print("Welcome to Rock-Paper-Scissors, kids!")
    print("Rules: the winner will be best of 2 out of three games")
    print("press 'q' if you would like to quit")

    #rock = 1
    #paper = 2
    #scissors= 3
   
    import random
    computerScore = 0
    playerScore = 0

    while (playerScore < 2) and (computerScore < 2):
   
        computerChoice = random.randint(1,3)
        playerChoice = input("you choose: ")
        #start checking user option
       
        if (playerChoice == "q"):
            keepPlaying = False
            break
       
        elif ((playerChoice == "rock" )and(computerChoice == 1)) or ((playerChoice == "paper") and (computerChoice == 2)) or ((playerChoice == "scissors") and (computerChoice == 3)):
            print("DRAW :(!")
            print("Computer's score is: ", + computerScore)
            print("Player's score is: ", + playerScore)
       
        elif ((playerChoice == "rock") and (computerChoice == 2)) or ((playerChoice == "scissors") and (computerChoice == 1)) or ((playerChoice == "paper") and (computerChoice == 3)):
            computerScore =+1
            print("Computer's score is: ", + computerScore)
            print("Player's score is: ", + playerScore)
       
       
        elif ((playerChoice == "paper") and (computerChoice == 1)) or ((playerChoice == "scissors") and (computerChoice == 2)) or ((playerChoice == "rock") and (computerChoice == 3)):
            playerScore =+1
            print("Computer's score is: ", + computerScore)
            print("Player's score is: ", + playerScore)
       
        else:
            print("Sorry, the input you have chosen is not valid, please try again")
           
    print("Thank You for playing Rock-Paper-Scissors! We hope to see you again")
     
    if (playerScore == 2):
        print("Congratulations, you won!")
     
    if (computerScore == 2):
        print("The computer won :( LOSER!!")
     
    print (playerScore and computerScore)            

    

        
    