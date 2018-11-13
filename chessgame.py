from chessinit import * #Imports the core program

print("Hello and welcome to chess !\n")
print("Our chess game is inspired by the og chess game.\n")
print("Game designed by Lucas, Maxime, Joseph, Alexandre & Morgan\n")
input("Press enter to start the game...")
print("\033[H\033[J") #Clears the board


end = False
while end != True: #Plays the game until the game is ended

    board.draw() #Updates the current board display
    print()

    correctInputPiece=False
    correctInputCoord=False

    while correctInputPiece==False :
        selectedPiece = input("Select the square of the piece you want to move : ") #Gets the initial square
        if len(selectedPiece)!=2 :
            print("\033[H\033[J") #Clears the board
            board.draw() #Updates the current board display
            print("The value you have entered is incorrect")
        elif selectedPiece[0].isalpha()==False or selectedPiece[1].isdigit()==False :
            print("The value you have entered is incorrect")
        else:
            correctInputPiece=True


    while correctInputCoord==False :
        selectedCoord = input("Select the square of where you want to move it to : ") #Gets the destination square
        if len(selectedCoord)!=2 :
            print("The value you have entered is incorrect")
        elif selectedCoord[0].isalpha()==False or selectedCoord[1].isdigit()==False :
            print("The value you have entered is incorrect")
        else:
            correctInputCoord=True


    selectedPieceY = ord(selectedPiece[0]) - 65 #Converts the input into coordinates
    selectedPieceX = int(selectedPiece[1]) - 1
    selectedCoordY = ord(selectedCoord[0]) - 65
    selectedCoordX = int(selectedCoord[1]) - 1

    if board.currentPlayerIsOne == False:
        board.currentPlayerIsOne = True
    else:
        board.currentPlayerIsOne = False

    print("\033[H\033[J") #Clears the board
