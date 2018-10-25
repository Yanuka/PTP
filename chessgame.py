from chesscore import *

board = Board()
actualBoard = board.initialize()

print("Hello and welcome to Chess !")
end = False
while end != True:

    board.draw(actualBoard)
    print("Select the piece you want to move and enter the coordinates to where you want to move it to")
    coordX = input()
    coordY = input()
