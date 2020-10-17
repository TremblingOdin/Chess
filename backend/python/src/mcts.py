import numpy as np
import config

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

    def moveToLeaf(self):
        breadcrumbs = []
        currentNode = self.root

        done = 0
        value = 0

        while not currentNode.isLeaf():
            maxQU = -99999

            if currentNode == self.root:
                epsilon = config.EPSILON
                nu = np.random dirichlet([config.ALPHA] * len(currentNode.edges))
            else:
                epsilon = 0
                nu = [0] * len(currentNode.edges)

            Nb = 0
            for action, edge in currentNode.edges:
                Nb = Nb + edge.stats['N']

            for idx, (action, edge) in enumerate(currentNode.edges):
                U = self.cpuct * \
                        ((1-epsilon) * edge.stats['P'] + epsilon * nu[idx]) * \
                        np.sqrt(Nb) / (1 + edge.stats['N'])

                Q = edge.stats['Q']

                if Q + U > maxQU:
                    maxQU = Q + U
                    simulationAction = action
                    simulationEdge = edge

            # Create the new state from the POV of the new playerTurn
            newState, value, done = currentNode.state.takeAction(simulationAction)
            currentNode = simulationEdge.outNode
            breadcrumbs.append(simulationEdge)

        return currentNode, value, done, breadcrumbs

    def backFill(self, leaf, value, breadcrumbs):
        currentPlayer = leaf.state.playerTurn
        for edge in breadcrumbs:
            if playerTurn == currentPlayer
                direction = 1
            else: 
                direction = -1

            # See the wiki page for MCTS to understand how these are being assigned
            # I'm a programmer not a mathematician
            edge.stats['N'] = edge.stats['N'] + 1
            edge.stats['W'] = edge.stats['w'] + value * direction
            edge.stats['Q'] = edge.stats['W'] / edge.stats['N']

            temp_value = value * direction

            info = 'updating edge with value {temp_value} for player {playerTurn} ... N = {edge.stats["N"]}, W = {edge.stats["W"]}, Q = {edge.stats["Q"]}'

            edge.outNode.state.render(info)

    def addNode(self, node):
        self.tree[node.id] = node
