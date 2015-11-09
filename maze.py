import random

class Maze:

    def __init__(self):
        self.maze = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                     ['#', 'E', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', '#', ' ', 'C', ' ', ' ', '#', 'E', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', ' ', ' ', ' ', ' ', 'C', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', 'E', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', '#'],
                     ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
        self.placedCrates = 0
        self.width = 16
        self.height = 10

    def Level2State(self):
        self.maze = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                     ['#', 'E', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', '#', ' ', 'C', ' ', ' ', '#', 'E', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', ' ', ' ', ' ', ' ', 'C', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', 'E', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', '#'],
                     ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
        self.placedCrates = 0
        self.width = 12
        self.height = 10

    def Level3State(self):
        self.maze = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                     ['#', 'E', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', '#', ' ', 'C', ' ', ' ', '#', 'E', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', ' ', ' ', ' ', ' ', 'C', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', 'E', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', '#'],
                     ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
        self.placedCrates = 0
        self.width = 12
        self.height = 10

    def placePlayer(self, char, row, col):
        """ Places the player at the specified row and col represented by char
         (char, int, int) -> none
         placePlayer("*", 5, 5)
         NoneType"""
        self.maze[row][col] = char

    def placeCrate(self, row, col):
        self.maze[row][col] = "C"

    def setCharAtPos(self, row, col, newChar):
        self.maze[row][col] = newChar

    def clearAtPos(self, row, col):
        """ Sets the postion to an empty space at specified row and col
        (int, int) -> none
         clearAtPos(3, 6)"""
        self.maze[row][col] = " "

    def getCharAtPos(self, row, col):
        """ Gets the character at specified row and col
         (int, int)
         getCharAtPos(0, 7)
         '#' """
        return self.maze[row][col]

    def placeCrate(self):
        self.placedCrates += 1

    def isLevelFinished(self):
        finished = True
        for i in range(0, len(self.maze)):
            for j in self.maze[i]:
                if j == "C":
                    finished = False
        return finished


    def getWidth(self):
        return self.width


    def getHeight(self):
        return self.height

    def getRandX(self):
        rand = random.randint(1, 14)
        return rand

    def getRandY(self):
        rand = random.randint(1, 8)
        return rand

    def toString(self):
        output = ""
        for i in range(0, len(self.maze)):
            for j in self.maze[i]:
                output += j
            output += "\n"
        return output




