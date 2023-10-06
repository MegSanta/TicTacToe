#Module for GUI for the server, A.K.A player 2
import tkinter as tk
from gameboard import BoardClass
import socket

class GUI():


    def __init__(self):
        '''Initialize variables self.IPSV, self.portIV, self.username2SV, self.port, self.username2, self.IP, create a BoardClass object, create
        a socket object, and call canvasSetup.'''
        self.canvasSetup()
        #This is the string variable for the user to enter their IP address
        self.IPSV = tk.StringVar(self.root, value='127.0.0.1')
        #This is the integer variable for the user to enter their port
        self.portIV = tk.IntVar(self.root, value='8001')
        #This is the string variabe for the user to enter their username
        self.username2SV = tk.StringVar(self.root, value='player2')
        #This is the variable for player 2's port
        self.port = 0
        #This is the string for player 2's username
        self.username2 = ''
        #This is the string for player 2's IP address
        self.IP = ''
        #Create a board object
        self.my_board = BoardClass()
        #Create a socket objecct
        self.socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def canvasSetup(self):
        '''Set up the window for the game to be played in.'''
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe Server") #sets the window title
        self.root.geometry('400x400') #sets default size of window
        self.root.configure(background='green') #makes the background blue
        self.root.resizable(1,1) #0 means not resizable, 1 means resizable
        self.root
    def textEntryIP(self):
        '''Create a widget for entering the host IP into.'''
        self.IPEntryLabel = tk.Label(self.root, text='Please enter the host name/IP address (for local use 127.0.0.1):').grid(row=1, column=0, padx=10, pady=10)
        self.IPEntry = tk.Entry(self.root, text=self.IPSV).grid(row=1, column=1, padx=10, pady=10)
        self.IPEntryButton = tk.Button(self.root, text='Enter', command=lambda: [self.getTextEntryIP(), self.widgetDisable(self.IPEntryButton)])
        self.IPEntryButton.grid(row=1, column=2, padx=10, pady=10)
    def getTextEntryIP(self):
        '''Get a string variable from a text entry and assign it to a permanant variable.'''
        self.IP = str(self.IPSV.get())
    def getTextEntryUsername2(self):
        '''Get a string variable from a text entry and assign it to a permanant variable.'''
        self.username2 = str(self.username2SV.get())
    def combinedUsername2(self):
        '''A set of functions to be carried out by the username 'Enter' button.'''
        self.getTextEntryUsername2()
        self.setUsername2(self.username2SV)
        self.checkTextEntry(self.username2SV)
    def getNumEntry(self):
        '''Get an integer variable from a text entry and assign it to a permanent variable.'''
        self.checkNumEntry(self.portIV)
        self.port = int(self.portIV.get())
    def checkNumEntry(self, num):
        '''Check if the entry is an integer.'''
        try:
            num = int(num.get())
            self.widgetDisable(self.portEntryButton)
        except:
            self.errorWindow = tk.Toplevel(self.root)
            self.ErrorEntryLabel = tk.Label(self.errorWindow, text='Please follow directions and try again.').grid(row=0, column=0, padx=10, pady=10)
            self.closeWindowButton = tk.Button(self.errorWindow, text= 'exit', command=self.errorWindow.destroy).grid(row=1, column=0, padx=10, pady=10)
    def widgetDisable(self, widget):
        '''Delete a text entry box after use.'''
        widget['state'] = 'disabled'
    def checkTextEntry(self, text):
        '''Checks if a text entry is alphanumeric. If it is not, creates a window with an error message and a close button.'''
        text = str(text.get())
        if text.isalnum() == True:
            self.widgetDisable(self.usernameEntryButton)
            return
        elif text.isalnum() == False:
            self.errorWindow = tk.Toplevel(self.root)
            self.ErrorEntryLabel = tk.Label(self.errorWindow, text='Please follow directions and try again.').grid(row=0, column=0, padx=10, pady=10)
            self.closeWindowButton = tk.Button(self.errorWindow, text= 'exit', command=self.errorWindow.destroy).grid(row=1, column=0, padx=10, pady=10)                        
    def textEntryPort(self):
        '''Create a widget for entering port number into.'''
        self.portEntryLabel = tk.Label(self.root, text='Please enter the number of the port you would like to use to play the game (this should be an integer, probably above 8,000):').grid(column=0, row=2, padx=10, pady=10)
        self.portEntry = tk.Entry(self.root, text=self.portIV).grid(column=1, row=2, padx=10, pady=10)
        self.portEntryButton = tk.Button(self.root, text='Enter', command=lambda: self.getNumEntry())
        self.portEntryButton.grid(row=2, column=2, padx=10, pady=10)
    def textEntryUsername2(self):
        '''Create a label, text entry box, and button so that the user can input their username and save it.'''
        self.usernameEntryLabel = tk.Label(self.root, text='Please input your username:').grid(row=0, column=0, padx=10, pady=10)
        self.usernameEntry = tk.Entry(self.root, text=self.username2SV).grid(row=0, column=1, padx=10, pady=10)
        self.usernameEntryButton = tk.Button(self.root, text='Enter', command=lambda: self.combinedUsername2())
        self.usernameEntryButton.grid(row=0, column=2, padx=10, pady=10)
    def gameBoardCreate(self):
        '''Create a gameBoard. Row is the first number and column is the second.'''
        self.frame1 = tk.Frame(self.root)
        self.frame1.configure(background='light green')
        self.frame1.grid(row=4, column=0, padx=10, pady=10)
        space = 10
        my_text = '   '
        h = 4
        w = 8
        self.button00 = tk.Button(self.frame1, text=my_text, height=h, width=w, command=lambda: [self.player2Move('0 0')])
        self.button00.grid(row=2, column=0, padx=space, pady=space)
        self.button01 = tk.Button(self.frame1, text=my_text, height=h, width=w, command=lambda: [self.player2Move('0 1')])
        self.button01.grid(row=2, column=1, padx=space, pady=space)
        self.button02 = tk.Button(self.frame1, text=my_text, height=h, width=w, command=lambda: [self.player2Move('0 2')])
        self.button02.grid(row=2, column=2, padx=space, pady=space)
        self.button10 = tk.Button(self.frame1, text=my_text, height=h, width=w, command=lambda: [self.player2Move('1 0')])
        self.button10.grid(row=3, column=0, padx=space, pady=space)
        self.button11 = tk.Button(self.frame1, text=my_text, height=h, width=w, command=lambda: [self.player2Move('1 1')])
        self.button11.grid(row=3, column=1, padx=space, pady=space)
        self.button12 = tk.Button(self.frame1, text=my_text, height=h, width=w, command=lambda: [self.player2Move('1 2')])
        self.button12.grid(row=3, column=2, padx=space, pady=space)
        self.button20 = tk.Button(self.frame1, text=my_text, height=h, width=w, command=lambda: [self.player2Move('2 0')])
        self.button20.grid(row=4, column=0, padx=space, pady=space)
        self.button21 = tk.Button(self.frame1, text=my_text, height=h, width=w, command=lambda: [self.player2Move('2 1')])
        self.button21.grid(row=4, column=1, padx=space, pady=space)
        self.button22 = tk.Button(self.frame1, text=my_text, height=h, width=w, command=lambda: [self.player2Move('2 2')])
        self.button22.grid(row=4, column=2, padx=space, pady=space)
    def displayStats(self):
        '''Display statistics when the player is done.'''
        self.frame2 = tk.Frame(self.root)
        self.frame2.configure(background='dark green')
        self.frame2.grid(row=4, column=2, padx=10, pady=10)
        text1 = 'Your username:', self.my_board.user2
        text2 = 'Last player to make a move:', self.my_board.last_player
        text3 = 'Number of total games:', self.my_board.games_played
        text4 = 'Number of wins:', self.my_board.num_wins2
        text5 = 'Number of losses:', self.my_board.num_loss2
        text6 = 'Number of ties:', self.my_board.num_ties
        text7 = 'Player 1\'s username', self.my_board.user1
        self.finalResultsLabel = tk.Label(self.frame2, text='Final Results').grid(row=0, column=0, padx=5, pady=5)
        self.user1Label = tk.Label(self.frame2, text=text7).grid(row=1, column=0, padx=5, pady=5)
        self.user2Label = tk.Label(self.frame2, text=text1).grid(row=2, column=0, padx=5, pady=5)
        self.lastMoveLabel = tk.Label(self.frame2, text=text2).grid(row=3, column=0, pady=5, padx=5)
        self.numGamesLabel = tk.Label(self.frame2, text=text3).grid(row=4, column=0, pady=5, padx=5)
        self.numWinsLabel = tk.Label(self.frame2, text=text4).grid(row=5, column=0, pady=5, padx=5)
        self.numLossLabel = tk.Label(self.frame2, text=text5).grid(row=6, column=0, pady=5, padx=5)
        self.numTiesLabel = tk.Label(self.frame2, text=text6).grid(row=7, column=0, pady=5, padx=5)
    def whoseTurnCreate(self):
        '''Display which player's turn it is.'''
        self.turn = tk.Label(self.root, text= 'It is this player\'s turn:').grid(row=6, column=0, sticky='NE', padx=10, pady=10)
        self.userTurn = tk.Label(self.root, text= '  ')
        self.userTurn.grid(row=6, column=1, sticky='NW', padx=10, pady=10)
    def whoseTurnUpdate(self, newText):
        '''Update which player's turn it is.'''
        self.userTurn['text'] = newText
    def gameBoardUpdate(self, button, turn):
        '''Update the widget gameboard to disable buttons on spaces that have been taken and mark spaces that have been taken with the 
        appropriate game piece.'''
        if turn == 2:
            button['state'] = 'disabled'
            button['text'] = 'o'

        elif turn == 1:
            button['state'] = 'disabled'
            button['text'] = 'x'

    def connectButtonCreate(self):
        '''A button for the user to try and connect to the client.'''
        self.connectButton = tk.Button(self.root, text='Connect', command=self.combinedConnect)
        self.connectButton.grid(row=2, column=4, padx=10, pady=10)
    def combinedConnect(self):
        '''Try to connect to the client.'''
        self.socket_obj.bind((self.IP, self.port))
        self.socket_obj.listen(1)
        self.connection, self.address = self.socket_obj.accept()
        self.widgetDisable(self.connectButton)
        self.receiveUsername1()
        self.setUsername1()
        self.sendUsername2()
        self.widgetDisable(self.connectButton)
        self.whoseTurnUpdate(self.username1)
        self.player1Move()
        
    def receiveUsername1(self):
        '''Receive player 1's username.'''
        self.username1 = self.connection.recv(1024)
        
    def setUsername1(self):
        '''Set player 1's username.'''
        self.my_board.setUsername1(self.username1.decode('utf-8'))
    def setUsername2(self, SV):
        '''Set player 2's username.'''
        self.checkTextEntry(SV)
        self.my_board.setUsername2(self.username2)
    def sendUsername2(self):
        '''Send player 2's username.'''
        self.connection.send(self.username2.encode('utf-8'))
    def player2Move(self, button):
        '''Match player 2's move to a string to send to player 1. Send the move to player 1. Update the gameboard with player 2's move.'''
        if button == '0 0':
            self.player2MoveString = '0 0'
            self.gameBoardUpdate(self.button00, 2)
        elif button == '0 1':
            self.player2MoveString = '0 1'
            self.gameBoardUpdate(self.button01, 2)
        elif button == '0 2':
            self.player2MoveString = '0 2'
            self.gameBoardUpdate(self.button02, 2)
        elif button == '1 0':
            self.player2MoveString = '1 0'
            self.gameBoardUpdate(self.button10, 2)
        elif button == '1 1':
            self.player2MoveString = '1 1'
            self.gameBoardUpdate(self.button11, 2)
        elif button == '1 2':
            self.player2MoveString = '1 2'
            self.gameBoardUpdate(self.button12, 2)
        elif button == '2 0':
            self.player2MoveString = '2 0'
            self.gameBoardUpdate(self.button20, 2)
        elif button == '2 1':
            self.player2MoveString = '2 1'
            self.gameBoardUpdate(self.button21, 2)
        elif button == '2 2':
            self.player2MoveString = '2 2'
            self.gameBoardUpdate(self.button22, 2)
        self.my_board.updateGameBoard(self.player2MoveString,'o')
        self.whoseTurnUpdate(self.my_board.user1)
        self.connection.send(self.player2MoveString.encode('utf-8'))
        if self.my_board.isWinner():
            self.playAgain = self.connection.recv(1024)
            if self.playAgain.decode('ascii') == 'Play Again':
                self.newGame()
                return
            else:
                self.displayStats()
                self.userTurn.destroy()
                self.socket_obj.close()
                return
        elif self.my_board.boardIsFull():
            self.playAgain = self.connection.recv(1024)
            if self.playAgain.decode('ascii') == 'Play Again':
                self.newGame()
                return
            else:
                self.displayStats()
                self.userTurn.destroy()
                self.socket_obj.close()
                return
        self.player1Move()

    def player1Move(self):
        '''Receive player 1's move. Update the gameboard with player 1's move. Update the widget gameboard with player 1's move.'''
        self.player1MoveString = self.connection.recv(1024).decode('ascii')
        self.my_board.updateGameBoard(self.player1MoveString,'x')
        if self.player1MoveString == '0 0':
            self.gameBoardUpdate(self.button00, 1)
        elif self.player1MoveString == '0 1':
            self.gameBoardUpdate(self.button01, 1)
        elif self.player1MoveString == '0 2':
            self.gameBoardUpdate(self.button02, 1)
        elif self.player1MoveString == '1 0':
            self.gameBoardUpdate(self.button10, 1)
        elif self.player1MoveString == '1 1':            
            self.gameBoardUpdate(self.button11, 1)
        elif self.player1MoveString == '1 2':
            self.gameBoardUpdate(self.button12, 1)
        elif self.player1MoveString == '2 0':
            self.gameBoardUpdate(self.button20, 1)
        elif self.player1MoveString == '2 1':
            self.gameBoardUpdate(self.button21, 1)
        elif self.player1MoveString == '2 2':
            self.gameBoardUpdate(self.button22, 1)

        self.whoseTurnUpdate(self.my_board.user2)
        if self.my_board.isWinner():
            self.playAgain = self.connection.recv(1024)
            if self.playAgain.decode('ascii') == 'Play Again':
                self.newGame()
                return
            else:
                self.displayStats()
                self.userTurn.destroy()
                self.socket_obj.close()
                return
        elif self.my_board.boardIsFull():
            self.playAgain = self.connection.recv(1024)
            if self.playAgain.decode('ascii') == 'Play Again':
                self.newGame()
                return
            else:
                self.displayStats()
                self.userTurn.destroy()
                self.socket_obj.close()
                return
                    
    def newGame(self):
        '''Reset the gameboard'''
        self.button00['state'] = 'normal'
        self.button01['state'] = 'normal'
        self.button02['state'] = 'normal'
        self.button10['state'] = 'normal'
        self.button11['state'] = 'normal'
        self.button12['state'] = 'normal'
        self.button20['state'] = 'normal'
        self.button21['state'] = 'normal'
        self.button22['state'] = 'normal'
        self.button00['text'] = '  '
        self.button01['text'] = '  '
        self.button02['text'] = '  '
        self.button10['text'] = '  '
        self.button11['text'] = '  '
        self.button12['text'] = '  '
        self.button20['text'] = '  '
        self.button21['text'] = '  '
        self.button22['text'] = '  '
        self.whoseTurnUpdate('')
        self.my_board.resetGameBoard()
        self.player1Move()
        
    
        
         


if __name__ == "__main__":
    player2GUI = GUI()
    #initialize the canvas
    #ask user for host information of player 2
    player2GUI.textEntryIP()
    player2GUI.textEntryPort()
    #Bind host name and port
    player2GUI.connectButtonCreate()
    my_board = BoardClass()
    player2GUI.gameBoardCreate()
    player2GUI.whoseTurnCreate()
    #store player 1's username in the gameboard
    player2GUI.textEntryUsername2()
