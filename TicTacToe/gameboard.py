#class BoardClass.

class BoardClass:
    '''Attributes:
    user (str): a player's username
    last_player (str): username of the last player to have a turn
    num_wins (int): number of wins
    num_ties (int): number of ties
    num_loss (int): number of losses'''

    #Initializing varibles
    def __init__(self, user1: str='', user2: str='', last_player: str=''):
        self.setUsername1(user1)
        self.setLastPlayer(last_player)
        self.setNumWins1(0)
        self.setNumWins2(0)
        self.setNumTies(0)
        self.setNumLoss1(0)
        self.setNumLoss2(0)
        self.setUsername2(user2)
        self.game_board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
        self.game_count = 1
        self.games_played = 0

    def setUsername1(self, name):
        '''takes name as an argument and sets player 1's username to 'name'. Returns the new username as self.user1.'''
        self.user1 = name
        return self.user1

    def setUsername2(self, name):
        '''takes name as an argument and sets player 2's username to 'name'. Returns the new username as self.user2.'''
        self.user2 = name
        return self.user2

    def setLastPlayer(self, last_player):
        '''takes name as an argument and sets the last_player variable to 'name'. Returns the last_player variable.
        Returns last_player.'''
        self.last_player = last_player
        return self.last_player

    def setNumWins1(self, num_wins):
        '''Takes number of wins as an argument and updates the variable num_wins1 which is the number of wins of player 1 to 
        equal the argument inputted. Returns num_wins1.'''
        self.num_wins1 = num_wins
        return self.num_wins1

    def setNumWins2(self, num_wins):
        '''Takes number of wins as an argument and updates the variable num_wins2 which is the number of wins of player 2 to 
        equal the argument inputted. Returns num_wins2.'''
        self.num_wins2 = num_wins
        return self.num_wins2

    def setNumTies(self, num):
        '''Takes num as an argument. Sets num_ties equal to num. Returns num_ties.'''
        self.num_ties = num
        return self.num_ties

    def setNumLoss1(self, num_loss):
        '''Takes num_loss as an argument. Sets num_loss 1 which is the number of losses for player 1 to num_loss. 
        Returns num_loss1.'''
        self.num_loss1 = num_loss
        return self.num_loss1
    
    def setNumLoss2(self, num_loss):
        '''Takes num_loss as an argument. Sets num_loss 1 which is the number of losses for player 1 to num_loss. 
        Returns num_loss1.'''
        self.num_loss2 = num_loss
        return self.num_loss2

    def updateGamesPlayed(self):
        '''keeps track of how many games have started. Takes no arguments. Adds 1 to the number of games played stored as games_played. 
        Returns games_played.'''
        self.games_played += 1
        return self.games_played

    def resetGameBoard(self):
        '''Clear all the moves from game board. Takes no arguments. Sets game_board to an empty matrix. Returns game_board.'''
        self.game_board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
        return self.game_board

    def updateGameBoard(self, user_input, game_piece):
        '''Updates the game board with the player's move
        This function will take two strings as arguments. user_input will be a string with two number separated by a space such as '1 0' 
        and game_piece will be either 'x' or 'o' depending on which player module it is running in. Implements the move on the game_board.
        Prints the gameboard. Returns True if the move was valid and returns False if the move was not valid.'''
        #Check if the place the user is trying to move to, the row and cell, are within the gameboard and are empty 
        if self.moveValid(user_input) == True:
            #make user_input into two separate objects, the row and cell
            user_place = user_input.split()
            row = int(user_place[0])
            cell = int(user_place[1])
            #if it is valid, place the 'x' or 'o' in the indexed space
            self.game_board[row][cell] = game_piece
            #print the gameboard in three rows so that it is easier to see
            print(self.game_board[0])
            print(self.game_board[1])
            print(self.game_board[2])
            #update the last player based on which gamepiece was implemented
            if game_piece == 'o':
                self.setLastPlayer(self.user2)
            elif game_piece == 'x':
                self.setLastPlayer(self.user1)
            return True
        else:
            return False
    
    def moveValid(self, user_input):
        '''check if a given move is valid meaning the index exists on the board and it is empty, and if the user input was two integers separated by a space.
        This takes the user move and splits it into two objects: the row and the column(cell). Returns True if the move was valid and false if not.'''
        try:
            user_place = user_input.split()
            row = int(user_place[0])
            cell = int(user_place[1])
            #checks if the space that the user is trying to place a piece in is empty and if so return true, if not return False
            if self.game_board[row][cell] == ' ':
                return True
            else:
                return False
        except:
            return False          

    def isWinner(self):
        '''Checks if the latest move resulted in a win.
        Updates the wins and losses count. Returns True of there is a win and False if there is not a win.'''
        #check if there is a horizontal win 
        if self.game_board[0][0] != ' ' and self.game_board[0][0] == self.game_board[0][1] and self.game_board[0][2] == self.game_board[0][0]:
            self.updateGamesPlayed()
            if self.game_board[0][0] == 'x':
                self.num_wins1 += 1
                self.num_loss2 += 1
                return True
            elif self.game_board[0][0] == 'o':
                self.num_wins2 += 1
                self.num_loss1 += 1
                return True
        elif self.game_board[1][0] != ' ' and self.game_board[1][0] == self.game_board[1][1] and self.game_board[1][2] == self.game_board[1][0]:
            self.updateGamesPlayed()
            if self.game_board[1][0] == 'x':
                self.num_wins1 += 1
                self.num_loss2 += 1
                return True
            elif self.game_board[1][0] == 'o':
                self.num_wins2 += 1
                self.num_loss1 += 1
                return True
        elif self.game_board[2][0] != ' ' and self.game_board[2][0] == self.game_board[2][1] and self.game_board[2][2] == self.game_board[2][0]:
            self.updateGamesPlayed()
            if self.game_board[2][0] == 'x':
                self.num_wins1 += 1
                self.num_loss2 += 1
                return True
            elif self.game_board[2][0] == 'o':
                self.num_wins2 += 1
                self.num_loss1 += 1
                return True
        #check if there is a vertical win
        elif self.game_board[0][0] != ' ' and self.game_board[0][0] == self.game_board[1][0] and self.game_board[0][0] == self.game_board[2][0]:
            self.updateGamesPlayed()
            if self.game_board[0][0] == 'x':
                self.num_wins1 += 1
                self.num_loss2 += 1
                return True
            elif self.game_board[0][0] == 'o':
                self.num_wins2 += 1
                self.num_loss1 += 1
                return True
        elif self.game_board[0][1] != ' ' and self.game_board[0][1] == self.game_board[1][1] and self.game_board[0][1] == self.game_board[2][1]:
            self.updateGamesPlayed()
            if self.game_board[0][1] == 'x':
                self.num_wins1 += 1
                self.num_loss2 += 1
                return True
            elif self.game_board[0][1] == 'o':
                self.num_wins2 += 1
                self.num_loss1 += 1
                return True
        elif self.game_board[0][2] != ' ' and self.game_board[0][2] == self.game_board[1][2] and self.game_board[0][2] == self.game_board[2][2]:
            self.updateGamesPlayed()
            if self.game_board[0][2] == 'x':
                self.num_wins1 += 1
                self.num_loss2 += 1
                return True
            elif self.game_board[0][2] == 'o':
                self.num_wins2 += 1
                self.num_loss1 += 1
                return True
        #check if there are diagonal wins
        elif self.game_board[0][0] != ' ' and self.game_board[0][0] == self.game_board[1][1] and self.game_board[0][0] == self.game_board[2][2]:
            self.updateGamesPlayed()
            if self.game_board[0][0] == 'x':
                self.num_wins1 += 1
                self.num_loss2 += 1
                return True
            elif self.game_board[0][0] == 'o':
                self.num_wins2 += 1
                self.num_loss1 += 1
                return True
        elif self.game_board[0][2] != ' ' and self.game_board[0][2] == self.game_board[1][1] and self.game_board[0][2] == self.game_board[2][0]:
            self.updateGamesPlayed()
            if self.game_board[0][2] == 'x':
                self.num_wins1 += 1
                self.num_loss2 += 1
                return True
            elif self.game_board[0][2] == 'o':
                self.num_wins2 += 1
                self.num_loss1 += 1
                return True
        return False
        
    def boardIsFull(self):
        '''Checks if the board is full (I.e. no more moves to make - tie).
        Updates the ties count. Returns True if there is a tie and False if not.'''
        #check if there are any empty spaces in the gameboard, and if not, update the tie counter and return True, if there are return False
        if ' ' not in self.game_board[0] and ' ' not in self.game_board[1] and ' ' not in self.game_board[2]:
            self.num_ties += 1
            return True
        #the reason for the empty space is because I index it in the player modules so I need it to return a tuple of 2 things.
        else:
            return False

    def computeStats(self, current_player):
        '''takes the argument 1 or 2 depending on which player you want to print stats for.
        Returns the following: player 1 username, player 2 username, last player to make a move, number of total games, number of wins, number of losses, number of ties'''
        if current_player == 2:
            return self.user2, self.user1, self.last_player, self.games_played, self.num_wins2, self.num_loss2, self.num_ties
        #if player 1 is asking to print their stats
        if current_player == 1:
            return self.user1, self.user2, self.last_player, self.games_played, self.num_wins1, self.num_loss1, self.num_ties
            print('Your username:', self.user1)
            print('Last player to make a move:', self.last_player)
            print('Number of total games:', self.games_played)
            print('Number of wins:', self.num_wins1)
            print('Number of losses:', self.num_loss1)
        #the number of ties is the same for both
        print('Number of ties:', self.num_ties)
        
