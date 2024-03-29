BOARDINDEX = [6,7,8,3,4,5,0,1,2]
def printgameboard(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
def winner(win_piece):
    if not win_piece == " ":
        print("Player " + win_piece + " has won!")
        return True
    return False
def findwin(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and not board[condition[0]] == " ":
            return winner(board[condition[0]])
    return False
while True:
    print(7*"\n")
    gameboard = []
    for i in range(9):
        gameboard.append(str(BOARDINDEX[i]+1))
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
            print(7*"\n")
            if any(placement == str(x) for x in range(1,10)):
                placement = BOARDINDEX[int(placement)-1]
                if gameboard[placement] == " ":
                    gameboard[placement] = token
                    invalid = False
                else:
                    print("Already piece there.")
            else:
                print("Invalid index.")
        if findwin(gameboard):
            break
    printgameboard(gameboard)
    input()