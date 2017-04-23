def playTicTacToeGame(board):
    player1 = 'X'
    player2 = 'O'
    current_player = player1
    printBoard(board)
    while (not isFull(board)):
        current_player_xpos = input("Player " + current_player + ", please enter the row number of your move: ")
        current_player_ypos = input("Player " + current_player + ", please enter the column number of your move: ")
        updateBoard(current_player_xpos - 1, current_player_ypos - 1, board, current_player)
        printBoard(board)
        if checkWinner(board, current_player):
            print "Congratulations, player ", current_player, " has won"
            return
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
    print "Looks like a draw"
    return


def isFull(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == '':
                return False

    return True

def updateBoard(x, y, board, player):
    while not (board[x][y] == ''):
        print "Sorry already taken my friend, please enter again"
        x = input("Player " + player + ", please enter the row number of your move: ") - 1
        y = input("Player " + player + ", please enter the column number of your move: ") - 1
    board[x][y] = player


def checkWinner(board, player):
    # checks the TicTacToe board for a winner
    return checkHorz(board, player) or checkVert(board, player) or checkDiag(board, player)


def checkHorz(board, player):
    winCounter = 0
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == player:
                winCounter += 1
            else:
                None
        if winCounter == len(board):
            return True
        winCounter = 0

    return False


def checkVert(board, player):
    winCounter = 0
    for x in range(len(board)):
        for y in range(len(board)):
            if board[y][x] == player:
                winCounter += 1
            else:
                None
        if winCounter == len(board):
            return True
        winCounter = 0

    return False


def checkDiag(board, player):
    winCounter = 0
    y = 0
    for x in range(len(board)):
        if board[x][y] == player:
            winCounter += 1
        else:
            None
        y += 1
    if winCounter == len(board):
        return True

    winCounter = 0

    x = len(board) - 1
    for y in range(len(board)):
        if board[x][y] == player:
            winCounter += 1
        else:
            None
        x -= 1
    if winCounter == len(board):
        return True

    return False


def printBoard(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == '':
                print "#",
            else:
                print board[x][y],
        print


def generateBoard(x, y):
    board = []
    for i in range(x):
        board.append([])
        for j in range(y):
            board[i].append('')
    return board


gameBoard = generateBoard(3, 3)
playTicTacToeGame(gameBoard)
