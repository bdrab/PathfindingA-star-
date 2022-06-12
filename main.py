from cell import Cell
import pygame

WIN_SIZE = 800
CELL_SIZE = 80
rows = WIN_SIZE // CELL_SIZE
grid = []

pygame.init()
screen = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))
pygame.display.set_caption("A* Algorithm")


def draw_lines():
    for row_lines in range(rows):
        for column_lines in range(rows):
            pygame.draw.line(screen, (0, 0, 0), (row_lines * CELL_SIZE, 0), (row_lines * CELL_SIZE, WIN_SIZE), 3)
            pygame.draw.line(screen, (0, 0, 0), (0, column_lines * CELL_SIZE), (WIN_SIZE, column_lines * CELL_SIZE), 3)


def draw_cells():
    for row_cell in grid:
        for cell in row_cell:
            cell.draw(screen)


def make_cell_grid():
    for row_grid in range(rows):
        grid.append([])
        for column_grid in range(rows):
            new_cell = Cell(row_grid, column_grid, CELL_SIZE)
            grid[row].append(new_cell)


make_cell_grid()
end_program = False
start, end = None, None

while not end_program:
    mouse_moved = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            end_program = True

        elif pygame.mouse.get_pressed()[0]:
            row = pygame.mouse.get_pos()[0] // CELL_SIZE
            column = pygame.mouse.get_pos()[1] // CELL_SIZE
            grid[row][column].color = (0, 255, 0)

        elif pygame.mouse.get_pressed()[2]:
            row = pygame.mouse.get_pos()[0] // CELL_SIZE
            column = pygame.mouse.get_pos()[1] // CELL_SIZE
            grid[row][column].color = (255, 255, 255)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2:
                row = pygame.mouse.get_pos()[0] // CELL_SIZE
                column = pygame.mouse.get_pos()[1] // CELL_SIZE
                if not start:
                    start = grid[row][column]
                    start.make_cell_start()
                elif not end:
                    end = grid[row][column]
                    end.make_cell_end()

    draw_cells()
    draw_lines()
    pygame.display.flip()
