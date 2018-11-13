# @Author: Lucas Bretel
# @Date:   2018-11-13T15:45:48+01:00
# @Email:  lucas.bretel@hotmail.fr
# @Last modified by:   Lucas Bretel
# @Last modified time: 2018-11-13T16:00:52+01:00



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

    pass

class Pawn(Piece) :
    Pawn1 = 'P'
    Pawn2 = 'P'
    pass

class King(Piece) :
    King1 = 'K'
    King2 = 'K'
    pass

class Queen(Piece) :
    Queen1 = 'Q'
    Queen2 = 'Q'
    pass

class Bishop(Piece) :
    Bishop1 = 'B'
    Bishop2 = 'B'
    pass

class Knight(Piece) :
    Knight1 = 'N'
    Knight2 = 'N'
    pass

class Rook(Piece) :
    Rook1 = 'R'
    Rook2 = 'R'
    pass

class supervisor() :

    def __init__(self):
        Board = Board()
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

    pass
