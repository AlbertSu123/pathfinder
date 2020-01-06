# Pathfinder - Aditya Saravanan
# A program for finding the shortest path between two different points.



class Node:

    can_use = True
    connections = []

    def __init__(self, x_pos, y_pos):
        self.coordinates = [x_pos, y_pos]
        node.x_coordinate = x_pos
        node.y_coordinate = y_pos

    def check_if_neighbors(node1, node2):
        if node1.x_coordinate == node2.x_coordinate:
            if abs(node1.y_coordinate - node2.y_coordinate) == 1:
                return True
            return False
        elif node1.y_coordinate == node2.y_coodinate:
            if abs(node1.x_coordinate - node2.x_coodinate) == 1:
                return True
            return False
        return False

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
                if check_if_neighbors(node, other_node):
                    node.connections.append(other_node)
