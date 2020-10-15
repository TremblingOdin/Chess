import numpy as np

class Node():
    def __init__(self, state):
        self.state = state
        self.playerTurn = state.playerTurn
        self.id = state.id
        self.edges = [] # This is a graph so edges are how this node connnects to other nodes

    def is_leaf(self):
        if len(self.edges) > 0:
            return False
        return True
