import random

def create_board(rows, cols):
    """Create an empty game board."""
    return [['O' for _ in range(cols)] for _ in range(rows)]

def display_board(board):
    """Display the current game board."""
    print(21*"=")
    indexprintline = " "
    for i in range(len(board[0])):
        indexprintline += " " + str(i)
    print(indexprintline)
    rownum = 0
    for row in board:
        print(str(rownum) + " " + ' '.join(row))
        rownum += 1

def place_ship(board, length, index):
    """Randomly place a ship on the board."""
    invalid_ship = True
    while invalid_ship:
        orientation = random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board[0]) - length)
            invalid_ship = False
            for i in range(length):
                if board[row][col + i] != 'O':
                    invalid_ship = True
            if not invalid_ship:
                for i in range(length):
                    board[row][col + i] = str(index)
        else:
            row = random.randint(0, len(board) - length)
            col = random.randint(0, len(board[0]) - 1)
            invalid_ship = False
            for i in range(length):
                if board[row+i][col] != 'O':
                    invalid_ship = True
            if not invalid_ship:
                for i in range(length):
                    board[row+i][col] = str(index)

def get_player_guess(message,guesses_board):
    """Get the player's guess for row and column."""
    while True:
        display_board(guesses_board)
        try:
            rowcol = input(message + (10 - len(message))*" "+ " : ")
            return int(rowcol[1]), int(rowcol[0])
        except:
            message = "Invalid."

def battleship():
    invalidmode = True
    while invalidmode:
        print("\n\n\n\n\n\nWelcome to Battleship\n[1] Small\n[2] Medium\n[3] Large\n[4] 1v1")
        mode = input(" : ")
        if mode in ["1","2","3"]:
            if mode == "1":
                rows, cols = 5, 5
                ship_lengths = [4, 3, 2, 2]
            elif mode == "2":
                rows, cols = 5, 8
                ship_lengths = [4, 4, 3, 3, 2]
            elif mode == "3":
                rows, cols = 5, 10
                ship_lengths = [5, 4, 4, 3, 3, 2]
            elif mode == "4":
                rows, cols = 5, 10
                ship_lengths = [5, 4, 4, 3, 3, 2]
                versus_mode = True
            invalidmode = False
    board = create_board(rows, cols)
    guesses_board = create_board(rows, cols)
    board_message = ""
    # Place ships on the board
    idex = 0
    for length in ship_lengths:
        place_ship(board, length, idex)
        idex += 1
    #display_board(board)

    attempts = 0
    ships_remaining = []
    for shipnum in range(len(ship_lengths)):
        for i in range(ship_lengths[shipnum]):
            ships_remaining.append(str(shipnum))

    while len(ships_remaining) > 0:
        guess_row, guess_col = get_player_guess(board_message,guesses_board)
        board_message = ""

        if 0 <= guess_row < rows and 0 <= guess_col < cols:
            if guesses_board[guess_row][guess_col] == 'X' or guesses_board[guess_row][guess_col] == 'M':
                board_message = ""
                attempts -= 1
            elif board[guess_row][guess_col] != 'O':
                ships_remaining.remove(board[guess_row][guess_col])
                if not board[guess_row][guess_col] in ships_remaining:
                    board_message = "Ship sunk!"
                else:
                    board_message = "Hit!"
                guesses_board[guess_row][guess_col] = 'X'
            else:
                board_message = "Miss!"
                guesses_board[guess_row][guess_col] = 'M'
        else:
            board_message = "Invalid."
            attempts -= 1

        attempts += 1

    display_board(guesses_board)
    x=input("Finished in " + str(attempts) + "!")

# Run the game
while True:
    battleship()