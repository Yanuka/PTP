class Board(object) :
    coordinates = []
    currentPlayerIsOne = False
    def __init__(self):
        self.clear()

    def clear(self): #Creates or resets the board
        self.displayBoard = []
        for i in range(0,8):
            self.displayBoard += [[]]
            for j in range(0,8):
                self.displayBoard[i] += [' ']

    def draw(self): #Draws the board
        if self.currentPlayerIsOne == True:
            print('Player ' + '\33[91m' + '1' + '\x1b[0m' + '\'s turn')
            print()
        else:
            print('Player ' + '\33[94m' + '2' + '\x1b[0m' + '\'s turn')
            print()
        print("        A     B     C     D     E     F     G     H")
        coordName = 1
        for i in self.displayBoard:
            count=0
            print("     —————————————————————————————————————————————————")
            for j in i:
                count+=1
                if count == 1:
                    print(" ", coordName, " ", end='')
                    coordName+=1
                print("| " , j , " ", end='')
                if count == 8:
                    print("|")
        print("     —————————————————————————————————————————————————")


    def fetch(self):#Updates the display board relative to the coordinates table
        self.clear()
        for piece in self.coordinates :
            self.displayBoard[piece[1][0]][piece[1][1]] = piece[0].displayCharacter

    def update(self):
        print("\033[H\033[J") #Clears the board
        self.fetch()
        self.draw() #Updates the current board display

    def getPlayerColor(self, selectedPieceX, selectedPieceY, playerColor):
        for piece in self.coordinates:
            if piece[1][0]==selectedPieceX and piece[1][1]==selectedPieceY and piece[0].color == playerColor:
                return True

    def isSquareEmpty(self, selectedPieceX, selectedPieceY):
        isSquareOccupied = False
        for piece in self.coordinates:
            if piece[1][0] == selectedPieceX and piece[1][1] == selectedPieceY:
                isSquareOccupied = True
        if isSquareOccupied == True:
            return False
        else :
            return True

    def isMoveListEmpty(self, selectedPieceX, selectedPieceY, boardName):
        for piece in self.coordinates:
            if piece[1][0] == selectedPieceX and piece[1][1] == selectedPieceY:
                if piece[0].moveList(selectedPieceX, selectedPieceY, boardName) == []:
                    return True

class Piece(object) :
    hasMoved = False

    def movePiece(self,actualCoordX,actualCoordY,destinationCoordX,destinationCoordY,boardName):
        for piece in boardName.coordinates:
            if piece[1][0]==actualCoordX and piece[1][1]==actualCoordY:
                piece[1][0] = destinationCoordX
                piece[1][1] = destinationCoordY


