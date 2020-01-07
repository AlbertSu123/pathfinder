# Pathfinder - Aditya Saravanan
# A program for finding the shortest path between two different points on a 2-D grid.

from functions import *
from classes import *
import time


### Basic Functions ###

def board_creation():
    x_size = int(input("How long would you like the x-axis of your board to be? The maximum should be 100. "))
    y_size = int(input("\nHow long would you like the y-axis of your board to be? The maximum should be 100. "))
    walls = wall_creation(x_size, y_size)
    return Board(x_size, y_size, walls)

def wall_creation(x_size, y_size):
    need_walls = input("\nPress enter to create and randomize walls. For user-defined walls, please run by yourself, interactively, in the command line.")
    return random_wall_creator(x_size, y_size)

def choose_algorithm():
    print("\nThere are four different kinds of algorithms. Breadth-first-search, depth-first-search, Dijkstra's algorithm, and the A* algorithm.")
    algo_type = input("\nWhich algorithm would you like? ")
    if "*" in algo_type:
        return a_star
    elif "di" in algo_type.lower():
        return dijkstras
    elif "depth" in algo_type.lower():
        return depth_first_search
    elif "brea" in algo_type.lower():
        return breadth_first_search
    print("\nSorry, what you typed didn't make sense. Please type one of the four algorithms.\n")
    return choose_algorithm()

def choose_start_and_end_points(board):
    x1 = int(input("\nPlease type the x-value for your desired startpoint. "))
    y1 = int(input("\nPlease type the y-value for your desired startpoint. "))
    if not board.find_node_from_coordinates([x1, y1]):
        print("\nSorry, that startpoint is invalid. Either it's not on the board, or it's a position of a wall. Choose another point, please.\n")
        return choose_start_and_end_points(board)
    x2 = int(input("\nPlease type the x-value for your desired endpoint. Remember, your endpoint cannot be your start point. "))
    y2 = int(input("\nPlease type the y-value for your desired endpoint. Remember, your endpoint cannot be your start point. "))
    if not board.find_node_from_coordinates([x2, y2]):
        print("\nSorry, that startpoint is invalid. Either it's not on the board, or it's a position of a wall. Choose another point, please.\n")
        return choose_start_and_end_points(board)
    if [x1, y1] == [x2, y2]:
        print("\nYou chose the same startpoint and endpoint. Please try again.\n")
        return choose_start_and_end_points(board)
    return [x1, y1], [x2, y2]

def process_result(start_point, end_point, algorithm, board):
    start_time = time.process_time()
    result = algorithm(board, start_point, end_point)
    time_taken = time.process_time() - start_time
    if not result or len(result) == 1:
        print("\nNo path could be found by the algorithm. Either this algorithm is not suited for the task (often the case with DFS) or the startpoint/endpoint cannot be reached due to walls.")
    else:
        print("\nThis was the path found by the algorithm: ", result)
        print("\nThis was the amount of time that it took the algorithm to find the path: ", time_taken, " seconds")
    waiting = input("\nPress enter once you are ready to continue. ")

### Execution Functions ###

def restart(board):
    restart = input("\nWould you like to keep the same board? Type 'keep'. Otherwise, to restart, type 'restart'. Use Ctrl + C to exit. ")
    if "k" in restart:
        loop(board)
    elif "res" in restart:
        loop()
    else:
        print("\nSorry, what you typed didn't make sense. Make sure to pick one of the options above.\n")
        restart(board)


def loop(board=None):
    try:
            if board is None:
                board = board_creation()
            algorithm = choose_algorithm()
            start_point, end_point = choose_start_and_end_points(board)
            process_result(start_point, end_point, algorithm, board)
            restart(board)
    except ValueError as value:
        print("\nYou didn't enter the proper value(s). Please try again, and follow the instructions. This was the error message: ", value, "\n")
        loop()
    except KeyboardInterrupt as key:
        print("\n\nThanks for using Pathfinder.\n")

### Runtime Functions ###
def main():
    print("\nWelcome to...")
    print("""
          ____       _   _      __ _           _
         |  _ \ __ _| |_| |__  / _(_)_ __   __| | ___ _ __
         | |_) / _` | __| '_ \| |_| | '_ \ / _` |/ _ \ '__|
         |  __/ (_| | |_| | | |  _| | | | | (_| |  __/ |
         |_|   \__,_|\__|_| |_|_| |_|_| |_|\__,_|\___|_|
                                                   \n""")
    loop()

main()
