from chesscore import *
import os

board = Board()

print("Hello and welcome to Chess !")
currentPlayerIsOne = True
end = False
while end != True:

    if currentPlayerIsOne == True:
        print("Player 1's turn")
    else:
        print("Player 2's turn")
    board.draw()
    print("Select the piece you want to move")
    selectedPieceX = input()
    selectedPieceX = input()
    print("Enter the coordinates to where you want to move it to")
    selectedCoordX = input()
    selectedCoordY = input()
    print("\033[H\033[J")
    if currentPlayerIsOne == False:
        currentPlayerIsOne = True
    else:
        currentPlayerIsOne = False
