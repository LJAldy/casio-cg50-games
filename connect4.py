#class for the Player 1 and 2
class Player():
        win_counter = 0
        token = "E"
        
        def __init__(self, name, player_number):
            self.name = name
            self.player_number = player_number
        
        #message for start of the game
        def __repr__(self):
            return "{name} is playing as Player {number} with the \"{token}\" token.".format(name=self.name, number=self.player_number, token=self.token)
        
            
#class for the game
class Four_In_A_Row():
        #dictionary for the single fields of the game
        # fields[column] = list[rows of that column]
        fields = {}
        for i in range (7):
            fields[i] = list(range(6))

        def __repr__(self):
            return "\n\n\n\n\nWelcome to 4-In-A-Row!"

        #method to create a game field or clear the last for the next game
        def create_clear_game(self):
            for j in range(7):
                for i in range(6):
                    self.fields[j][i] = "-"
        
        def print_field(self,token_turn,move_num):
            for i in range(6):
                row = ""
                for j in range(7):
                    row += ("{field}".format(field=self.fields[j][i]))
                    row += "|"
                row = row[:-1]
                if i == 0:
                    row += "  Move:"
                elif i == 1:
                    row += "  {move}".format(move=move_num)
                elif token_turn:
                    if i == 3:
                        row += "  Turn:"
                    elif i == 4:
                        row += "  {token}".format(token=token_turn)
                print(row)
            #print("1 2 3 4 5 6 7")
        
        def edit_field(self, column_number, player_token):
            for i in range(6):
                if self.fields[column_number - 1][-i - 1] == "-":
                    self.fields[column_number - 1][-i - 1] = player_token
                    break
            #self.print_field()
        
        #method for the gameplay
        def gameplay(self):
            #game preparation
            self.create_clear_game()
            #start of the game and player inputs
            move = 0
            random_number = 1
            while move < 42:
                move += 1
                if move % 2 == 1:
                    current_player_token = player1.token
                else:
                    current_player_token = player2.token
                self.print_field(current_player_token,move)
                chosen_column = input("1 2 3 4 5 6 7 : ")
                while random_number < 10:
                    if chosen_column in ["1","2","3","4","5","6","7"]:
                        column_number= int(chosen_column)
                        if not self.fields[column_number - 1][0] != "-":
                            break
                        else:
                            self.print_field(current_player_token,move)
                            chosen_column = input("1 2 3 4 5 6 7 : ")
                    else:
                        self.print_field(current_player_token,move)
                        chosen_column = input("1 2 3 4 5 6 7 : ")
                self.edit_field(column_number, current_player_token)
                #check is somebody won
                possible_win = self.check_win(current_player_token,move)
                if possible_win == True:
                    break    
            if move >= 42:
                self.print_field(False,move)
                print(input("It is a draw! "))
            self.gameplay()

        #method to check for the win
        def check_win(self, token, move):
            win = False
            #checking 4 vertical
            for i in range(7):
                #have to be at least 4 same tokens
                if self.fields[i].count(token) >= 4:
                    #two in middle of the column need to be same token
                    if self.fields[i][2] == token and self.fields[i][3] == token:
                        #3 possibilities
                        if self.fields[i][1] == token:
                            if self.fields[i][0] == self.fields[i][1] or self.fields[i][4] == self.fields[i][1]:
                                win = True
                        if self.fields[i][4] == token and self.fields[i][4] == self.fields[i][5]:
                            win = True
            #checking 4 horizontal
            for j in range(6):
                #create list for rows
                list = []
                for i in range(7):
                    list.append(self.fields[i][j])
                #have to be at least 4 tokens same kind
                if list.count(token) >= 4:
                    #middle of the row need to be the same
                    if list[3] == token:
                        #4 possibilities left
                        if list[2] == token:
                            if list[1] == token:
                                if list[1] == list[0] or list[1] == list[4]:
                                    win = True
                            if list[4] == token and list[5] == token:
                                win = True
                        if list[4] == token and list[5] == token and list [6] == token:
                            win = True
            #checking 4 diagonal
            if self.fields[3][0] == token:
                if self.fields[0][3] == token and self.fields[0][3] == self.fields[1][2] and self.fields[0][3] == self.fields[2][1]:
                    win = True
                if self.fields[4][1] == token and self.fields[4][1] == self.fields[5][2] and self.fields[4][1] == self.fields[6][3]:
                    win = True
            if self.fields[3][5] == token:
                if self.fields[0][2] == token and self.fields[0][2] == self.fields[1][3] and self.fields[0][2] == self.fields[2][4]:
                    win = True
                if self.fields[4][4] == token and self.fields[4][4] == self.fields[5][3] and self.fields[4][4] == self.fields[6][2]:
                    win = True 
            if self.fields[3][1] == token:
                if self.fields[4][2] == token and self.fields[5][3] == token:
                    if self.fields[2][0] == token or self.fields[6][4] == token:
                        win = True
                if self.fields[1][3] == token and self.fields[2][2] == token:
                    if self.fields[4][0] == token or self.fields[0][4] == token:
                        win = True
            if self.fields[3][4] == token:
                if self.fields[1][2] == token and self.fields[2][3] == token:
                    if self.fields[0][1] == token or self.fields[4][5] == token:
                        win = True
                if self.fields[4][3] == token and self.fields[5][2] == token:
                    if self.fields[2][5] == token or self.fields[6][1] == token:
                        win = True   
            if self.fields[3][3] == token:
                if self.fields[2][2] == token:
                    if self.fields[1][1] == token:
                        if self.fields[0][0] == token or self.fields[4][4] == token:
                            win = True
                    if self.fields[4][4] == token and self.fields[5][5] == token:
                        win = True
                if self.fields[4][2] == token:
                    if self.fields[5][1] == token:
                        if self.fields[6][0] == token or self.fields[2][4] == token:
                            win = True
                    if self.fields[2][4] == token and self.fields[1][5] == token:
                        win = True
            if self.fields[3][2] == token:
                if self.fields[4][3] == token:
                    if self.fields[5][4] == token:
                        if self.fields[6][5] == token or self.fields[2][1] == token:
                            win = True
                    if self.fields[2][1] == token and self.fields[1][0] == token:
                        win = True
                if self.fields[2][3] == token:
                    if self.fields[1][4] == token:
                        if self.fields[0][5] == token or self.fields[4][1] == token:
                            win = True
                    if self.fields[4][1] == token and self.fields[5][0] == token:
                        win = True
            if win == True:
                if token == player1.token:
                    player1.win_counter += 1
                    self.print_field(False,move)
                    input("{win_counter} wins!".format(win_counter=player1.token))
                if token == player2.token:
                    player2.win_counter += 1
                    self.print_field(False,move)
                    input("{win_counter} wins!".format(win_counter=player2.token))
            return win
                            


#initialize the game
game = Four_In_A_Row()
print(game)
input()

#player input name and token, modified so pretty much useless
player1 = Player("one", 1)
player2 = Player("two", 2)
player1.token = "O"
player2.token = "X"

#the game itself
game.gameplay()