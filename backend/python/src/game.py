import numpy as np

class Game:
    def __init__(self, start_array, action_array, name, win_conditions, game_play, identities):
        self.start_array = start_array
        self.current_player = 1
        self.win_conditions = win_conditions
        self.game_play = game_play
        self.game_state = GameState(np.array(start_array, dtype=np.int), 1, self.win_conditions, self.game_play)
        self.action_space = np.array(actionArray, dtype=np.int)
        self.pieces = {'1':'X', '0':'-', '-1':'0'}
        self.gridshape = (6,7)
        self.input_shape = (2,6,7)
        self.name = name
        self.state_size = len(self.game_state.binary)
        self.action_size = len(self.action_space)
        self.identities = identities

    def reset(self):
        self.game_state = GameState(np.array(start_array, dtype = np.int), 1)
        self.current_player = 1
        return self.game_state

    def step(self, action):
        next_state, value, done = self.game_state.take_action(action)
        self.game_state = next_state
        self.current_player = -self.current_player
        info = None
        return ((next_state, value, done, info))

    def identities(self, state, action_values, height, width):
        identities = [(state, action_values)]
        current_board = state.board
        current_av = action_values

        temp_board_array = []
        temp_av_array = []

        for x in range(0, height):
            for y in range(width, -1, -1):
                index = width * height + y
                temp_board_array.append(current_board[index])
                temp_av_array.append(current_av[index])
                
        current_board = np.array(temp_board_array)
        current_av = np.array(temp_av_array)

        identities.append((state.reinitialize(current_board, state.player_turn),current_av))
        return identities


# to make it more modular the win conditions and gameplay should be passed in
# As I go through more of this I am thinking Game State might need to be defined from an external source in order to fully work
class GameState():
    def __init__(self, board, pieces player_turn, win_conditions, game_play, binary, conversion_to_id, endgame_check, value_function):
        self.board = board
        self.pieces = pieces
        self.winners = win_conditions
        self.player_turn = player_turn
        self.binary = binary
        self.id = conversion_to_id
        self.allowed_actions = game_play
        self.is_end_game = endgame_check
        self.value = value_function
        self.score = self._get_score()
       
    #I think I would need to ask for a new game state many times, so I made a function
    def reinitialize(self, board, player_turn):
        state = GameState(board, self.pieces, player_turn, self.winners, self.allowed_actions, self.binary, self.id, self.is_end_game, self.value)
        return state
        

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
