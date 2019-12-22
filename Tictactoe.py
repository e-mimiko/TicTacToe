#x and o

import random
mat=[]
boardSize=["3","4","5"]


def game_open():
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
        
        

def make_board():
    playerChoice,boardChoice=game_open()
    boardChoice=int(boardChoice)

    for r in range (boardChoice):
        roll=[]
        for c in range(boardChoice):
            roll.append("?")
        mat.append(roll)
    print (mat)





def play():
    make_board()
    while True:
        try:
            row,column = input("Enter the ROW, then a SPACE, then COLUMN you'd like to play e.g. 2 1 : ").split()
        except ValueError:
            print("\nPlease enter a SPACE between the row e.g. 2 3")
            continue
        row = int(row)
        column = int(column)
        if row > len(mat)-1 or column > len(mat)-1:
            print("\nEnter a valid Row and Column")
            continue
        break
    



play()

#print board    
'''    
print (mat)
print(len(mat))
mat[0][1]="X"
mat[2][1]="O"
for i in mat:
    for x in i:
        print("\t", x, end="")
    print()
    
'''   


##old printboard
'''
make_board()


def print_board()
    for i in range(boardChoice):
        for h in range (boardChoice):
            print ("\t",mat[i][r],end="")
        print()

print_board()

'''





    
