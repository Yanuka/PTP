class Board :

    def initializeBoard(self):
        """
        Function that return a table[8][8] full of 0
        When a piece is inside a square, the 0 is swapped by the ID 
        """
        board = []
        for i in range(0,8):
            board += [[]]
            for j in range(0,8):
                board[i] += [0]
        print(board)



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
board1.initializeBoard()
