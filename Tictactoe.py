#x and o

from random import randint
mat=[]
boardSize=["3","4","5"]
Ex = "X"
Oh = "O"
winners_score = 0

def game_open():
    playOrNot=input("This is a game of Xs and Os, would you like to play? Yes/No --> ")
    while playOrNot != "Yes" and playOrNot != "No":
        print("\nThis is not a valid input. NOTE: Letters are case sensitive")
        playOrNot =input("This is a game of Xs and Os, would you like to play? Yes/No --> ")
    if playOrNot == "No":
        print ("\nYou chose No. Bye!")
    else:  
        playerChoice=input("\nGreat! Which letter would you like?\n\nX or O \n--> ")
        while playerChoice != Ex and playerChoice != Oh:
            print("This is not a valid input. NOTE: Letters are case sensitive. Try again")
            playerChoice=input("Which letter would you like?\n\nX or O \n--> ")
        if playerChoice == Ex:
            computerChoice = Oh
        else:
            computerChoice = Ex
        boardChoice=input("\nGreat! What size of board do you want? 3 to 5 inclusive.\n--> ")
        while boardChoice not in boardSize:
            print("This is not a valid input. NOTE: Enter a valid number.")
            boardChoice=input("\nWhat size of board do you want? 3 to 5 inclusive.\n--> ")
        return playerChoice, computerChoice, boardChoice
        
        

def make_board():
    playerChoice, computerChoice, boardChoice = game_open()
    boardChoice=int(boardChoice)

    for r in range (boardChoice):
        roll=[]
        for c in range(boardChoice):
            roll.append("?")
        mat.append(roll)
    return playerChoice, computerChoice, boardChoice

def print_board():
    print()
    for r in mat:
        for c in r:
            print("\t", c, end="")
        print()

def check_score(play,winners_score):
    if play >= boardChoice:
        for r in range(boardChoice): #for rows
            roll = []
            for c in range(boardChoice):
                roll.append(mat[r][c])
            if len(set(roll)) == 1 and ("?") not in set(roll):
                winners_score = 1
                winner = str(set(roll))
                print (winner, "a")
                return winner, winners_score
            
      
        if winners_score == 0:
            for r in range(boardChoice): #for columns
                roll = []
                for c in range(boardChoice):
                    roll.append(mat[c][r])
                if len(set(roll)) == 1 and ("?") not in set(roll):
                    winners_score = 1
                    winner = str(set(roll))
                    print (winner, "b")
                    return winner, winners_score

        if winners_score == 0: 
            roll = []
            for r in range(boardChoice): # for similar increments
                c = r
                roll.append(mat[r][c])
            if len(set(roll)) == 1 and ("?") not in set(roll):
                winners_score = 1
                winner = str(set(roll))
                print (winner, "c")
                return winner, winners_score
##work on this part
        if winners_score == 0:
            roll = []
            for r in range(boardChoice):
                for c in reversed(boardChoice):
                    pass
                roll.append(mat[r][c])
            if len(set(roll)) == 1 and ("?") not in set(roll):
                winners_score = 1
                winner = str(set(roll))
                print (winner, "d")
                return winner, winners_score
                

        if any("?" in i for i in mat) == False:
            winner = ("Nobody")
            winners_score = 2
            return winner, winners_score
                
            
                

##Game Body
playerChoice, computerChoice, boardChoice = make_board()
play = 0
while winners_score == 0 and any("?" in i for i in mat) == True:
    try:
            row,column = input("Enter the ROW, then a SPACE, then COLUMN you'd like to play e.g. 2 1 : ").split()
    except ValueError:
        print("\nPlease enter a SPACE between the row e.g. 2 3")
        continue
    if int(row) > len(mat)-1 or int(column) > len(mat)-1:
        print("\nEnter a valid Row and Column in the range of the Board")
        continue
    else:
        row = int (row)
        column = int(column)
        if mat[row][column] != "?":
            print("\nThis position has already been played.")
            continue

    mat[row][column] = playerChoice
    play += 1
    print_board()

    try:
        winner, winners_score = check_score(play,winners_score)
        if winners_score == 1:
            break
        elif winners_score == 2:
            break
    except TypeError:
        pass
        
    

#computer plays here
    
    row = randint(0, len(mat) - 1)
    column = randint(0, len(mat) - 1)
    while mat[row][column] != "?":
        row = randint(0, len(mat) - 1)
        column = randint(0, len(mat) - 1)
        continue
    mat[row][column] = computerChoice
    print("Computer Plays...", row, column)
    print_board()

    try:
        winner, winners_score = check_score(play,winners_score)
        if winners_score == 1:
            break
        elif winners_score == 2:
            break
    except TypeError:
        pass


if winners_score == 1:
    print(winner, "player wins!")
else:
    print("No One Wins!")








