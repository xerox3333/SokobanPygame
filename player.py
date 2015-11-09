class Player:
    def __init__(self, row, col, char):
        self.row = row
        self.col = col
        self.char = char
        self.numMoves = 0
        self.cratesMoved = 0

    def moveUp(self):
        self.row -= 1

    def moveDown(self):
        self.row += 1

    def moveLeft(self):
        self.col -= 1

    def moveRight(self):
        self.col += 1

    def getCol(self):
        return self.col

    def getRow(self):
        return self.row

    def getChar(self):
        return self.char

    def setCol(self, newChar):
        self.char = newChar

    def setRow(self, newRow):
        self.row = newRow

    def setChar(self, newChar):
        self.char = newChar

    def incrementMoves(self):
        self.numMoves += 1

    def decrementMoves(self):
        self.numMoves -= 1

    def getScore(self):
        return self.numMoves

    def crateInPosition(self):
        self.cratesMoved += 1

    def toString(self):
        info = "Player (" + self.char + ") is at row:" + str(self.row) + " col:" + str(self.col) + " and has moved "
        info += str(self.cratesMoved) + " crates into position"
        return info