class Pawn(Piece) :
    def __init__(self, color):
        self.capturePossible = []
        self.availableMoves = []
        self.color = color
        if self.color == "White":
            self.displayCharacter = '\33[91m' + 'P' + '\x1b[0m'
        elif self.color == "Black":
            self.displayCharacter = '\33[94m' + 'P' + '\x1b[0m'

    def moveList(self, actualCoordX, actualCoordY, boardName):
        noPieceDetected = True
        self.availableMoves = []
        self.capturePossible = []

        if self.color == "White":
            for piece in boardName.coordinates:
                if piece[1][0] == actualCoordX + 1 and piece[1][1] == actualCoordY:
                    noPieceDetected = False

            if noPieceDetected == True:
                self.availableMoves += [[actualCoordX + 1, actualCoordY]]
                for piece in boardName.coordinates:
                    if piece[1][0] == actualCoordX + 2 and piece[1][1] == actualCoordY:
                        noPieceDetected = False

                if noPieceDetected == True and self.hasMoved == False:
                    self.availableMoves += [[actualCoordX + 2, actualCoordY]]

            for piece in boardName.coordinates:
                if piece[1][0] == actualCoordX + 1 and piece[1][1] == actualCoordY + 1:
                    self.availableMoves += [[actualCoordX + 1, actualCoordY + 1]]
                    self.capturePossible += [[actualCoordX + 1, actualCoordY + 1]]
                elif piece[1][0] == actualCoordX + 1 and piece[1][1] == actualCoordY - 1:
                    self.availableMoves += [[actualCoordX + 1, actualCoordY - 1]]
                    self.capturePossible += [[actualCoordX + 1, actualCoordY - 1]]

        elif self.color == "Black":
            for piece in boardName.coordinates:
                if piece[1][0] == actualCoordX - 1 and piece[1][1] == actualCoordY:
                    noPieceDetected = False

            if noPieceDetected == True:
                self.availableMoves += [[actualCoordX - 1, actualCoordY]]
                for piece in boardName.coordinates:
                    if piece[1][0] == actualCoordX - 2 and piece[1][1] == actualCoordY:
                        noPieceDetected = False

                if noPieceDetected == True and self.hasMoved == False:
                    self.availableMoves += [[actualCoordX - 2, actualCoordY]]

                for piece in boardName.coordinates:
                    if piece[1][0] == actualCoordX - 1 and piece[1][1] == actualCoordY + 1:
                        self.availableMoves += [[actualCoordX - 1, actualCoordY + 1]]
                        self.capturePossible += [[actualCoordX - 1, actualCoordY + 1]]
                    elif piece[1][0] == actualCoordX - 1 and piece[1][1] == actualCoordY - 1:
                        self.availableMoves += [[actualCoordX - 1, actualCoordY - 1]]
                        self.capturePossible += [[actualCoordX - 1, actualCoordY - 1]]

        #MANQUE LA TRANSFO EN BOUT DE LIGNE
        return self.availableMoves

class King(Piece) :
    def __init__(self,color):
        self.color=color
        if self.color == "White":
            self.displayCharacter = '\33[91m' + 'K' + '\x1b[0m'
        elif self.color == "Black":
            self.displayCharacter = '\33[94m' + 'K' + '\x1b[0m'
        self.capturePossible = []

    def moveList(self, actualCoordX, actualCoordY, boardName):
        self.availableMoves = [[actualCoordX + 1, actualCoordY], [actualCoordX + 1, actualCoordY + 1],[actualCoordX + 1, actualCoordY - 1], [actualCoordX - 1, actualCoordY],[actualCoordX - 1, actualCoordY + 1], [actualCoordX - 1, actualCoordY - 1],[actualCoordX, actualCoordY + 1], [actualCoordX, actualCoordY - 1]]

        for piece in boardName.coordinates:
            if piece[1][0] == actualCoordX + 1 and piece[1][1] == actualCoordY:
                if piece[0].color == self.color:
                    self.availableMoves.remove([actualCoordX + 1, actualCoordY])
                elif piece[0].color != self.color:
                    self.capturePossible += [[actualCoordX + 1, actualCoordY]]

            if piece[1][0] == actualCoordX + 1 and piece[1][1] == actualCoordY + 1:
                if piece[0].color == self.color:
                    self.availableMoves.remove([actualCoordX + 1, actualCoordY + 1])
                elif piece[0].color != self.color:
                    self.capturePossible += [[actualCoordX + 1, actualCoordY + 1]]

            if piece[1][0] == actualCoordX + 1 and piece[1][1] == actualCoordY - 1:
                if piece[0].color == self.color:
                    self.availableMoves.remove([actualCoordX + 1, actualCoordY - 1])
                elif piece[0].color != self.color:
                    self.capturePossible += [[actualCoordX + 1, actualCoordY - 1]]

            if piece[1][0] == actualCoordX - 1 and piece[1][1] == actualCoordY:
                if piece[0].color == self.color:
                    self.availableMoves.remove([actualCoordX - 1, actualCoordY])
                elif piece[0].color != self.color:
                    self.capturePossible += [[actualCoordX - 1, actualCoordY]]

            if piece[1][0] == actualCoordX - 1 and piece[1][1] == actualCoordY + 1:
                if piece[0].color == self.color:
                    self.availableMoves.remove([actualCoordX - 1, actualCoordY + 1])
                elif piece[0].color != self.color:
                    self.capturePossible += [[actualCoordX - 1, actualCoordY + 1]]

            if piece[1][0] == actualCoordX - 1 and piece[1][1] == actualCoordY - 1:
                if piece[0].color == self.color:
                    self.availableMoves.remove([actualCoordX - 1, actualCoordY - 1])
                elif piece[0].color != self.color:
                    self.capturePossible += [[actualCoordX - 1, actualCoordY - 1]]

            if piece[1][0] == actualCoordX and piece[1][1] == actualCoordY + 1:
                if piece[0].color == self.color:
                    self.availableMoves.remove([actualCoordX, actualCoordY + 1])
                elif piece[0].color != self.color:
                    self.capturePossible += [[actualCoordX, actualCoordY + 1]]

            if piece[1][0] == actualCoordX and piece[1][1] == actualCoordY - 1:
                if piece[0].color == self.color:
                    self.availableMoves.remove([actualCoordX, actualCoordY - 1])
                elif piece[0].color != self.color:
                    self.capturePossible += [[actualCoordX, actualCoordY - 1]]

        for i in range(len(self.availableMoves) - 1,-1,-1):
            if self.availableMoves[i][0] not in range(0,8) or self.availableMoves[i][1] not in range(0,8):
                self.availableMoves.remove(self.availableMoves[i])
        #MANQUE LE ROCK
        return self.availableMoves


