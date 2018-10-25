from chesscore import *
import os

board = Board()
actualBoard = board.initialize()

print("Hello and welcome to Chess !")
playerOne = False
end = False
while end != True:

    if playerOne == False:
        print("Player 1's turn")
    else:
        print("Player 2's turn")
    board.draw(actualBoard)
    print("Select the piece you want to move and enter the coordinates to where you want to move it to")
    coordX = input()
    coordY = input()
    os.system('cls')
    os.system('clear')
    if playerOne == True:
        playerOne = False
    else:
        playerOne = True
