import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


class Cell:
    def __init__(self, row, column, width, rows):
        self.x = row * width
        self.y = column * width
        self. rows = rows
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
        self.color = RED

    def make_empty(self):
        self.color = WHITE

    def make_barrier(self):
        self.color = BLACK

    def is_barrier(self):
        if self.color == BLACK:
            return True
        else:
            return False

    def update_neighbours(self, grid):
        if self.row > 0 and not grid[self.row-1][self.column].is_barrier():
            self.neighbours.append(grid[self.row-1][self.column])

        if self.column > 0 and not grid[self.row][self.column - 1].is_barrier():
            self.neighbours.append(grid[self.row][self.column - 1])

        if self.row < self.rows - 1 and not grid[self.row + 1][self.column].is_barrier():
            self.neighbours.append(grid[self.row + 1][self.column])

        if self.column < self.rows - 1 and not grid[self.row][self.column + 1].is_barrier():
            self.neighbours.append(grid[self.row][self.column + 1])
