class supervisor() :
    pass

class Board(object) :

    def __init__(self): #Creates the board
        self.currentBoard = []
        for i in range(0,8):
            self.currentBoard += [[]]
            for j in range(0,8):
                self.currentBoard[i] += [' ']

    def draw(self): #Draws the board
        print("        1     2     3     4     5     6     7     8")
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
        return (0)

    def update(self,selectedPieceX,selectedPieceY,selectedCoordX,selectedCoordY,pieceName) : #Updates the board
        self.currentBoard[selectedPieceX][selectedPieceY] = ' '
        self.currentBoard[selectedCoordX][selectedCoordY] = pieceName

class Piece(object) :
    isBlack = 'bool'
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
