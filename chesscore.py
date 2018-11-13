class Board(object) :
    coordinates = []

    def __init__(self): #Creates the board
        self.currentBoard = []
        for i in range(0,8):
            self.currentBoard += [[]]
            for j in range(0,8):
                self.currentBoard[i] += [' ']

    def draw(self): #Draws the board
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
        for piece in self.coordinates :
            self.currentBoard[piece[1][0]][piece[1][1]] = piece[0].dispayCharacter

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
board.coordinates+=[[whitePawn1,(1,0)],[whitePawn2,(1,1)],[whitePawn3,(1,2)],[whitePawn4,(1,3)],[whitePawn5,(1,4)],[whitePawn6,(1,5)],[whitePawn7,(1,6)],[whitePawn8,(1,7)],[whiteKing,(0,4)],[whiteQueen,(0,3)],[whiteBishop1,(0,2)],[whiteBishop2,(0,5)],[whiteKnight1,(0,1)],[whiteKnight2,(0,6)],[whiteRook1,(0,0)],[whiteRook2,(0,7)],[blackPawn1,(6,0)],[blackPawn2,(6,1)],[blackPawn3,(6,2)],[blackPawn4,(6,3)],[blackPawn5,(6,4)],[blackPawn6,(6,5)],[blackPawn7,(6,6)],[blackPawn8,(6,7)],[blackKing,(7,4)],[blackQueen,(7,3)],[blackBishop1,(7,2)],[blackBishop2,(7,5)],[blackKnight1,(7,1)],[blackKnight2,(7,6)],[blackRook1,(7,0)],[blackRook2,(7,7)]]
board.fetch()
