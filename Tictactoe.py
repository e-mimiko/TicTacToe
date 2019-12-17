#x and o

import random
mat=[]
boardSize=["3","4","5"]


def play():
    playOrNot=input("This is a game of Xs and Os, would you like to play? Yes/No --> ")
    while playOrNot != "Yes" and playOrNot != "No":
        print("\nThis is not a valid input. NOTE: Letters are case sensitive")
        playOrNot=input("This is a game of Xs and Os, would you like to play? Yes/No --> ")
    if playOrNot == "No":
        print ("\nYou chose No. Bye!")
    else:  
        playerChoice=input("\nGreat! Which letter would you like?\n\n\tX or O \n--> ")
        while playerChoice != "X" and playerChoice != "O":
            print("This is not a valid input. NOTE: Letters are case sensitive. Try again")
            playerChoice=input("Which letter would you like?\n\n\tX or O \n--> ")
        boardChoice=input("\nGreat! What size of board do you want? 3 to 5 inclusive.\n--> ")
        while boardChoice not in boardSize:
            print("This is not a valid input. NOTE: Enter a valid number.")
            boardChoice=input("\nWhat size of board do you want? 3 to 5 inclusive.\n--> ")
        return playerChoice, boardChoice
        

        

def Game():
    playerChoice,boardChoice=play()
    print (playerChoice)
    print (boardChoice)

Game()
'''
for r in range (3):
    roll=[]
    for c in range(3):
        roll.append("?")
    mat.append(roll)
#print (mat)


for i in range(3):
    for h in range (3):
        print ("\t",mat[i][r],"\t",end="")
    print()
'''
        

    
