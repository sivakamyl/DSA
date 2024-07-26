
'''
Code for Tic-Tac-Toe with a 3x3 grid and 2 players alternatively filling Xs and Os.
To win:
One player is able to place 3 symbols of the same type either
 - horizontally
 - vertically
 - diagonally

 Stopping criteria:
 - If and when any player wins 
 OR
 - If all 9 spots in the grid are filled, in which it becomes a draw
'''

board = [[None, None, None], [None, None, None], [None, None, None]]

# Display the current state of the 3x3 grid
def displayBoard():
    for rowNum in range(3):
        for colNum in range(3):
            print(" " if board[rowNum][colNum]==None else board[rowNum][colNum], end = " ")
            if colNum < 2:
                print ("|", end=" ")
        if rowNum < 2:
            print("\n----------")

# Variables for controlling Play
playing = True
spotsLeft = 9

# Variables for controlling Players. Let's have them as 0 and 1.
currentPlayer = 0

while playing:
    print ("\n\n ROUND ", str(9-spotsLeft + 1), " | PLAYER ", int(currentPlayer))

    # Get player choice for symbol placement
    row, col = input("\nEnter row and column of target grid: ").split()
    row = int(row)
    col = int(col)

    # Validations
    if row > 2 or col > 2:
        print ("Yikes! Invalid row/col number. Try a valid one this time!")
        continue
    if board[row][col] != None:
        print ("Yikes! Grid is already filled. Try a valid one this time!")
        continue

    # Mark the symbol on the chosen spots
    board[row][col] = "X" if currentPlayer else "O"
    displayBoard()

    # Updating controls for next round
    spotsLeft = spotsLeft - 1
    currentPlayer = not currentPlayer #toggling

    # Update playing to false if stopping criteria is reached
    if spotsLeft == 0:
        playing = False

