#x and o

import random

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
        return playerChoice
        
play()
        

def Game():
    playerChoice=play()

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
        

    