class Queen(Piece) :
    def __init__(self,color):
        self.capturePossible = []
        self.availableMoves = []
        self.color=color
        if self.color == "White":
            self.displayCharacter = '\33[91m' + 'Q' + '\x1b[0m'
        elif self.color == "Black":
            self.displayCharacter = '\33[94m' + 'Q' + '\x1b[0m'

    def moveList(self, actualCoordX, actualCoordY, boardName):
        limit = [0,0,0,0]
        limit2 = [7,7,7,7]
        limitCondtion = [False, False, False, False]
        self.availableMoves = []
        self.capturePossible = []

        for i in range(0, 7):
            if actualCoordX + i >= 7 or actualCoordY + i >= 7:
                if limitCondtion[0] == False:
                    limit[0] = i
                    limitCondtion[0] = True
            if actualCoordX - i <= 0 or actualCoordY + i >= 7:
                if limitCondtion[1] == False:
                    limit[1] = i
                    limitCondtion[1] = True
            if actualCoordX - i <= 0 or actualCoordY - i <= 0:
                if limitCondtion[2] == False:
                    limit[2] = i
                    limitCondtion[2] = True
            if actualCoordX + i >= 7 or actualCoordY - i <= 0:
                if limitCondtion[3] == False:
                    limit[3] = i
                    limitCondtion[3] = True

        for i in range(1, 7):
            for piece in boardName.coordinates:
                if piece[1][0] == actualCoordX + i and piece[1][1] == actualCoordY + i:
                    if limit2[0] == 7:
                        if self.color == piece[0].color:
                            limit2[0] = i - 1
                        else:
                            limit2[0] = i
                            self.capturePossible += [[piece[1][0], piece[1][1]]]
                if piece[1][0] == actualCoordX - i and piece[1][1] == actualCoordY + i:
                    if limit2[1] == 7:
                        if self.color == piece[0].color:
                            limit2[1] = i - 1
                        else:
                            limit2[1] = i
                            self.capturePossible += [[piece[1][0], piece[1][1]]]
                if piece[1][0] == actualCoordX - i and piece[1][1] == actualCoordY - i:
                    if limit2[2] == 7:
                        if self.color == piece[0].color:
                            limit2[2] = i - 1
                        else:
                            limit2[2] = i
                            self.capturePossible += [[piece[1][0], piece[1][1]]]
                if piece[1][0] == actualCoordX + i and piece[1][1] == actualCoordY - i:
                    if limit2[3] == 7:
                        if self.color == piece[0].color:
                            limit2[3] = i - 1
                        else:
                            limit2[3] = i
                            self.capturePossible += [[piece[1][0], piece[1][1]]]

        for i in range(4):
            if limit2[i] < limit[i]:
                limit[i] = limit2[i]

        if limit[0] != 0:
            for j in range(1, limit[0]+1):
                self.availableMoves += [[actualCoordX + j, actualCoordY + j]]
        if limit[1] != 0:
            for j in range(1, limit[1]+1):
                self.availableMoves += [[actualCoordX - j, actualCoordY + j]]
        if limit[2] != 0:
            for j in range(1, limit[2]+1):
                self.availableMoves += [[actualCoordX - j, actualCoordY - j]]
        if limit[3] != 0:
            for j in range(1, limit[3]+1):
                self.availableMoves += [[actualCoordX + j, actualCoordY - j]]

        limit = [0,0,0,0]
        limit2 = [7,7,7,7]
        limitCondtion = [False, False, False, False]

        for i in range(0, 8):
            if actualCoordX + i >= 7:
                if limitCondtion[0] == False:
                    limit[0] = i
                    limitCondtion[0] = True
            if actualCoordY + i >= 7:
                if limitCondtion[1] == False:
                    limit[1] = i
                    limitCondtion[1] = True
            if actualCoordX - i <= 0:
                if limitCondtion[2] == False:
                    limit[2] = i
                    limitCondtion[2] = True
            if actualCoordY - i <= 0:
                if limitCondtion[3] == False:
                    limit[3] = i
                    limitCondtion[3] = True


        for i in range(1, 7):
            for piece in boardName.coordinates:
                if piece[1][0] == actualCoordX + i and piece[1][1] == actualCoordY:
                    if limit2[0] == 7:
                        if self.color == piece[0].color:
                            limit2[0] = i - 1
                        else:
                            limit2[0] = i
                            self.capturePossible += [[piece[1][0], piece[1][1]]]
                if piece[1][0] == actualCoordX and piece[1][1] == actualCoordY + i:
                    if limit2[1] == 7:
                        if self.color == piece[0].color:
                            limit2[1] = i - 1
                        else:
                            limit2[1] = i
                            self.capturePossible += [[piece[1][0], piece[1][1]]]
                if piece[1][0] == actualCoordX - i and piece[1][1] == actualCoordY:
                    if limit2[2] == 7:
                        if self.color == piece[0].color:
                            limit2[2] = i - 1
                        else:
                            limit2[2] = i
                            self.capturePossible += [[piece[1][0], piece[1][1]]]
                if piece[1][0] == actualCoordX and piece[1][1] == actualCoordY - i:
                    if limit2[3] == 7:
                        if self.color == piece[0].color:
                            limit2[3] = i - 1
                        else:
                            limit2[3] = i
                            self.capturePossible += [[piece[1][0], piece[1][1]]]

        for i in range(4):
            if limit2[i] < limit[i]:
                limit[i] = limit2[i]

        if limit[0] != 0:
            for j in range(1, limit[0]+1):
                self.availableMoves += [[actualCoordX + j, actualCoordY]]
        if limit[1] != 0:
            for j in range(1, limit[1]+1):
                self.availableMoves += [[actualCoordX, actualCoordY + j]]
        if limit[2] != 0:
            for j in range(1, limit[2]+1):
                self.availableMoves += [[actualCoordX - j, actualCoordY]]
        if limit[3] != 0:
            for j in range(1, limit[3]+1):
                self.availableMoves += [[actualCoordX, actualCoordY - j]]

        return self.availableMoves


