# Pathfinder - Aditya Saravanan
# A program for finding the shortest path between two different points on a 2-D grid.

from functions import *
from classes import *
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import time


### Helper Functions ###

def convert_board_to_map(board, visited):
    """Converts the board to a map. This is an 2-D array of the same size of the
    board that has different values if the corresponding point on the board is
    an unvisited node, a visited node, or a wall. Used to create a colormap."""
    reversed_board_array = []
    for y_counter in range(board.y_size + 1):
        row = []
        for x_counter in range(board.x_size + 1):
            if board.find_node_from_coordinates([x_counter, y_counter]):
                if [x_counter, y_counter] in visited:
                    row.append(25)
                else:
                    row.append(15)
            else:
                row.append(5)
        reversed_board_array.append(row)
    return list(reversed(reversed_board_array))


# Drawing Functions ###

def draw_board(board, visited):
    data = convert_board_to_map(board, visited)
    color_map = colors.ListedColormap(['black', 'white', 'red'])
    bounds = [0, 10, 20, 30]
    norm = colors.BoundaryNorm(bounds, color_map.N)
    fig, ax = plt.subplots()
    ax.imshow(data, cmap=color_map, norm=norm)
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
    ax.set_xticks(np.arange(-.5, board.x_size+1, 1));
    ax.set_yticks(np.arange(-.5, board.y_size+1, 1));
    ax.set_xticklabels([]);
    ax.set_yticklabels([]);
    plt.tight_layout()
    plt.show()
    plt.close()
