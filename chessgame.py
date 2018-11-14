from chessinit import * #Imports the core program

print("\nHello and welcome to chess !\n\n")
print("Our chess game is inspired by the original chess game.\n\n")
print("Game designed by Lucas, Maxime, Joseph, Alexandre & Morgan\n\n")
input('Press ' + '\33[93m' + 'enter ' + '\x1b[0m' + 'to start the game...')
print("\033[H\033[J") #Clears the board

end = False
while end != True: #Plays the game until the game is ended

    board.draw() #Updates the current board display
    print()

    correctInputPiece=False
    correctInputCoord=False

    while correctInputPiece==False :
        selectedPiece = input("Select the square of the piece you want to move : ") #Gets the initial square
        selectedPiece = selectedPiece.capitalize()
        if len(selectedPiece)!=2 :
            print("\033[H\033[J") #Clears the board
            board.fetch()
            board.draw() #Updates the current board display
            print("The value you have entered is incorrect")
        elif selectedPiece[0].isalpha()==False or selectedPiece[1].isdigit()==False :
            print("\033[H\033[J") #Clears the board
            board.fetch()
            board.draw() #Updates the current board display
            print("The value you have entered is incorrect")
        else:
            correctInputPiece=True

    while correctInputCoord==False :
        selectedCoord = input("Select the square of where you want to move it to : ") #Gets the destination square
        selectedCoord = selectedCoord.capitalize()
        if len(selectedCoord)!=2 :
            print("\033[H\033[J") #Clears the board
            board.fetch()
            board.draw() #Updates the current board display
            print("The value you have entered is incorrect")
        elif selectedCoord[0].isalpha()==False or selectedCoord[1].isdigit()==False :
            print("\033[H\033[J") #Clears the board
            board.fetch()
            board.draw() #Updates the current board display
            print("The value you have entered is incorrect")
        else:
            correctInputCoord=True


    if board.currentPlayerIsOne == False:
        board.currentPlayerIsOne = True
    else:
        board.currentPlayerIsOne = False

    selectedPieceY = ord(selectedPiece[0]) - 65 #Converts the input into coordinates
    selectedPieceX = int(selectedPiece[1]) - 1
    selectedCoordY = ord(selectedCoord[0]) - 65
    selectedCoordX = int(selectedCoord[1]) - 1

    print("\033[H\033[J") #Clears the board
