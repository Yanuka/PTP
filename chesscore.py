class Board(object) :

	actualBoard = []

	def initialize(self):
		"""
        Function that returns an 8 by 8 table filled with dummy values
        We replace these dummy values with the pieces' coordinates when the piece is moved
        """
        board =[]
        for i in range(0,8):
            board += [[]]
            for j in range(0,8):
                board[i] += [0]
        return(board)

    def draw(self,board):
        for i in board:
            count=0
            print("————————————————————————————————————————————————")
            for j in i:
                count+=1
                print("| " , j , " ", end='')
                if count == 8:
                    print("|")
        print("————————————————————————————————————————————————")
        return (0)

	def __init__(self):
    	actualBoard = initialize()



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

board= Board()