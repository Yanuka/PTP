class Board(object) :
    coordinates = []
    currentPlayerIsOne = False
    whiteChecked = False
    blackChecked = False

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
            print('Player ' + '\33[1;36;40m' + '2' + '\x1b[0m' + '\'s turn')
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
        if self.whiteChecked ==  True:
            print('\x1b[0m' + '\33[91m' + 'White King' + '\x1b[0m' + ' is in check!')
        if self.blackChecked == True:
            print('\x1b[0m' + '\33[1;36;40m' + 'Black King' + '\x1b[0m' + ' is in check!')

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
    capturePossible = []
    availableMoves = []

    def movePiece(self,actualCoordX,actualCoordY,destinationCoordX,destinationCoordY,boardName):
        for piece in boardName.coordinates:
            if piece[1][0]==actualCoordX and piece[1][1]==actualCoordY:
                piece[1][0] = destinationCoordX
                piece[1][1] = destinationCoordY


class Pawn(Piece) :
    def __init__(self, color):
        self.name = "Pawn"
        self.color = color
        if self.color == "White":
            self.displayCharacter = '\33[91m' + 'P' + '\x1b[0m'
        elif self.color == "Black":
            self.displayCharacter = '\33[1;36;40m' + 'P' + '\x1b[0m'

    def moveList(self, actualCoordX, actualCoordY, boardName):
        noPieceDetected = True
        self.availableMoves = []
        self.capturePossible = []
        if self.color == "Black":
            isEmpty = [[-1,0],[-2,0],[-1,-1],[-1,1]]
            for piece in boardName.coordinates:
                    if piece[1][0] == actualCoordX - 1 and piece[1][1] == actualCoordY:
                        noPieceDetected = False
                    elif piece[1][0] == actualCoordX -1 and piece[1][1] == actualCoordY - 1 and piece[0].color != self.color:
                        self.availableMoves += [[piece[1][0],piece[1][1]]]
                        self.capturePossible += [[piece[1][0],piece[1][1]]]
                    elif piece[1][0] == actualCoordX -1 and piece[1][1] == actualCoordY + 1 and piece[0].color != self.color:
                        self.availableMoves += [[piece[1][0],piece[1][1]]]
                        self.capturePossible += [[piece[1][0],piece[1][1]]]
            if noPieceDetected == True:
                self.availableMoves += [[actualCoordX - 1,actualCoordY]]
                for piece in boardName.coordinates:
                    if piece[1][0] == actualCoordX - 2 and piece[1][1] == actualCoordY:
                        noPieceDetected = False
                if noPieceDetected == True and self.hasMoved == False:
                    self.availableMoves += [[actualCoordX - 2,actualCoordY]]
        else:
            for piece in boardName.coordinates:
                    if piece[1][0] == actualCoordX + 1 and piece[1][1] == actualCoordY:
                        noPieceDetected = False
                    elif piece[1][0] == actualCoordX + 1 and piece[1][1] == actualCoordY - 1 and piece[0].color != self.color:
                        self.availableMoves += [[piece[1][0],piece[1][1]]]
                        self.capturePossible += [[piece[1][0],piece[1][1]]]
                    elif piece[1][0] == actualCoordX + 1 and piece[1][1] == actualCoordY + 1 and piece[0].color != self.color:
                        self.availableMoves += [[piece[1][0],piece[1][1]]]
                        self.capturePossible += [[piece[1][0],piece[1][1]]]
            if noPieceDetected == True:
                self.availableMoves += [[actualCoordX + 1,actualCoordY]]
                for piece in boardName.coordinates:
                    if piece[1][0] == actualCoordX + 2 and piece[1][1] == actualCoordY:
                        noPieceDetected = False
                if noPieceDetected == True and self.hasMoved == False:
                    self.availableMoves += [[actualCoordX + 2,actualCoordY]]



        for i in range(len(self.availableMoves) - 1,-1,-1):
            if self.availableMoves[i][0] not in range(0,8) or self.availableMoves[i][1] not in range(0,8):
                self.availableMoves.remove(self.availableMoves[i])

        return self.availableMoves

class King(Piece) :
    def __init__(self,color):
        self.name = "King"
        self.color=color
        if self.color == "White":
            self.displayCharacter = '\33[91m' + 'K' + '\x1b[0m'
        elif self.color == "Black":
            self.displayCharacter = '\33[1;36;40m' + 'K' + '\x1b[0m'

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
        self.name = "Queen"
        self.color=color
        if self.color == "White":
            self.displayCharacter = '\33[91m' + 'Q' + '\x1b[0m'
        elif self.color == "Black":
            self.displayCharacter = '\33[1;36;40m' + 'Q' + '\x1b[0m'

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
        self.name = "Bishop"
        self.color=color
        if self.color == "White":
            self.displayCharacter = '\33[91m' + 'B' + '\x1b[0m'
        elif self.color == "Black":
            self.displayCharacter = '\33[1;36;40m' + 'B' + '\x1b[0m'

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
        self.name = "Knight"
        self.color=color
        if self.color == "White":
            self.displayCharacter = '\33[91m' + 'N' + '\x1b[0m'
        elif self.color == "Black":
            self.displayCharacter = '\33[1;36;40m' + 'N' + '\x1b[0m'
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
        self.name = "Rook"
        self.color=color
        if self.color == "White":
            self.displayCharacter = '\33[91m' + 'R' + '\x1b[0m'
        elif self.color == "Black":
            self.displayCharacter = '\33[1;36;40m' + 'R' + '\x1b[0m'

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

    def promotion(self, boardName):
        for piece in boardName.coordinates:
            if piece[0].name == "Pawn" and (piece[1][0] == 0 or piece[1][0] == 7):
                promoInput = input("In which piece would you like to be promoted ?\n1-Queen\n2-Knight\n")
                while promoInput not in ["1","2"]:
                    boardName.update()
                    promoInput = input('\33[93m' + '|!| ' + '\x1b[0m' + "Please type a valid number!\nIn which piece would you like to be promoted ?\n1-Queen\n2-Knight\n")
                if promoInput == "1":
                    piece[0] = Queen(piece[0].color)
                    piece[0].hasMoved = True
                elif promoInput == "2":
                    piece[0] = Knight(piece[0].color)
                    piece[0].hasMoved = True

    def isCheck(self, boardName):
        boardName.whiteChecked = False
        boardName.blackChecked = False
        for king in boardName.coordinates:
            if king[0].name == "King" and king[0].color == "White":
                for piece in boardName.coordinates:
                    if piece[0].color == "Black":
                        for pos in piece[0].moveList(piece[1][0], piece[1][1], boardName):
                            if pos == [king[1][0], king[1][1]]:
                                boardName.whiteChecked = True
            elif king[0].name == "King" and king[0].color == "Black":
                for piece in boardName.coordinates:
                    if piece[0].color == "White":
                        for pos in piece[0].moveList(piece[1][0], piece[1][1], boardName):
                            if pos == [king[1][0], king[1][1]]:
                                boardName.blackChecked = True

    def isPat(self, boardName):
        if boardName.whiteChecked == True:
            #do stuff
            pass
        elif boardName.blackChecked == True:
            #do stuff
            pass
