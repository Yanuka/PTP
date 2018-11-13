from chesscore import * #Imports the core program

board = Board() #Starts the game


print("Hello and welcome to Chess !")
currentPlayerIsOne = True
end = False
while end != True: #Plays the game until the game is ended

    if currentPlayerIsOne == True:
        print("Player 1's turn\n")
    else:
        print("Player 2's turn\n")
    board.draw() #Updates the current board display
    print()
    selectedPiece = input("Select the square of the piece you want to move")
    selectedCoord = input("Select the square to where you want to move the piece")

    selectedPieceX = selectedPiece
    selectedPieceY = selectedPiece
    selectedCoordX = selectedCoord
    selectedCoordY = selectedCoord

    print("\033[H\033[J") #Clears the display of the board

    if currentPlayerIsOne == False:
        currentPlayerIsOne = True
    else:
        currentPlayerIsOne = False