class Bishop(Piece) :
    def __init__(self,color):
        self.capturePossible = []
        self.availableMoves = []
        self.color=color
        if self.color == "White":
            self.displayCharacter = '\33[91m' + 'B' + '\x1b[0m'
        elif self.color == "Black":
            self.displayCharacter = '\33[94m' + 'B' + '\x1b[0m'

    def moveList(self, actualCoordX, actualCoordY, boardName):
        limit = [0,0,0,0]
        limit2 = [7,7,7,7]
        limitCondtion = [False, False, False, False]
        self.availableMoves = []
        self.capturePossible = []

        for i in range(0, 7):
            if actualCoordX + i >= 7 or actualCoordY + i >= 7:
                if limitCondtion[0] == False:
                    limit[0] = i
                    limitCondtion[0] = True
            if actualCoordX - i <= 0 or actualCoordY + i >= 7:
                if limitCondtion[1] == False:
                    limit[1] = i
                    limitCondtion[1] = True
            if actualCoordX - i <= 0 or actualCoordY - i <= 0:
                if limitCondtion[2] == False:
                    limit[2] = i
                    limitCondtion[2] = True
            if actualCoordX + i >= 7 or actualCoordY - i <= 0:
                if limitCondtion[3] == False:
                    limit[3] = i
                    limitCondtion[3] = True

        for i in range(1, 7):
            for piece in boardName.coordinates:
                if piece[1][0] == actualCoordX + i and piece[1][1] == actualCoordY + i:
                    if limit2[0] == 7:
                        if self.color == piece[0].color:
                            limit2[0] = i - 1
                        else:
                            limit2[0] = i
                            self.capturePossible += [[piece[1][0], piece[1][1]]]
                if piece[1][0] == actualCoordX - i and piece[1][1] == actualCoordY + i:
                    if limit2[1] == 7:
                        if self.color == piece[0].color:
                            limit2[1] = i - 1
                        else:
                            limit2[1] = i
                            self.capturePossible += [[piece[1][0], piece[1][1]]]
                if piece[1][0] == actualCoordX - i and piece[1][1] == actualCoordY - i:
                    if limit2[2] == 7:
                        if self.color == piece[0].color:
                            limit2[2] = i - 1
                        else:
                            limit2[2] = i
                            self.capturePossible += [[piece[1][0], piece[1][1]]]
                if piece[1][0] == actualCoordX + i and piece[1][1] == actualCoordY - i:
                    if limit2[3] == 7:
                        if self.color == piece[0].color:
                            limit2[3] = i - 1
                        else:
                            limit2[3] = i
                            self.capturePossible += [[piece[1][0], piece[1][1]]]

        for i in range(4):
            if limit2[i] < limit[i]:
                limit[i] = limit2[i]

        if limit[0] != 0:
            for j in range(1, limit[0]+1):
                self.availableMoves += [[actualCoordX + j, actualCoordY + j]]
        if limit[1] != 0:
            for j in range(1, limit[1]+1):
                self.availableMoves += [[actualCoordX - j, actualCoordY + j]]
        if limit[2] != 0:
            for j in range(1, limit[2]+1):
                self.availableMoves += [[actualCoordX - j, actualCoordY - j]]
        if limit[3] != 0:
            for j in range(1, limit[3]+1):
                self.availableMoves += [[actualCoordX + j, actualCoordY - j]]

        return self.availableMoves



