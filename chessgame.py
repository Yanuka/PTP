from chessinit import * #Imports the core program

print("\nHello and welcome to chess !\n\n")
print("Our chess game is inspired by the original chess game.\n\n")
print("Game designed by Lucas, Maxime, Joseph, Alexandre & Morgan\n\n")
input('Press ' + '\33[93m' + 'enter ' + '\x1b[0m' + 'to start the game...')
print("\033[H\033[J") #Clears the board

end = False
while end != True: #Plays the game until the game is ended
    if board.currentPlayerIsOne == False :
        board.currentPlayerIsOne = True
        playerColor = "Black"
    else:
        board.currentPlayerIsOne = False
        playerColor = "White"

    board.fetch()
    board.draw() #Updates the current board display
    print()

    correctInputPiece = False
    correctInputCoord = False

    allowedInputLetter = ["A","B","C","D","E","F","G","H"]

    while correctInputPiece==False :
        selectedPiece = input("Select the square of the piece you want to move : ") #Gets the initial square
        selectedPiece = selectedPiece.capitalize()

        if len(selectedPiece)!=2 :
            board.update()
            print("Please enter the coordinates like this : \'E4\'")
        elif selectedPiece[0].isalpha()==False or selectedPiece[0] not in allowedInputLetter or selectedPiece[1].isdigit()==False or int(selectedPiece[1])<1 or int(selectedPiece[1])>8 :
            board.update()
            print("The value you have entered is incorrect")
        elif board.getPlayerColor((int(selectedPiece[1]) - 1), (ord(selectedPiece[0]) - 65), playerColor) == True:
            board.update()
            print("Please select a piece of your color!")
        else:
            correctInputPiece=True

    board.update()

    while correctInputCoord==False :
        selectedCoord = input("\nSelect the square of where you want to move it to : ") #Gets the destination square
        selectedCoord = selectedCoord.capitalize()

        if len(selectedCoord)!=2 :
            board.update()
            print("Please enter the coordinates like this : \'E5\'")
        elif selectedCoord[0].isalpha()==False or selectedCoord[0] not in allowedInputLetter or selectedCoord[1].isdigit()==False or int(selectedCoord[1])<1 or int(selectedCoord[1])>8 :
            board.update()
            print("The value you have entered is incorrect")
        else:
            correctInputCoord=True

        selectedPieceY = ord(selectedPiece[0]) - 65 #Converts the input into coordinates
        selectedPieceX = int(selectedPiece[1]) - 1
        selectedCoordY = ord(selectedCoord[0]) - 65
        selectedCoordX = int(selectedCoord[1]) - 1

    for piece in board.coordinates:
        if piece[1][0]==selectedPieceX and piece[1][1]==selectedPieceY:
            piece[0].movePiece(selectedPieceX,selectedPieceY,selectedCoordX,selectedCoordY,board)
    print("\033[H\033[J") #Clears the board
