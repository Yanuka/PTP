class Board(object) :

    def __init__(self): #Creates the board
        self.currentBoard = []
        for i in range(0,8):
            self.currentBoard += [[]]
            for j in range(0,8):
                self.currentBoard[i] += [' ']

    def draw(self): #Draws the board
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

    def update(self,selectedPieceX,selectedPieceY,selectedCoordX,selectedCoordY,pieceName) : #Updates the board
        self.currentBoard[selectedPieceX][selectedPieceY] = ' '
        self.currentBoard[selectedCoordX][selectedCoordY] = pieceName

class Piece(object) :
    isBlack = bool
    pass

class Pawn(Piece) :
    Pawn1 = "♙"
    Pawn2 = "♟"
    pass

class King(Piece) :
    King1 = "♔"
    King2 = "♚"
    pass

class Queen(Piece) :
    Queen1 = "♕"
    Queen2 = "♛"
    pass

class Bishop(Piece) :
    Bishop1 = "♗"
    Bishop2 = "♝"
    pass

class Knight(Piece) :
    Knight1 = "♘"
    Knight2 = "♞"
    pass

class Rook(Piece) :
    Rook1 = "♖"
    Rook2 = "♜"
    pass
