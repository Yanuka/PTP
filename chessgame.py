from chesscore import *
import os

board = Board()

print("Hello and welcome to Chess !")
currentPlayerIsOne = True
end = False
while end != True:

    if currentPlayerIsOne == True:
        print("Player 1's turn\n")
    else:
        print("Player 2's turn\n")
    board.draw()
    print()
    selectedPieceX = int(input("Select the X coordinate of the piece you want to move : ")) - 1
    selectedPieceY = int(input("Select the Y coordinate of the piece you want to move : ")) - 1
    selectedCoordX = int(input("Enter the X coordinate to where you want to move it to : ")) - 1
    selectedCoordY = int(input("Enter the Y coordinate to where you want to move it to : ")) - 1

    print("\033[H\033[J")

    if currentPlayerIsOne == False:
        currentPlayerIsOne = True
    else:
        currentPlayerIsOne = False
