class Board(object) :
    coordinates = []
    currentPlayerIsOne = True
    def __init__(self):
        self.clear()

    def clear(self): #Creates the board
        self.currentBoard = []
        for i in range(0,8):
            self.currentBoard += [[]]
            for j in range(0,8):
                self.currentBoard[i] += [' ']

    def draw(self): #Draws the board
        if self.currentPlayerIsOne == True:
            print('Player ' + '\33[91m' + '1' + '\x1b[0m' + '\'s turn')
            print()
        else:
            print('Player ' + '\33[94m' + '2' + '\x1b[0m' + '\'s turn')
            print()
        print("        A     B     C     D     E     F     G     H")
        coordName = 1
        for i in self.currentBoard:
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


    def fetch(self):
        self.clear()
        for piece in self.coordinates :
            self.currentBoard[piece[1][0]][piece[1][1]] = piece[0].dispayCharacter



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
           self.dispayCharacter = '\33[91m' + 'P' + '\x1b[0m'
       elif self.color == "Black":
           self.dispayCharacter = '\33[94m' + 'P' + '\x1b[0m'


class King(Piece) :
    def __init__(self,color):
        self.color=color
        if self.color == "White":
            self.dispayCharacter = '\33[91m' + 'K' + '\x1b[0m'
        elif self.color == "Black":
            self.dispayCharacter = '\33[94m' + 'K' + '\x1b[0m'


class Queen(Piece) :
    def __init__(self,color):
        self.color=color
        if self.color == "White":
            self.dispayCharacter = '\33[91m' + 'Q' + '\x1b[0m'
        elif self.color == "Black":
            self.dispayCharacter = '\33[94m' + 'Q' + '\x1b[0m'


class Bishop(Piece) :
    def __init__(self,color):
        self.color=color
        if self.color == "White":
            self.dispayCharacter = '\33[91m' + 'B' + '\x1b[0m'
        elif self.color == "Black":
            self.dispayCharacter = '\33[94m' + 'B' + '\x1b[0m'


class Knight(Piece) :
    def __init__(self,color):
        self.color=color
        if self.color == "White":
            self.dispayCharacter = '\33[91m' + 'N' + '\x1b[0m'
        elif self.color == "Black":
            self.dispayCharacter = '\33[94m' + 'N' + '\x1b[0m'


class Rook(Piece) :
    def __init__(self,color):
        self.color=color
        if self.color == "White":
            self.dispayCharacter = '\33[91m' + 'R' + '\x1b[0m'
        elif self.color == "Black":
            self.dispayCharacter = '\33[94m' + 'R' + '\x1b[0m'


class supervisor() :
    pass
