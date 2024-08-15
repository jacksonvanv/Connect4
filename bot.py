import random

from base import ConnectNBase, Player

class Bot:
    """
    Class for implementing a simple bot. The bot does the following:
    1. Take the winning move, if there is one.
    2. Block the opponent, placing a piece in its winning spot.
    3. If none of the above, choose a column randomly.
    """
    connectm: ConnectNBase
    player: Player
    opponent: Player

    def __init__(self, connectm: ConnectNBase, player: Player,
                 opponent: Player):
        self._connectm = connectm
        self.player = player
        self.opponent = opponent

    def suggest_move(self) -> int:
        """
        Bot traverses the board to choose a possible move
        """
        opponent_winning_moves = []
        nonwinning_moves = []

        for col in range(self._connectm.num_cols):
            if not self._connectm.is_allowed(col):
                continue

            if self._connectm.is_winner(col, self.player):
                return col
            elif self._connectm.is_winner(col, self.opponent):
                opponent_winning_moves.append(col)
            else:
                nonwinning_moves.append(col)

        if len(opponent_winning_moves) > 0:
            return opponent_winning_moves[0]
        else:
            return random.choice(nonwinning_moves)
