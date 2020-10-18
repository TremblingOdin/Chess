import numpy as np

class Game:
    def __init__(self, start_array, action_array, name):
        self.currentPlayer = 1
        self.game_state = GameState(np.array(startArray, dtype=np.int), 1)
        self.action_space = np.array(actionArray, dtype=np.int)
        self.pieces = {'1':'X', '0':'-', '-1':'0'}
        self.gridshape = (6,7)
        self.input_shape = (2,6,7)
        self.name = name
        self.state_size = len(self.game_state.binary)
        self.action_size = len(self.action_space)


class GameState():
    def __init__(self, board, player_turn, win_conditions, game_play):
        self.board = board
        self.pieces = {'1':'X', '0':'-', '-1':'0'}
        self.winners = win_conditions
        self.player_turn = player_turn
        self.binary = self._binary()
        self.id = self._convert_state_to_id()
        self.allowedActions = game_play
        self.isEndGame = self._check_for_end_game()
        self.value = self._get_value()
        self.score = self._get_score()
        



