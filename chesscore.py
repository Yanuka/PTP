class Board(object) :

    def initialize(self):
        """
        Function that returns an 8 by 8 table filled with dummy values
        We replace these dummy values with the pieces' coordinates when the piece is moved
        print("————————————————————————————————————————————————")
        print("|  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |")
        print("————————————————————————————————————————————————")
        print("|  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |")
        print("————————————————————————————————————————————————")
        print("|  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |")
        print("————————————————————————————————————————————————")
        print("|  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |")
        print("————————————————————————————————————————————————")
        print("|  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |")
        print("————————————————————————————————————————————————")
        print("|  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |")
        print("————————————————————————————————————————————————")
        print("|  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |")
        print("————————————————————————————————————————————————")
        print("|  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |")
        print("————————————————————————————————————————————————")
        test
        """
        board =[]
        for i in range(0,8):
            board += [[]]
            for j in range(0,8):
                board[i] += [0]
        return(board)

    def draw(self,board):
        count=0
        for i in board:
            print("")
            print("————————————————————————————————————————————————")
            for j in i:
                print("| " , j , " ", end='')
        print()
        return (0)



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


board = Board()
actualBoard = board.initialize()
board.draw(actualBoard)

print("Hello and welcome to Chess !")
board.draw()
