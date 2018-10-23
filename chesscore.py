class Board :

    def initializeBoard(self):
        """
        Function that return a table[8][8] full of None
        When a piece is inside a square, we swap the None at those coordonate with the name of the piece
        """
        board = []
        for i in range(0,8):
            board += [[]]
            for j in range(0,8):
                board[i] += [None]
        return(board)



class Piece :
    pass

class Pawn(Piece) :
    pass

class King(Piece) :
    pass

class Queen(Piece) :
    pass

class Bishop(Piece) :
    pass

class Knight(Piece) :
    pass

class Rook(Piece) :
    pass

board1= Board()
print(board1.initializeBoard())
