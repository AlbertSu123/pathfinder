import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np


def convert_board_to_array(board, visited):
    board_coordinates = convert_board_to_coordinates(board)
    reversed_board_array = []
    for x_counter in range(board.x_size + 1):
        reversed_board_array.append(create_row_of_board(board_coordinates, visited, x_counter))
    return list(reversed(reversed_board_array))

def create_row_of_board(board_coordinates, visited, current_row):
    row = []
    for y_counter in range(board.y_size + 1):
        if board.find_node_from_coordinates([current_row, y_counter]):
            if check_if_in_visited([current_row, y_counter]):
                row.append(25)
            else:
                row.append(15)
        row.append(5)
    return row

def convert_board_to_coordinates(board):
    return [node.coordinates for node in board.values]

def check_if_in_visited(coordinates, visited):
    for visited_point in visited:
        if visited_point == coordinates:
            return True
    return False




















data = convert_board_to_array(board)

figure, axis = plt.subplots(1, 1, tight_layout = True)

grid = colors.ListedColormap(['black', 'white', 'red'])
bounds = [0, 10, 20, 30]
norm = colors.BoundaryNorm(bounds, grid.N)

for x in range(10):
    axis.axhline(x, lw=2, color='k', zorder=5)
    axis.axvline(x, lw=2, color='k', zorder=5)

axis.imshow(data, interpolation='none', cmap=grid, extent=[0, 10, 0, 10], zorder=0)

axis.axis('off')
plt.show()
