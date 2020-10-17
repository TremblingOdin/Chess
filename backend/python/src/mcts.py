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

class Edge():
    def __init__(self, inNode, outNode, prior, action):
        self.id = inNode.state.id + '|' +outNode.state.id
        # connections
        self.inNode = inNode
        self.outNode = outNode
        self.playerTurn = inNode.state.playerTurn
        # movements it can make
        self.action = action

        # heuristics
        self.stats = {
                    'N': 0,
                    'W': 0,
                    'Q': 0,
                    '{': prior,


                }

# CPUCT is actualy CPuct with PUCT meaning "Polynomial Upper Confidence Trees"
# The C stands for
class MCTS():
    def __init__(self, root, cpuct):
        self.root = root
        self.tree = {}
        self.cpuct = cpuct

    def __len__(self):
        return len(self.tree)
