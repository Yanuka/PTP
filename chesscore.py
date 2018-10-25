class Board(object) :

    def __init__(self):
        self.currentBoard = []
        for i in range(0,8):
            self.currentBoard += [[]]
            for j in range(0,8):
                self.currentBoard[i] += [(i,j)]

    def draw(self):
        for i in range(len(self.currentBoard)):
            count=0
            print("————————————————————————————————————————————————")
            a = self.currentBoard[len(self.currentBoard)-i-1]
            for j in a:
                count+=1
                print("| " , j , " ", end='')
                if count == 8:
                    print("|")
        print("————————————————————————————————————————————————")
        return (0)

        def update(self,selectedPieceX,selectedPieceY,selectedCoordX,selectedCoordY,pieceName) :
            self.currentBoard[selectedPieceX][selectedPieceY] = ' '
            self.currentBoard[selectedCoordX][selectedCoordY] = pieceName

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
