# Pathfinder - Aditya Saravanan
# A program for finding the shortest path between two different points on a 2-D grid.

from functions import *
from classes import *
from visuals import *
import time


### Basic Functions ###

def board_creation():
    """Creates the board that will be used, with user-specified dimensions."""
    x_size = int(input("\nHow long would you like the x-axis of your board to be? The value should be between 2 and 100. "))
    y_size = int(input("\nHow long would you like the y-axis of your board to be? The value should be between 2 and 100. "))
    if x_size > 100 or y_size > 100 or x_size < 2 or y_size < 2:
        print("Sorry, the size of the board is unattainable. Please enter new dimensions.")
        return board_creation()
    walls = wall_creation(x_size, y_size)
    return Board(x_size, y_size, walls)

def wall_creation(x_size, y_size):
    """Creates random walls to be placed on the board."""
    need_walls = input("\nPress enter to create and randomize walls. For user-defined walls, please run by yourself, interactively, in the command line.")
    return random_wall_creator(x_size, y_size)

def choose_algorithm():
    """Allows the user to choose an algorithm to perform on their board."""
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
    print("\nSorry, what you typed didn't make sense. Please choose one of the four algorithms.\n")
    return choose_algorithm()

def choose_start_and_end_points(board):
    """Allows the user to select the starting and ending points on their board."""
    x1 = int(input("\nPlease type the x-value for your desired startpoint. "))
    y1 = int(input("\nPlease type the y-value for your desired startpoint. "))
    if not board.find_node_from_coordinates([x1, y1]):
        print("\nSorry, that startpoint is invalid. Either it's not on the board, or it's a position of a wall. Choose another point, please.\n")
        return choose_start_and_end_points(board)
    x2 = int(input("\nPlease type the x-value for your desired endpoint. Remember, your endpoint cannot be your start point. "))
    y2 = int(input("\nPlease type the y-value for your desired endpoint. Remember, your endpoint cannot be your start point. "))
    if not board.find_node_from_coordinates([x2, y2]):
        print("\nSorry, that endpoint is invalid. Either it's not on the board, or it's a position of a wall. Choose another point, please.\n")
        return choose_start_and_end_points(board)
    if [x1, y1] == [x2, y2]:
        print("\nYou chose the same startpoint and endpoint. Please try again.\n")
        return choose_start_and_end_points(board)
    return [x1, y1], [x2, y2]

def process_result(start_point, end_point, algorithm, board):
    """Processes the path given the starting point, ending point, algorithm, and
    board. Prints out the path and the time taken to find the path."""
    start_time = time.process_time()
    result = algorithm(board, start_point, end_point)
    time_taken = time.process_time() - start_time
    if not result or len(result) == 1:
        print("\nNo path could be found by the algorithm. Either this algorithm is not suited for the task or the startpoint/endpoint cannot be reached due to walls.")
        result = []
    else:
        print("\nThis was the path found by the algorithm: ", result)
        print("\nThis was the amount of time that it took the algorithm to find the path: ", time_taken, " seconds")
    print("\nPlease see the other window for a picture of the board. Exit the window to continue.")
    draw_board(board, result)


### Execution Functions ###

def loop(board=None):
    """The main loop of the program, where everything happens."""
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

def restart(board):
    """Function used in mutual recursion with the loop() function to allow the
    user to choose whether to keep their board, or generate a new one after an
    algorithm runs."""
    want_to_restart = input("\nWould you like to keep the same board? Type 'keep'. Otherwise, to restart, type 'restart'. Use Ctrl + C, then Enter, to exit. ")
    if "k" in want_to_restart:
        loop(board)
    elif "res" in want_to_restart:
        loop()
    else:
        print("\nSorry, what you typed didn't make sense. Make sure to pick one of the options above.\n")
        restart(board)


### Runtime Functions ###

def main():
    """A function used as an introduction to the program, and to run the program's
    main loop."""
    print("\nWelcome to...")
    print("""
          ____       _   _      __ _           _
         |  _ \ __ _| |_| |__  / _(_)_ __   __| | ___ _ __
         | |_) / _` | __| '_ \| |_| | '_ \ / _` |/ _ \ '__|
         |  __/ (_| | |_| | | |  _| | | | | (_| |  __/ |
         |_|   \__,_|\__|_| |_|_| |_|_| |_|\__,_|\___|_|
                                                    """)
    loop()

main()
