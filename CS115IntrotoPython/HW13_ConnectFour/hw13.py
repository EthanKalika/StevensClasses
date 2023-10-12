# Ethan Kalika
# "I pledge my honor that I have abided By the Stevens Honor System"


class Board:
    def __init__(self, w = 7, h = 6):
        '''
        Input: Two integers (w and h)
        Action: Creates an instance of board with w columns and h rows
        '''
        self.width = w
        self.height = h
        array = []
        gameBoard = []
        for i in range(self.height):
            for i in range(self.width):
                array += [' ']
            gameBoard += [array]
            array = []
        self.board = gameBoard

    def __str__(self):
        '''
        Input: None
        Output: A string representation of the board
        '''
        theString = ''
        theNumbers = ''
        i = 0
        for element in self.board:
            theString += '|' + ('|'.join(element) + '|' + '\n')
            theNumbers += ' ' + str(i)
            i += 1
        return theString + '-' * (2 * self.width + 1) + '\n' + theNumbers + ' ' + str(i)

    def get_board(self):
        '''
        Input: None
        Output: The board
        '''
        return self.board

    def allowsMove(self, col):
        '''
        Input: An integer col
        Output: A boolean representing weather or not a move can be made in column col
        '''
        if not (0 <= col <= self.width):
            return False
        for element in self.board:
            if element[col] == ' ':
                return True
        return False

    def addMove(self, col, ox):
        '''
        Input: A column number col and a string which is either O or X
        Action: Puts the given string in that column where available
        '''
        if self.allowsMove(col):
            isEmpty = True
            for element in range(1, self.height):
                if self.board[element][col] != ' ' and self.board[element - 1][col] == ' ':
                    self.board[element - 1][col] = ox
                    isEmpty = False
            if isEmpty:
                self.board[self.height - 1][col] = ox

    def setBoard(self, moveString):
        """ takes in a string of columns and places
         alternating checkers in those columns,
         starting with 'X'

         For example, call b.setBoard('012345')
         to see 'X's and 'O's alternate on the
         bottom row, or b.setBoard('000000') to
         see them alternate in the left column.
         moveString must be a string of integers
         """
        nextCh = 'X' # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'

    def delMove(self, col):
        '''
        Input: An integer representing a column
        Action: Removes the last move mad in that column if it exists
        '''
        if 0 <= col <= self.width and self.board[-1][col] != ' ':
            if self.board[0][col] != ' ':
                self.board[0][col] = ' '
            else:
                for element in range(self.height - 1):
                    if self.board[element][col] == self.board[element][col - 1]:
                        self.board[element][col] = ' '

    def winsFor(self, ox):
        '''
        Input: A string that is either O or X
        Output: A boolean representing if either player has won
        '''
        for i in range(self.height):
            for j in range(self.width - 3):
                if self.board[i][j] == ox and self.board[i][j + 1] == ox and self.board[i][j + 2] == ox and self.board[i][j + 3] == ox:
                    return True
        for i in range(self.height - 3):
            for j in range(self.width):
                if self.board[i][j] == ox and self.board[i + 1][j] == ox and self.board[i + 2][j] == ox and self.board[i + 3][j] == ox:
                    return True
        for i in range(self.width - 3):
            for j in range(self.height - 3):
                if self.board[j][i] == ox and self.board[j + 1][i + 1] == ox and self.board[j + 2][i + 2] == ox and self.board[j + 3][i + 3] == ox:
                    return True
        for i in range(3, self.width):
            for j in range(self.height - 3):
                if self.board[j][i] == ox and self.board[j + 1][i - 1] == ox and self.board[j + 2][i - 2] == ox and self.board[j + 3][i - 3] == ox:
                    return True
        return False

    def hostGame(self):
        '''
        Input: None
        Action: Runs a game
        '''
        print("\n\nWelcome to Connect Four!")
        print(str(self) + "\n")
        while(not self.winsFor('X') and not self.winsFor('O')):
            player1Turn = int(input("X's choice:  "))
            self.addMove(player1Turn, 'X')
            if self.winsFor('X'):
                print('\n\nX wins -- Congradulations!\n')
                print(self)
            else:
                print('\n' + str(self) + '\n')
                player2Turn = int(input("O's choice:  "))
                self.addMove(player2Turn, 'O')
                if not self.winsFor('O'):
                    print('\n' + str(self) + '\n')
        if (self.winsFor('O')):
            print('\n\nO wins -- Congradulations!\n')
            print(self)
