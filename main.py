# Pathfinder - Aditya Saravanan
# A program for finding the shortest path between two different points.

def find_slope(start_point, end_point):
    return (end_point[1] - start_point[1])/(end_point[0] - start_point[0])

def




# idea: make a line which sections the area where the point can actually move
# if the point moves outside this area, that path is considered null and void.
