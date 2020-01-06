# Pathfinder - Aditya Saravanan
# A program for finding the shortest path between two different points.

# Meant to check if the point is on the board_size_x by board_size_y grid contained in the first quadrant
def check_if_on_board(point, board_size_x, board_size_y):
    if point[0] > board_size_x or point[0] < 0 or point[1] > board_size_y or point[1] < 0:
        return False
    return True

# Returns a list of all possible valid movements from the current position.
def possible_movements(point, board_size_x, board_size_y):
    movement_lst = []
    movement_lst.append([point[0] + 1, point[1]])
    movement_lst.append([point[0] - 1, point[1]])
    movement_lst.append([point[0], point[1] + 1])
    movement_lst.append([point[0], point[1] - 1])
    return [point for point in movement_lst if check_if_on_board(point, board_size_x, board_size_y)]
