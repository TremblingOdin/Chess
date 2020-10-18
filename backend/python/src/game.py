import numpy as np

class Game:
    def __init__(self, start_array, action_array, name, win_conditions, game_play):
        self.currentPlayer = 1
        self.win_conditions = win_conditions
        self.game_play = game_play
        self.game_state = GameState(np.array(startArray, dtype=np.int), 1, self.win_conditions, self.game_play)
        self.action_space = np.array(actionArray, dtype=np.int)
        self.pieces = {'1':'X', '0':'-', '-1':'0'}
        self.gridshape = (6,7)
        self.input_shape = (2,6,7)
        self.name = name
        self.state_size = len(self.game_state.binary)
        self.action_size = len(self.action_space)


# to make it more modular the win conditions and gameplay should be passed in
# As I go through more of this I am thinking Game State might need to be defined from an external source in order to fully work
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
        
    def _binary(self):
        current_player_position = np.zeros(len(self.board), dtype=np.int)
        current_player_position[self.board==self.player_turn] = 1

        other_position = np.zeros(len(self.board), dtype=np.int)
        other_position[self.board==self.player_turn] = 1

        position = np.append(current_player_position, other_position)

        return(position)

    def _convert_state_to_id(self):
        player1_position = np.zeros(len(self.board), dtype = np.int)
        player1_position[self.board==1] = 1

        other_position = np.zeros(len(self.board), dtype=np.int)
        other_position[self.board==-1] = 1
        
        position = np.append(player1_position,other_position)
        
        id = ''.join(map(str,position))

        return id
