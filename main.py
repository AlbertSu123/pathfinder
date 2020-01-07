



def board_creation():
    try:
        x_board_size = input("How long would you like the x-axis of your board to be? The maximum should be 100.")
        y_board_size = input("How long would you like the y-axis of your board to be? The maximum should be 100.")
        walls = input("Please enter a list of two-element lists that signifies where you would like the walls to be.")
        return Board()
    except TypeError as type:
        print("Sorry! You entered the wrong type of data for an argument.")
        print("Here's the error message: " + str(type))











# handle errors in new main.py, make classes.py, algs.py
# make it possible to remove list of nodes (walls) (before creation of connections)
# make it possible to change weights (future)
# same start/end node? no path?
# timer!!
