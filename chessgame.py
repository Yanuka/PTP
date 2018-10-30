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
    selectedPieceX = int(input("Select the X coordinate of the piece you want to move : ")) - 1
    selectedPieceY = int(input("Select the Y coordinate of the piece you want to move : ")) - 1
    selectedCoordX = int(input("Enter the X coordinate to where you want to move it to : ")) - 1
    selectedCoordY = int(input("Enter the Y coordinate to where you want to move it to : ")) - 1

    #C'est un bout de code test, je suis pas sur que ça fonctionne
    #board.update(selectedPieceX,selectedPieceY,selectedCoordX,selectedCoordY,pieceName)

    print("\033[H\033[J") #Clears the display of the board

    if currentPlayerIsOne == False:
        currentPlayerIsOne = True
    else:
        currentPlayerIsOne = False
