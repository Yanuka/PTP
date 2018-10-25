class Board(object) :

    def __init__(self):
        self.currentBoard = []
        for i in range(0,8):
            self.currentBoard += [[]]
            for j in range(0,8):
                self.currentBoard[i] += [' ']

    def draw(self):
        print("        1     2     3     4     5     6     7     8")
        coun = 1
        for i in self.currentBoard:
            count=0
            print("     —————————————————————————————————————————————————")
            for j in i:
                count+=1
                if count == 1:
                    print(" ", coun, " ", end='')
                    coun+=1
                print("| " , j , " ", end='')
                if count == 8:
                    print("|")
        print("     —————————————————————————————————————————————————")
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
