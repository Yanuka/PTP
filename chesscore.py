class Board(object) :
    
    def initializeBoard(self):
        """
        Function that returns an 8 by 8 table filled with dummy values
        We replace these dummy values with the pieces' coordinates when the piece is moved
        """
        board = []
        for i in range(0,8):
            board += [[]]
            for j in range(0,8):
                board[i] += [None]
        return(board)



class Piece(object) :
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
