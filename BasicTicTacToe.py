
# Game board
board = ['-','-','-',
        '-','-','-',
        '-','-','-']

currentPlayer = 'X'
winner = None
gameRunning= True


#Print the game board-
def printBoard (board):
    print (board[0] + ' | ' + board[1] + ' | ' + board[2])
    print ('----------')
    print (board[3] + ' | ' + board[4] + ' | ' + board[5])
    print ('----------')
    print (board[6] + ' | ' + board[7] + ' | ' + board[8])


#Take player input
def playerInput(board):
    inp = int(input('Enter a number 1-9:'))
    if inp>= 1 and inp<=9 and board[inp-1] == '-':
        board[inp-1] = currentPlayer
    else:
        print ('Oops, try again!')


#Check for win or tie:
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != '-':
        winner = board[2]
        return True
    elif board[3] == board[4] == board[5] and board[4] != '-':
        winner = board[5]
        return True
    elif board[6] == board[7] == board[8] and board[7] != '-':
        winner = board[7]
        return True

def checkVertical(board):
    global winner
    if board[0] == board [3] == board[6] and board [3] != '-':
        winner = board[6]
        return True
    elif board[1] == board[4] == board[7] and board[4] != '-':
        winner = board[7]
        return True
    elif board[2] == board[5] == board[8] and board[5] != '-':
        winner = board[8]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board [4] != '-':
        winner = board[8]
        return True
    elif board [2] == board[4] == board[6] and board[4] != '-':
        winner = board[6]
        return True

def checkTie(board):
    if '-'  not in board:
        printBoard(board)
        global gameRunning
        gameRunning = False
        print('It\'s a tie!')


def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
        global gameRunning
        gameRunning = False
        print(f'The winner is {winner}')

#Switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'

#Computer
def computer(board):
    while currentPlayer == 'O':
        import random
        position = random.randint(0,8)
        if board[position] == '-':
            board[position] = 'O'
            switchPlayer()

#Game flow
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)