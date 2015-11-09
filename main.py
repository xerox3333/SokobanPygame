import pygame
import sys
from menu import Menu
from maze import Maze
from player import Player
from pygame.locals import *

maze = Maze()
player = Player(1, 1, "*")

MAXFPS = 30
TILEWIDTH = 64
TILEHEIGHT = 64
TILEFLOORHEIGHT = 64
WIDTH = TILEWIDTH * maze.width
HEIGHT = 640

BRIGHTBLUE = (0, 170, 255)
WHITE = (255, 255, 255)
BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

IMAGES = {'floor': pygame.image.load('img/floor.png'),
          'wall': pygame.image.load('img/wall.png'),
          'crate': pygame.image.load('img/crate.png'),
          'floorEnd': pygame.image.load('img/floorSpace.png'),
          'spacer': pygame.image.load('img/spacer.png'),
          'forkLiftUp': pygame.image.load('img/ForkLiftUp.png'),
          'forkLiftDown': pygame.image.load('img/ForkLiftDown.png'),
          'forkLiftLeft': pygame.image.load('img/ForkLiftLeft.png'),
          'forkLiftRight': pygame.image.load('img/ForkLiftRight.png')}

TILEMAP = {' ': IMAGES['floor'],
           '#': IMAGES['wall'],
           'C': IMAGES['crate'],
           'E': IMAGES['floorEnd'],
           '/': IMAGES['spacer'],
           '*': IMAGES['forkLiftUp']}

pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sokoban v 0.01')
BASICFONT = pygame.font.SysFont('monospace', 18)
SCOREFONT = pygame.font.SysFont('arial', 28)
SCOREFONT.set_bold(True)

# Create main menu
menu_items = ('Press enter to start', '')
mainMenu = Menu(DISPLAYSURF, menu_items, BGCOLOR, BASICFONT, TEXTCOLOR)
mainMenu.run()

def movePlayerRight():
    nextPos = maze.getCharAtPos(player.getRow(), player.getCol() + 1)
    if nextPos == "#":
        print "This is a wall"
    else:
        if nextPos == "C":
            # Check that the next position is clear for the crate
            nextCratePos = maze.getCharAtPos(player.getRow(), player.getCol() + 2)
            if nextCratePos == "#" or nextCratePos == "C":
                # path is obstructed
                movePlayerLeft()
                player.decrementMoves()
            else:
                # path is clear to push crate
                if nextPos == "C":
                    maze.clearAtPos(player.getRow(), player.getCol() + 1)
                    maze.setCharAtPos(player.getRow(), player.getCol() + 2, "C")
                    #maze.placeCrate(player.getRow(), player.getCol() + 2)
                    player.incrementMoves()
            print "Crate found"
        else:
            print "Empty space found"
            player.incrementMoves()

        maze.clearAtPos(player.getRow(), player.getCol())
        player.moveRight()
        TILEMAP['*'] = IMAGES['forkLiftRight']
        maze.placePlayer(player.getChar(), player.getRow(), player.getCol())

    print maze.toString()
    print player.toString()


def movePlayerLeft():
    nextPos = maze.getCharAtPos(player.getRow(), player.getCol() - 1)
    if nextPos == "#":
        print "This is a wall"
    else:
        if nextPos == "C":
            # Check that the next position is clear for the crate
            nextCratePos = maze.getCharAtPos(player.getRow(), player.getCol() - 2)
            if nextCratePos == "#" or nextCratePos == "C":
                # path is obstructed
                movePlayerRight()
                player.decrementMoves()
            else:
                # path is clear to push crate
                if nextPos == "C":
                    maze.clearAtPos(player.getRow(), player.getCol() - 1)
                    maze.setCharAtPos(player.getRow(), player.getCol() - 2, "C")
                    #maze.placeCrate(player.getRow(), player.getCol() - 2)
                    player.incrementMoves()
            print "Crate found"
        else:
            print "Empty space found"
            player.incrementMoves()

        maze.clearAtPos(player.getRow(), player.getCol())
        player.moveLeft()
        TILEMAP['*'] = IMAGES['forkLiftLeft']
        maze.placePlayer(player.getChar(), player.getRow(), player.getCol())

    print maze.toString()
    print player.toString()


