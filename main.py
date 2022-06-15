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
            new_cell = Cell(row_grid, column_grid, CELL_SIZE, rows)
            grid[row_grid].append(new_cell)


make_cell_grid()
end_program = False
start, end = None, None


def calculate_distance(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)


while not end_program:
    mouse_moved = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            end_program = True

        elif pygame.mouse.get_pressed()[0]:
            row = pygame.mouse.get_pos()[0] // CELL_SIZE
            column = pygame.mouse.get_pos()[1] // CELL_SIZE
            grid[row][column].make_barrier()

        elif pygame.mouse.get_pressed()[2]:
            row = pygame.mouse.get_pos()[0] // CELL_SIZE
            column = pygame.mouse.get_pos()[1] // CELL_SIZE
            grid[row][column].make_empty()

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

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and start and end:
                print("Algorithm started")

    draw_cells()
    draw_lines()
    pygame.display.flip()
