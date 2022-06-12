import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

class Cell:
    def __init__(self, row, column, width):
        self.x = row * width
        self.y = column * width
        self.row = row
        self.column = column
        self.width = width
        self.neighbours = []
        self.color = WHITE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def make_cell_start(self):
        self.color = BLUE

    def make_cell_end(self):
        self.color = BLACK
