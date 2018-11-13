from chesscore import * #Imports the core program

"""
print("Hello and welcome to Chess !")
currentPlayerIsOne = True
end = False
while end != True: #Plays the game until the game is ended

    if currentPlayerIsOne == True:
        print('Player ' + '\33[31m' + '1' + '\x1b[0m' + '\'s turn')
    else:
        print('Player ' + '\33[34m' + '2' + '\x1b[0m' + '\'s turn')
    board.draw() #Updates the current board display
    print()
    selectedPiece = input("Select the square of the piece you want to move : ") #Gets the square of the piece
    if len(selectedPiece)>2 :
        print("The value you have entered is incorrect")
    selectedCoord = input("Select the square to where you want to move the piece : ") #Gets the square of the coordinates
    if len(selectedCoord)>2 :
        print("The value you have entered is incorrect")
    selectedPieceX = ord(selectedPiece[0]) - 65 #Converts the input into coordinates
    selectedPieceY = int(selectedPiece[1]) - 1
    selectedCoordX = ord(selectedCoord[0]) - 65
    selectedCoordY = int(selectedCoord[1]) - 1

    print("\033[H\033[J") #Clears the board

    if currentPlayerIsOne == False:
        currentPlayerIsOne = True
    else:
        currentPlayerIsOne = False
"""
