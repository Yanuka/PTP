from chesscore import *

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