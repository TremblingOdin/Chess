import numpy as np

class Game:
    def __init__(self, startArray, actionArray, name):
        self.currentPlayer = 1
        self.gameState = GameState(np.array(startArray, dtype=np.int), 1)
        self.actionSpace = np.array(actionArray, dtype=np.int)
        self.pieces = {'1':'X', '0':'-', '-1':'0'}
        self.gridshape = (6,7)
        self.input_shape = (2,6,7)
        self.name = name
        self.state_size = len(self.gameState.binary)
        self.action_size = len(self.actionSpace)


class GameState():
    def __init__(self, board, PlayerTurn, winConditions):
        self.board = board
        self.pieces = {'1':'X', '0':'-', '-1':'0'}
        self.winners = winConditions
        self.playerTurn = playerTurn
        self.binary = self._binary()
        self.id = self._convertStateToId()
        self.allowedActions = self._allowedActions()
        self.isEndGame = self._checkForEndGame()
        self.value = self._getValue()
        self.score = self._getScore()



