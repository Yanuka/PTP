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


class Piece(object) :
    def __init__(self,color):
        self.color=color



class Pawn(Piece) :
   a=1

class King(Piece) :
    King1 = 'K'
    King2 = 'K'


class Queen(Piece) :
    Queen1 = 'Q'
    Queen2 = 'Q'


class Bishop(Piece) :
    Bishop1 = 'B'
    Bishop2 = 'B'


class Knight(Piece) :
    Knight1 = 'N'
    Knight2 = 'N'


class Rook(Piece) :
    Rook1 = 'R'
    Rook2 = 'R'


class supervisor() :

    def __init__(self,boardName):
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
        boardName.coordinates+=[whitePawn1,(2,2)]

    pass
