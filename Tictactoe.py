#x and o

import random

def play():
    playOrNot=input("This is a game of Xs and Os, would you like to play? Yes/No --> ")
    if playOrNot=="Yes":
        playerChoice=input("Great! Which letter would you like?\nX or O --> ")
        while playerChoice != "X" or "O":
            print("This is not a valid input. NOTE: letters are case sensitive")
            playerChoice=input("Great! Which letter would you like?\nX or O --> ")
        return playerChoice
    elif playOrNot=="No":
        print("Thats Ok! Come back again another time. Bye!")
    else:
        print("This is not a valid Input. NOTE: letters are case sensitive")
        playerChoice=input("Great! Which letter would you like?\nX or O --> ")
        return playerChoice


def play():
    playOrNot=input("This is a game of Xs and Os, would you like to play? Yes/No --> ")
    while playOrNot != "Yes" or "No":
        print("This is not a valid input. NOTE: Letters are case sensitive")
        playOrNot=input("This is a game of Xs and Os, would you like to play? Yes/No --> ")
    playerChoice=input("Great! Which letter would you like?\nX or O --> ")
    while playerChoice != "X" or "O":
        print("This is not a valid input. NOTE: Letters are case sensitive. Try again")
        playerChoice=input("Which letter would you like?\nX\nO\n--> ")
    return playerChoice
        

        


            

        

    
