class Board(object) :
    coordinates = []
    currentPlayerIsOne = True
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

    def getPlayerColor(self, selectedPieceX, selectedPieceY, playerColor):
        for piece in self.coordinates:
            if piece[1][0]==selectedPieceX and piece[1][1]==selectedPieceY and piece[0].color == playerColor:
                return True



class Piece(object) :
    def movePiece(self,actualCoordX,actualCoordY,destinationCoordX,destinationCoordY,boardName):
        for piece in boardName.coordinates:
            if piece[1][0]==actualCoordX and piece[1][1]==actualCoordY:
                piece[1][0] = destinationCoordX
                piece[1][1] = destinationCoordY





class Pawn(Piece) :
   def __init__(self,color):
       self.color=color
       if self.color == "White":
           self.displayCharacter = '\33[91m' + 'P' + '\x1b[0m'
       elif self.color == "Black":
           self.displayCharacter = '\33[94m' + 'P' + '\x1b[0m'


class King(Piece) :
    def __init__(self,color):
        self.color=color
        if self.color == "White":
            self.displayCharacter = '\33[91m' + 'K' + '\x1b[0m'
        elif self.color == "Black":
            self.displayCharacter = '\33[94m' + 'K' + '\x1b[0m'


class Queen(Piece) :
    def __init__(self,color):
        self.color=color
        if self.color == "White":
            self.displayCharacter = '\33[91m' + 'Q' + '\x1b[0m'
        elif self.color == "Black":
            self.displayCharacter = '\33[94m' + 'Q' + '\x1b[0m'


class Bishop(Piece) :
    def __init__(self,color):
        self.color=color
        if self.color == "White":
            self.displayCharacter = '\33[91m' + 'B' + '\x1b[0m'
        elif self.color == "Black":
            self.displayCharacter = '\33[94m' + 'B' + '\x1b[0m'


class Knight(Piece) :
    def __init__(self,color):
        self.color=color
        if self.color == "White":
            self.displayCharacter = '\33[91m' + 'N' + '\x1b[0m'
        elif self.color == "Black":
            self.displayCharacter = '\33[94m' + 'N' + '\x1b[0m'


class Rook(Piece) :
    def __init__(self,color):
        self.color=color
        if self.color == "White":
            self.displayCharacter = '\33[91m' + 'R' + '\x1b[0m'
        elif self.color == "Black":
            self.displayCharacter = '\33[94m' + 'R' + '\x1b[0m'


class supervisor() :
    pass
