class Board(object) :
    coordinates = []

    def __init__(self): #Creates the board
        self.currentBoard = []
        for i in range(0,8):
            self.currentBoard += [[]]
            for j in range(0,8):
                self.currentBoard[i] += [' ']

    def draw(self): #Draws the board
        print("        A     B     C     D     E     F     G     F")
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


class Piece(object) :
    a=1




class Pawn(Piece) :
   def __init__(self,color):
       self.color=color
       if self.color == "White":
           self.dispayCharacter = '\33[31m' + 'P' + '\x1b[0m'
       elif self.color == "Black":
           self.dispayCharacter = '\33[34m' + 'P' + '\x1b[0m'


class King(Piece) :
    def __init__(self,color):
        self.color=color
        if self.color == "White":
            self.dispayCharacter = '\33[31m' + 'K' + '\x1b[0m'
        elif self.color == "Black":
            self.dispayCharacter = '\33[34m' + 'K' + '\x1b[0m'


class Queen(Piece) :
    def __init__(self,color):
        self.color=color
        if self.color == "White":
            self.dispayCharacter = '\33[31m' + 'Q' + '\x1b[0m'
        elif self.color == "Black":
            self.dispayCharacter = '\33[34m' + 'Q' + '\x1b[0m'


class Bishop(Piece) :
    def __init__(self,color):
        self.color=color
        if self.color == "White":
            self.dispayCharacter = '\33[31m' + 'B' + '\x1b[0m'
        elif self.color == "Black":
            self.dispayCharacter = '\33[34m' + 'B' + '\x1b[0m'


class Knight(Piece) :
    def __init__(self,color):
        self.color=color
        if self.color == "White":
            self.dispayCharacter = '\33[31m' + 'N' + '\x1b[0m'
        elif self.color == "Black":
            self.dispayCharacter = '\33[34m' + 'N' + '\x1b[0m'


class Rook(Piece) :
    def __init__(self,color):
        self.color=color
        if self.color == "White":
            self.dispayCharacter = '\33[31m' + 'R' + '\x1b[0m'
        elif self.color == "Black":
            self.dispayCharacter = '\33[34m' + 'R' + '\x1b[0m'


class supervisor() :
    pass

board = Board()
whitePawn1 = Pawn("White")
whitePawn2 = Pawn("White")
whitePawn3 = Pawn("White")
whitePawn4 = Pawn("White")
whitePawn5 = Pawn("White")
whitePawn6 = Pawn("White")
whitePawn7 = Pawn("White")
whitePawn8 = Pawn("White")
whiteKing = King("White")
whiteQueen = Queen("White")
whiteBishop1 = Bishop("White")
whiteBishop2 = Bishop("White")
whiteKnight1 = Knight("White")
whiteKnight2 = Knight("White")
whiteRook1 = Rook("White")
whiteRook2 = Rook("White")
blackPawn1 = Pawn("Black")
blackPawn2 = Pawn("Black")
blackPawn3 = Pawn("Black")
blackPawn4 = Pawn("Black")
blackPawn5 = Pawn("Black")
blackPawn6 = Pawn("Black")
blackPawn7 = Pawn("Black")
blackPawn8 = Pawn("Black")
blackKing = King("Black")
blackQueen = Queen("Black")
blackBishop1 = Bishop("Black")
blackBishop2 = Bishop("Black")
blackKnight1 = Knight("Black")
blackKnight2 = Knight("Black")
blackRook1 = Rook("Black")
blackRook2 = Rook("Black")
board.coordinates+=[[whitePawn1,(0,1)],[whitePawn2,(1,1)],[whitePawn3,(2,1)],[whitePawn4,(3,1)],[whitePawn5,(4,1)],[whitePawn6,(5,1)],[whitePawn7,(6,1)],[whitePawn8,(7,1)],[whiteKing,(4,0)],[whiteQueen,(3,0)],[whiteBishop1,(2,0)],[whiteBishop2,(5,0)],[whiteKnight1,(1,0)],[whiteKnight2,(6,0)],[whiteRook1,(0,0)],[whiteRook2,(7,0)],[blackPawn1,(0,6)],[blackPawn2,(1,6)],[blackPawn3,(2,6)],[blackPawn4,(3,6)],[blackPawn5,(4,6)],[blackPawn6,(5,6)],[blackPawn7,(6,6)],[blackPawn8,(7,6)],[blackKing,(4,7)],[blackQueen,(3,7)],[blackBishop1,(2,7)],[blackBishop2,(5,7)],[blackKnight1,(1,7)],[blackKnight2,(6,7)],[blackRook1,(0,7)],[blackRook2,(7,7)]]
