from cell import Cell
import pygame
from queue import PriorityQueue

WIN_SIZE = 800
CELL_SIZE = 40
rows = WIN_SIZE // CELL_SIZE
grid = []

pygame.init()
screen = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))
pygame.display.set_caption("A* Algorithm")


def make_cell_grid():
    for row_grid in range(rows):
        grid.append([])
        for column_grid in range(rows):
            new_cell = Cell(row_grid, column_grid, CELL_SIZE, rows)
            grid[row_grid].append(new_cell)


def draw_lines():
    for row_lines in range(rows):
        for column_lines in range(rows):
            pygame.draw.line(screen, (0, 0, 0), (row_lines * CELL_SIZE, 0), (row_lines * CELL_SIZE, WIN_SIZE), 3)
            pygame.draw.line(screen, (0, 0, 0), (0, column_lines * CELL_SIZE), (WIN_SIZE, column_lines * CELL_SIZE), 3)


def draw_cells():
    for row_cell in grid:
        for cell in row_cell:
            cell.draw(screen)


def calculate_distance(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, current):
    while current in came_from:
        current = came_from[current]
        current.make_path()


def start_algorithm(grid_cell, start_cell, end_cell):
    count_value = 0
    open_set = PriorityQueue()
    open_set.put((0, count_value, start_cell))
    came_from = {}
    g_score = {spot: float("inf") for row_in_grid in grid_cell for spot in row_in_grid}
    g_score[start_cell] = 0
    f_score = {spot: float("inf") for row_in_grid in grid_cell for spot in row_in_grid}
    f_score[start_cell] = calculate_distance(start_cell.get_pos(), end_cell.get_pos())

    open_set_copy = {start_cell}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current_cell = open_set.get()[2]
        open_set_copy.remove(current_cell)

        if current_cell == end_cell:
            reconstruct_path(came_from, end_cell)
            start_cell.make_cell_start()
            end_cell.make_cell_end()
            return True

        for neighbour in current_cell.neighbours:
            temp_g_score = g_score[current_cell] + 1

            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = current_cell
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + calculate_distance(neighbour.get_pos(), end_cell.get_pos())
                if neighbour not in open_set_copy:
                    count_value += 1
                    open_set.put((f_score[neighbour], count_value, neighbour))
                    open_set_copy.add(neighbour)
                    neighbour.make_open()

        draw_cells()
        draw_lines()
        pygame.display.flip()

        if current_cell != start_cell:
            current_cell.make_closed()
    return False


make_cell_grid()
end_program = False
start, end = None, None

while not end_program:
    mouse_moved = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
                for row in grid:
                    for cell in row:
                        cell.update_neighbours(grid)

                if start_algorithm(grid, start, end):
                    print("Path has been found.")
                else:
                    print("There is no path to destination point.")

            elif event.key == pygame.K_r:
                for row in grid:
                    for cell in row:
                        cell.make_empty()
                start, end = None, None

    draw_cells()
    draw_lines()
    pygame.display.flip()
pygame.quit()
