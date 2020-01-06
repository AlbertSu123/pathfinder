# Pathfinder - Aditya Saravanan
# A program for finding the shortest path between two different points.


# A node.
# Meant to act as a single-unit square on a graph.
class Node:

    can_use = True

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


# A Board consists of many nodes, tied together to make a graph-like structure.
class Board:

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


# The BFS (breadth-first-search) algorithm.
# Interestingly, because all squares are interconnected, it's only possible for this algorithm to yield one path.
# Nodes on the remainder of the board are 'invalidated' through the 'visited' array.
def breadth_first_search(board, start_point, end_point):

    queue = []
    visited = []
    queue.append((board.find_node_from_coordinates(start_point), [start_point]))
    visited.append(board.find_node_from_coordinates(start_point))

    while queue:
        current, path_so_far = queue.pop(0)
        for movement_node in current.connections:
            if movement_node not in visited:
                visited.append(movement_node)
                if movement_node.coordinates == end_point:
                    return path_so_far + [end_point]
                else:
                    queue.append((movement_node, path_so_far + [movement_node.coordinates]))
