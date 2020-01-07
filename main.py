# Pathfinder - Aditya Saravanan
# A program for finding the shortest path between two different points on a 2-D grid.

class Node:
    """A node, meant to act as a single-unit square on a graph."""
    can_use = True
    distance = float('inf')
    weight = 1
    previous_node = None

    def __init__(self, x_pos, y_pos):
        self.coordinates = [x_pos, y_pos]
        self.x_coordinate = x_pos
        self.y_coordinate = y_pos
        self.connections = []

    def check_node_neighbors(node1, node2):
        if node1.x_coordinate == node2.x_coordinate:
            if abs(node1.y_coordinate - node2.y_coordinate) == 1:
                return True
            return False
        elif node1.y_coordinate == node2.y_coordinate:
            if abs(node1.x_coordinate - node2.x_coordinate) == 1:
                return True
            return False
        return False


class Board:
    """A Board consists of many nodes, tied together to make a graph-like structure."""
    def __init__(self, x_size, y_size):
        self.values = []
        self.fill_board(x_size, y_size)
        self.make_connections()

    def fill_board(self, x_size, y_size):
        for xcounter in range(x_size+1):
            for ycounter in range(y_size+1):
                self.values.append(Node(xcounter, ycounter))

    def make_connections(self):
        for node in self.values:
            for other_node in self.values:
                if Node.check_node_neighbors(node, other_node):
                    node.connections.append(other_node)

    def find_node_from_coordinates(self, point):
        for node in self.values:
            if node.coordinates == point:
                return node


def breadth_first_search(board, start_point, end_point):
    """Performs the breadth-first-search pathfinding algorithm."""
    first_node = board.find_node_from_coordinates(start_point)
    queue = []
    visited = []
    queue.append((first_node, [start_point]))
    visited.append(first_node)
    while queue:
        current_node, path_so_far = queue.pop(0)
        for movement_node in current_node.connections:
            if movement_node not in visited:
                visited.append(movement_node)
                if movement_node.coordinates == end_point:
                    return path_so_far + [end_point]
                else:
                    queue.append((movement_node, path_so_far + [movement_node.coordinates]))


def depth_first_search(board, start_point, end_point):
    """Performs the depth-first-search pathfinding algorithm."""
    first_node = board.find_node_from_coordinates(start_point)
    def dfs_helper(visited, current_node, path_so_far):
        if current_node.coordinates == end_point:
            yield path_so_far
        else:
            for movement_node in current_node.connections:
                if movement_node not in visited:
                    visited.append(movement_node)
                    return dfs_helper(visited, movement_node, path_so_far + [movement_node.coordinates])
    return dfs_helper([first_node], first_node, [start_point])


def dijkstras(board, start_point, end_point):
    """Performs Dijkstra's pathfinding algorithm."""
    first_node = board.find_node_from_coordinates(start_point)
    for node in board.values:
        node.distance = float('inf')
    first_node.distance = 0
    queue = list(board.values)
    while queue:
        minimum_distance_from_root_node = min(queue, key = lambda node: node.distance)
        queue.remove(minimum_distance_from_root_node)
        if minimum_distance_from_root_node.coordinates == end_point:
            return backtrack_path_creator(minimum_distance_from_root_node)
        for movement_node in minimum_distance_from_root_node.connections:
            if movement_node in queue:
                temp = minimum_distance_from_root_node.distance + movement_node.weight
                if temp < movement_node.distance:
                    movement_node.distance = temp
                    movement_node.previous_node = minimum_distance_from_root_node


def a_star(board, start_point, end_point, heuristic):
    """Performs the A* pathfinding algorithm, with a heuristic of choice."""
    first_node = board.find_node_from_coordinates(start_point)
    end_node = board.find_node_from_coordinates(end_point)
    for node in board.values:
        node.distance = float('inf')
    first_node.distance = 0 + heuristic(first_node, end_node)
    queue = [first_node]
    while queue:
        minimum_distance_from_root_node = min(queue, key = lambda node: node.distance)
        queue.remove(minimum_distance_from_root_node)
        if minimum_distance_from_root_node.coordinates == end_point:
            return backtrack_path_creator(minimum_distance_from_root_node)
        for movement_node in minimum_distance_from_root_node.connections:
            temp = minimum_distance_from_root_node.distance + heuristic(movement_node, end_node) + movement_node.weight
            if temp < movement_node.distance:
                movement_node.distance = temp
                movement_node.previous_node = minimum_distance_from_root_node
                queue.append(movement_node)



















def backtrack_path_creator(final_node):
    """Takes in the final node after performing a pathfinding algorithm,
    backtracks through the "previous_node" attribute to find the shortest path."""
    current_node = final_node
    path_reversed = []
    while current_node is not None:
        path_reversed.append(current_node.coordinates)
        current_node = current_node.previous_node
    return list(reversed(path_reversed))


def manhattan_distance(start_node, end_node):
    """A popular heuristic for use with the A* algorithm."""
    return (abs(start_node.x_coordinate - end_node.x_coordinate)
            + abs(start_node.y_coordinate - end_node.y_coordinate))


















# complete algs (bidirectional)
# clean up code (when no path, etc.)
# handle errors in new main.py, make classes.py, algs.py
# make it possible to remove list of nodes (walls) (before creation of connections)
# make it possible to change weights (future)
