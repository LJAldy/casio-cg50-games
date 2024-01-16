def cls():
    print("\n\n\n\n\n\n\n\n")
def printgameboard(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
def winner(winpiece):
    if not winpiece == " ":
        print("Player " + winpiece + " has won!")
        return True
    return False
def findwin(board):
    if board[0] == board[1] and board[1] == board[2]:
        return winner(board[0])
    elif board[3] == board[4] and board[4] == board[5]:
        return winner(board[3])
    elif board[6] == board[7] and board[7] == board[8]:
        return winner(board[6])
    elif board[0] == board[3] and board[3] == board[6]:
        return winner(board[0])
    elif board[1] == board[4] and board[4] == board[7]:
        return winner(board[1])
    elif board[2] == board[5] and board[5] == board[8]:
        return winner(board[2])
    elif board[0] == board[4] and board[4] == board[8]:
        return winner(board[0])
    elif board[2] == board[4] and board[4] == board[6]:
        return winner(board[2])
    else:
        return False
while True:
    cls()
    gameboard = []
    for i in range(9):
        gameboard.append("i")
    printgameboard(gameboard)
    input()
    for i in range(9):
        gameboard[i] = " "
    win = False
    for i in range(9):
        if i % 2 == 0:
            token = "O"
        else:
            token = "X"
        invalid = True
        while invalid:  
            printgameboard(gameboard)
            placement = input(token + ": Enter index: ")
            cls()
            if any(placement == str(x) for x in range(1,10)):
                placement = int(placement)
                if placement >= 1 and placement <= 9:
                    if gameboard[placement-1] == " ":
                        gameboard[placement-1] = token
                        invalid = False
                    else:
                        print("Already piece there.")
                else:
                    print("Number between 1-9.")
            else:
                print("Not a number.")
        if findwin(gameboard):
            break
    printgameboard(gameboard)
    input()
