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

    selectedPieceX = input("Select the X coordinates of the piece you want to move : ")
    selectedPieceY = input("Select the Y coordinates of the piece you want to move : ")
    selectedCoordX = input("Enter the X coordinates to where you want to move it to : ")
    selectedCoordY = input("Enter the Y coordinates to where you want to move it to : ")

    print("\033[H\033[J")

    if currentPlayerIsOne == False:
        currentPlayerIsOne = True
    else:
        currentPlayerIsOne = False
