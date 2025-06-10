print("************* Rock Paper Scissors Game *************")

userScore = 0
computerScore = 0
while True:
    c = ["Rock","Paper","Scissors"]
    userChoice = input("Enter your Choice:").capitalize()

    import random
    computerChoice = random.choice(c)

    print("UserChoice===",userChoice)
    print("ComputerChoice===",computerChoice)

    if userChoice=='Rock':
        if computerChoice=='Rock':
            print("It's tie")
        elif computerChoice =='Paper':
            print("Computer Won")
            computerScore+=1
        else:
            print("You Won")
            userScore+=1

    elif userChoice=='Paper':
        if computerChoice=='Rock':
            print("You won")
            userScore+=1
        elif computerChoice=='Paper':
            print("It's a tie")
        else:
            print("computer Won")
            computerScore+=1

    elif userChoice=='Scissors':
        if computerChoice=="Rock":
            print("Computer Won")
            computerScore+=1

        elif computerChoice=="Paper":
            print("You won")
            userScore+=1
        else:
            print("it's a tie")
    else:
        print("Invalid choice")

    print("User Score ===", userScore)
    print("Computer Score===",computerScore)
    print()
    a = input("Do you want to Continue(y/n):").lower()
    if a=="n":
        print("Thank you..")
        break