class Knight(Piece) :
    def __init__(self,color):
        self.color=color
        self.capturePossible = []
        if self.color == "White":
            self.displayCharacter = '\33[91m' + 'N' + '\x1b[0m'
        elif self.color == "Black":
            self.displayCharacter = '\33[94m' + 'N' + '\x1b[0m'
    def moveList(self, actualCoordX, actualCoordY, boardName):
        isEmpty = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
        self.availableMoves= []
        self.capturePossible=[]
        for square in isEmpty:
            mateFound = False
            for piece in boardName.coordinates:
                if piece[1][0] == (actualCoordX+square[0]) and piece[1][1] == (actualCoordY+square[1]):
                    if self.color != piece[0].color:
                        self.availableMoves += [[piece[1][0],piece[1][1]]]
                        self.capturePossible += [[piece[1][0],piece[1][1]]]
                    else:
                        mateFound = True
                        if [(actualCoordX+square[0]),(actualCoordY+square[1])] in self.availableMoves:
                            self.availableMoves.remove([(actualCoordX+square[0]),(actualCoordY+square[1])])
                elif [actualCoordX+square[0],(actualCoordY+square[1])] not in self.availableMoves and mateFound == False :
                    self.availableMoves += [[actualCoordX+square[0],(actualCoordY+square[1])]]

        for i in range(len(self.availableMoves) - 1,-1,-1):
            if self.availableMoves[i][0] not in range(0,8) or self.availableMoves[i][1] not in range(0,8):
                self.availableMoves.remove(self.availableMoves[i])
        return self.availableMoves



