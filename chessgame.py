from chessinit import * #Imports the core program

print("\nHello and welcome to chess !\n\n") #Displays a welcome interface
print("Our chess game is inspired by the original chess game.\n\n")
print("Game designed by Lucas, Maxime, Joseph, Alexandre & Morgan\n\n")
input('Press ' + '\33[93m' + 'enter ' + '\x1b[0m' + 'to start the game...')
print("\033[H\033[J") #Clears the board

end = False
while end != True: #Plays the game until the game is ended
    if board.currentPlayerIsOne == False : #Turn of player Black
        board.currentPlayerIsOne = True
        playerColor = "Black"
    else: #Turn of player White
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
        selectedPiece = selectedPiece.capitalize() #Forces the capitalization of the letter

        if len(selectedPiece)!=2 : #Checks if the the length is correct
            board.update() #Updates the board
            print("Please enter the coordinates like this : \'E4\'")
        elif selectedPiece[0].isalpha()==False or selectedPiece[0] not in allowedInputLetter or selectedPiece[1].isdigit()==False or int(selectedPiece[1])<1 or int(selectedPiece[1])>8 : #Cheks if the entered input is correctly syntaxed
            board.update() #Updates the board
            print("The value you have entered is incorrect")
        elif board.getPlayerColor((int(selectedPiece[1]) - 1), (ord(selectedPiece[0]) - 65), playerColor) == True: #Checks if the piece selected is the right color
            board.update() #Updates the board
            print("Please select a piece of your color!")
        else:
            correctInputPiece=True #Tells the program that the input was correctly executed

    board.update() #Updates the board

    while correctInputCoord==False :
        selectedCoord = input("\nSelect the square of where you want to move it to : ") #Gets the destination square
        selectedCoord = selectedCoord.capitalize() #Forces the capitalization of the letter

        if len(selectedCoord)!=2 : #Checks if the the length is correct
            board.update() #Updates the board
            print("Please enter the coordinates like this : \'E5\'")
        elif selectedCoord[0].isalpha()==False or selectedCoord[0] not in allowedInputLetter or selectedCoord[1].isdigit()==False or int(selectedCoord[1])<1 or int(selectedCoord[1])>8 : #Cheks if the entered input is correctly syntaxed
            board.update() #Updates the board
            print("The value you have entered is incorrect")
        else:
            correctInputCoord=True #Tells the program that the input was correctly executed

    selectedPieceY = ord(selectedPiece[0]) - 65 #Converts the selected piece into Y coordinates
    selectedPieceX = int(selectedPiece[1]) - 1 #Converts the selected piece into X coordinates
    selectedCoordY = ord(selectedCoord[0]) - 65 #Converts the selected coordinates into Y coordinates
    selectedCoordX = int(selectedCoord[1]) - 1 #Converts the selected coordinates into X coordinates

    pieceCaptured = False
    for piece in board.coordinates : #Moves the selected piece
        if pieceCaptured == True :
            break
        elif piece[1][0]==selectedPieceX and piece[1][1]==selectedPieceY:
            print('1')
            piece[0].moveList(selectedPieceX, selectedPieceY, board)
            for pieceToCapture in piece[0].capturePossible:
                print('2')
                if  pieceToCapture[0] == selectedCoordX and  pieceToCapture[1] == selectedCoordY:
                    print('3')
                    supervisor.capturePiece(selectedCoordX,selectedCoordY,board)
                    pieceCaptured = True
                    break

    for piece in board.coordinates :
        if piece[1][0]==selectedPieceX and piece[1][1]==selectedPieceY:
            piece[0].movePiece(selectedPieceX,selectedPieceY,selectedCoordX,selectedCoordY,board)



    #print("\033[H\033[J") #Clears the board
