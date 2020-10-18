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
    def __init__(self, board, player_turn, win_conditions, game_play, binary, conversion_to_id, endgame_check, value_function):
        self.board = board
        self.pieces = {'1':'X', '0':'-', '-1':'0'}
        self.winners = win_conditions
        self.player_turn = player_turn
        self.binary = binary
        self.id = conversion_to_id
        self.allowed_actions = game_play
        self.is_end_game = endgame_check
        self.value = value_function
        self.score = self._get_score()
       
    def _get_score():
        tmp = self.value
        return(tmp[1],tmp[2])

    def take_action(self, action):
        new_board = np.array(self.board)
        nead_board[action] = self.player_turn

        new_state = self._reinitialize(new_board, -self.player_turn)

        value = 0
        done = 0

        if(new_state.is_end_game:
                value = new_state.value[0]
                done = 1

        return (new_state, value, done)
