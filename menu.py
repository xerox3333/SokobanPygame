import pygame
from pygame.locals import *
import sys

pygame.init()

class Menu:

    def __init__(self, screen, items, bg_color, font, font_color):
        """ Constructor method for menu creates a menu on screen with specified items
         (pygame.display, str[], (int, int, int), str, (int, int, int), int -> none
         NoneType"""
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.bg_color = bg_color
        self.font = font
        #self.font_size = font_size
        self.font_color = font_color

        self.clock = pygame.time.Clock()

        self.items = items
        #self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color

        self.items = []
        for index, item in enumerate(items):
            label = self.font.render(item, 1, font_color)

            width = label.get_rect().width
            height = label.get_rect().height

            posx = (self.scr_width / 2) - (width / 2)
            # t_h: total height of text block
            t_h = len(items) * height
            posy = (self.scr_height / 2) - (t_h / 2) + (index * height)

            self.items.append([item, label, (width, height), (posx, posy)])


    def run(self):
        menuloop = True
        while menuloop:
            self.clock.tick(30)

            # Get mouse input check for menu item press

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        menuloop = False
                        break
                    elif event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    menuloop = False

            # Redraw the background
            self.screen.fill(self.bg_color)

            for name, label, (width, height), (posx, posy) in self.items:
                self.screen.blit(label, (posx, posy))

            pygame.display.flip()
