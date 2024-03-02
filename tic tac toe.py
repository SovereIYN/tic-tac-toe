print('Welcome to Tic Tac Toe!')

# step 1: create a board
board = ['-','-','-',
         '-','-','-',
         '-','-','-']

def printboard(board):
    print('  1 2 3')
    print('1 ' + board[0] + '|' + board[1] + '|' + board[2])
    print('2 ' + board[3] + '|' + board[4] + '|' + board[5])
    print('3 ' + board[6] + '|' + board[7] + '|' + board[8])
printboard(board)

class Player:
    def __init__(self,name,chip):
        self.name = name
        self.chip = chip

    def player_turn(self):
        x_coordinate = input(self.name + ', please enter the x-value of your position: ')
        y_coordinate = input(self.name + ', please enter the y-value of your position: ')
        if int(x_coordinate) > 3 or int(x_coordinate) < 1 or int(y_coordinate) > 3 or int(y_coordinate) < 1:
            print('Error, please re enter your coordinates')
            self.player_turn()
        else:
            self.choose_position(self.chip,int(x_coordinate),int(y_coordinate))

    def choose_position(self,chip,x,y):
        position = 0
        if x==1 and y==1:
            position = 0
            self.check_taken_position(position)
        elif x==2 and y==1:
            position = 1
            self.check_taken_position(position)
        elif x==3 and y==1:
            position = 2
            self.check_taken_position(position)
        elif x==1 and y==2:
            position = 3
            self.check_taken_position(position)
        elif x==2 and y==2:
            position = 4
            self.check_taken_position(position)
        elif x==3 and y==2:
            position = 5
            self.check_taken_position(position)
        elif x==1 and y==3:
            position = 6
            self.check_taken_position(position)
        elif x==2 and y==3:
            position = 7
            self.check_taken_position(position)
        elif x==3 and y==3:
            position = 8
            self.check_taken_position(position)

    def check_taken_position(self, position):
    
        if board[position] != 'X' and board[position] != 'O':
            board[position] = self.chip
            printboard(board)
        else:
            print('This space is taken, try again')
            self.player_turn()

    def check_win(self):
        if board[0] == board[1] and board[1] == board[2] and board[0] != '-':
            return True
        elif board[3] == board[4] and board[4] == board[5] and board[3] != '-':
            return True
        elif board[6] == board[7] and board[7] == board[8] and board[6] != '-':
            return True
        elif board[0] == board[4] and board[4] == board[8] and board[0] != '-':
            return True
        elif board[2] == board[4] and board[4] == board[6] and board[2] != '-':
            return True
        elif board[0] == board[3] and board[3] == board[6] and board[0] != '-':
            return True
        elif board[1] == board[4] and board[4] == board[7] and board[1] != '-':
            return True
        elif board[2] == board[5] and board[5] == board[8] and board[2] != '-':
            return True
        
    def print_winner(self):
    
        print(self.name + ' has won the game!')
        
                
    def __repr__(self):
        return 'Welcome to the game ' + self.name + ', your chosen chip is: ' + self.chip
player1_name = input('Please enter your name, player 1: ')
player1_chip = input('Please choose if you would want X or O: ')
player1 = Player(player1_name,player1_chip)
# print(player1)

player2_name = input('Please enter your name, player 2: ')
if player1_chip == "X":
    player2_chip = "O"
else:
    player2_chip = "X"
player2 = Player(player2_name, player2_chip)
# print(player2)


    
    


# step 2: player 1 moves
# step 3: check if win 
# step 4: player 2 moves 
    
# step 5: check if win
# step 6: end game
def player1_full_turn():
    player1.player_turn()
    if player1.check_win() == True:
        player1.print_winner()
    elif '-' not in board:
        print('The game has ended in a draw')
    else:
        player2_full_turn()


def player2_full_turn():
    player2.player_turn()
    if player2.check_win() == True:
        player2.print_winner()
    elif '-' not in board:
        print('The game has ended in a draw')
    else:
        player1_full_turn()

player1_full_turn()
