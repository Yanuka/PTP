import chesscore

board = Board()
actualBoard = board.initialize()
board.draw(actualBoard)

print("Hello and welcome to Chess !")
board.draw()
print("Select the piece you want to move and enter the coordinates to where you want to move it to")
coordX = input()
coordY = input()
