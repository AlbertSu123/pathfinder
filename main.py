# Pathfinder - Aditya Saravanan
# A program for finding the shortest path between two different points on a 2-D grid.

from functions import *
from classes import *
import random


### Functions ###

def board_creation():
    try:
        x_size = input("How long would you like the x-axis of your board to be? The maximum should be 100.")
        y_size = input("How long would you like the y-axis of your board to be? The maximum should be 100.")
        walls = wall_creation(x_size, y_size)
        return Board(x_size, y_size, walls)

def wall_creation(x_size, y_size):
    need_walls = input("Please enter a list of two-element lists that signifies where you would like the walls to be. Type [] to have no walls, or type 'random' to randomize your walls.")
    if type(walls) == "list":
        return need_walls
    elif "ran" in need_walls:
        return random_wall_creator(x_size, y_size)
    else:
        print("Sorry, what you typed doesn't make sense. Please choose one of the options.")
        wall_creation(x_size, y_size)

def choose_algorithm():
    print("There are four different kinds of algorithms. Breadth-first-search, depth-first-search, Djikstra's algorithm, and the A* algorithm.")
    algo_type = input("Which algorithm would you like?")
    if type(algo_type) == "string":
        if "*" in algo_type:
            return a_star
        elif "dj" in algo_type:
            return djikstras
        elif "depth" in algo_type:
            return depth_first_search
        elif "brea" in algo_type:
            return breadth_first_search
    print("Sorry, what you typed didn't make sense. Please type one of the four algorithms.")
    return choose_algorithm()

def choose_start_and_end_points(board):
    try:
        start_point = input("Please type a two-element list of integers for your desired startpoint.")
        end_point = input("Please type a two-element list of integers for your desired endpoint. Your endpoint cannot be your start point!")
        if type(start_point) is not "list" or type(end_point) is not "list" or start_point == end_point:
            print("You did not follow the instructions. Pleas try again.")
            return choose_start_and_end_points(board)
        return start_point, end_point



# from board_creation
    # except TypeError as type:
    #     print("Sorry! You entered the wrong type of data for an argument.")
    #     print("Here's the error message: ", type)

# from choose_start_and_end_points
    #
    # except ValueError as value:
    #     print("Sorry, you've chosen a starting or ending value that's a wall.")
    #     choose_start_and_end_points(board)




# handle errors in new main.py, make classes.py, algs.py
# make it possible to change weights (future)
# no path?
# timer!!
# random walls (1/3)