class Rook(Piece) :
    def __init__(self,color):
        self.capturePossible = []
        self.availableMoves = []
        self.color=color
        if self.color == "White":
            self.displayCharacter = '\33[91m' + 'R' + '\x1b[0m'
        elif self.color == "Black":
            self.displayCharacter = '\33[94m' + 'R' + '\x1b[0m'

    def moveList(self, actualCoordX, actualCoordY, boardName):
        limit = [0,0,0,0]
        limit2 = [7,7,7,7]
        limitCondtion = [False, False, False, False]
        self.availableMoves = []
        self.capturePossible = []

        for i in range(0, 8):
            if actualCoordX + i >= 7:
                if limitCondtion[0] == False:
                    limit[0] = i
                    limitCondtion[0] = True
            if actualCoordY + i >= 7:
                if limitCondtion[1] == False:
                    limit[1] = i
                    limitCondtion[1] = True
            if actualCoordX - i <= 0:
                if limitCondtion[2] == False:
                    limit[2] = i
                    limitCondtion[2] = True
            if actualCoordY - i <= 0:
                if limitCondtion[3] == False:
                    limit[3] = i
                    limitCondtion[3] = True


        for i in range(1, 7):
            for piece in boardName.coordinates:
                if piece[1][0] == actualCoordX + i and piece[1][1] == actualCoordY:
                    if limit2[0] == 7:
                        if self.color == piece[0].color:
                            limit2[0] = i - 1
                        else:
                            limit2[0] = i
                            self.capturePossible += [[piece[1][0], piece[1][1]]]
                if piece[1][0] == actualCoordX and piece[1][1] == actualCoordY + i:
                    if limit2[1] == 7:
                        if self.color == piece[0].color:
                            limit2[1] = i - 1
                        else:
                            limit2[1] = i
                            self.capturePossible += [[piece[1][0], piece[1][1]]]
                if piece[1][0] == actualCoordX - i and piece[1][1] == actualCoordY:
                    if limit2[2] == 7:
                        if self.color == piece[0].color:
                            limit2[2] = i - 1
                        else:
                            limit2[2] = i
                            self.capturePossible += [[piece[1][0], piece[1][1]]]
                if piece[1][0] == actualCoordX and piece[1][1] == actualCoordY - i:
                    if limit2[3] == 7:
                        if self.color == piece[0].color:
                            limit2[3] = i - 1
                        else:
                            limit2[3] = i
                            self.capturePossible += [[piece[1][0], piece[1][1]]]

        for i in range(4):
            if limit2[i] < limit[i]:
                limit[i] = limit2[i]

        if limit[0] != 0:
            for j in range(1, limit[0]+1):
                self.availableMoves += [[actualCoordX + j, actualCoordY]]
        if limit[1] != 0:
            for j in range(1, limit[1]+1):
                self.availableMoves += [[actualCoordX, actualCoordY + j]]
        if limit[2] != 0:
            for j in range(1, limit[2]+1):
                self.availableMoves += [[actualCoordX - j, actualCoordY]]
        if limit[3] != 0:
            for j in range(1, limit[3]+1):
                self.availableMoves += [[actualCoordX, actualCoordY - j]]

        return self.availableMoves


class supervisor() :

    def capturePiece(self, destinationCoordX, destinationCoordY, boardName):
        for piece in boardName.coordinates : #Moves the selected piece
            if piece[1][0]==destinationCoordX and piece[1][1]==destinationCoordY:
                boardName.coordinates.remove(piece)
                boardName.fetch()