def movePlayerUp():
    nextPos = maze.getCharAtPos(player.getRow() - 1, player.getCol())
    if nextPos == "#":
        print "This is a wall"
    else:
        if nextPos == "C":
            # Check that the next position is clear for the crate
            nextCratePos = maze.getCharAtPos(player.getRow() - 2, player.getCol())
            if nextCratePos == "#" or nextCratePos == "C":
                # path is obstructed
                movePlayerDown()
                player.decrementMoves()
            else:
                # path is clear to push crate
                if nextPos == "C":
                    maze.clearAtPos(player.getRow() - 1, player.getCol())
                    maze.setCharAtPos(player.getRow() - 2, player.getCol(), "C")
                    #maze.placeCrate(player.getRow() - 2, player.getCol())
                    player.incrementMoves()
            print "Crate found"
        else:
            print "Empty space found"
            player.incrementMoves()

        maze.clearAtPos(player.getRow(), player.getCol())
        player.moveUp()
        TILEMAP['*'] = IMAGES['forkLiftUp']
        maze.placePlayer(player.getChar(), player.getRow(), player.getCol())

    print maze.toString()
    print player.toString()


def movePlayerDown():
    nextPos = maze.getCharAtPos(player.getRow() + 1, player.getCol())
    if nextPos == "#":
        print "This is a wall"
    else:
        if nextPos == "C":
            # Check that the next position is clear for the crate
            nextCratePos = maze.getCharAtPos(player.getRow() + 2, player.getCol())
            if nextCratePos == "#" or nextCratePos == "C":
                # path is obstructed
                movePlayerUp()
                player.decrementMoves()
            else:
                # path is clear to push crate
                if nextPos == "C":
                    maze.clearAtPos(player.getRow() + 1, player.getCol())
                    maze.setCharAtPos(player.getRow() + 2, player.getCol(), "C")
                    player.incrementMoves()
            print "Crate found"
        else:
            print "Empty space found"
            player.incrementMoves()

        maze.clearAtPos(player.getRow(), player.getCol())
        player.moveDown()
        TILEMAP['*'] = IMAGES['forkLiftDown']
        maze.placePlayer(player.getChar(), player.getRow(), player.getCol())

    print maze.toString()
    print player.toString()


def generateRandomCrate():
    """ Generates a random X and Y and set the charater at that position to C
    none
    generateRandomCrate()
    NoneType"""
    randX = maze.getRandX()
    randY = maze.getRandY()
    randPos = maze.getCharAtPos(randX, randY)
    while randPos == "C" or randPos == "#":
        randX = maze.getRandX()
        randY = maze.getRandY()

    maze.setCharAtPos(randX, randY, "C")


def drawMap(maze):
    mapSurfaceWidth = (maze.getWidth() * TILEWIDTH)
    mapSurfaceHeight = (maze.getHeight() * TILEHEIGHT)
    mapSurf = pygame.Surface((mapSurfaceWidth, mapSurfaceHeight))
    mapSurf.fill(BGCOLOR)
    for h in range(maze.getHeight()):
        for w in range(maze.getWidth()):
            thisTile = pygame.Rect((w * TILEWIDTH, h * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT))
            if maze.getCharAtPos(h, w) in TILEMAP:
                baseTile = TILEMAP[maze.getCharAtPos(h, w)]

            mapSurf.blit(baseTile, thisTile)
    return mapSurf


def main():
    global FPSCLOCK, DISPLAYSURF, IMAGES, TILEMAP, BASICFONT
    maze.placePlayer('*', 1, 1)
    print maze.toString()
    drawMap(maze)
    generateRandomCrate()

    redraw = False

    while True:
        # Check for input
        for event in pygame.event.get():
            if event.type == QUIT:
                exitGame()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    movePlayerRight()
                if event.key == K_LEFT:
                    movePlayerLeft()
                elif event.key == K_UP:
                    movePlayerUp()
                elif event.key == K_DOWN:
                    movePlayerDown()
                elif event.key == K_SPACE:
                    restart()
            redraw = True

        DISPLAYSURF.fill(BGCOLOR)

        if redraw:
            mapSurf = drawMap(maze)
            redraw = False

            mapSurfRect = mapSurf.get_rect()
            mapSurfRect.center = ((WIDTH / 2), (HEIGHT / 2))

            score  = SCOREFONT.render("No of Moves: " + str(player.getScore()), 1, WHITE)
            DISPLAYSURF.blit(mapSurf, mapSurfRect)
            DISPLAYSURF.blit(score, ((WIDTH - 220), (HEIGHT - 40)))

            pygame.display.update()  # draw DISPLAYSURF to the screen.
            FPSCLOCK.tick()


def restart():
    pass


def exitGame():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
