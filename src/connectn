"""
Class for Implementing Connect N Logic
"""
from typing import Optional
import copy

from base import ConnectNBase, Player

class ConnectN(ConnectNBase):
    """
    
    """
    board: list[list[Optional[Player]]]
    winner: Optional[Player]
    max_heights: list[int]

    def __init__(self, num_rows: int, num_cols: int, n: int):
        super().__init__(num_rows, num_cols, n)
        self.board = [[None] * num_cols for _ in range(num_rows)]
        self.winner = None
        self.max_heights = [0] * num_cols
    
    def piece_loc(self, row: int, col: int):
        """
        See ABC
        """
        # The 0th row is the bottom row
        if not (0 <= row < self._num_rows):
            raise ValueError("Out of bounds")
        elif not (0 <= col < self._num_cols):
            raise ValueError("Out of bounds")
        return self.board[self._num_rows - 1 - row][col]
    
    def set_piece(self, row: int, col: int, player: Player):
        """
        Places the piece in the place where it is dropped
        """
        assert 0 <= row <= self._num_rows and 0 <= col <= self._num_cols
        self.board[self._num_rows - 1 - row][col] = player

    def is_allowed(self, col: int):
        """
        See ABC
        """
        return self.max_heights[col] <= self._num_rows
    
    def execute_move(self, col: int, player: Player):
        """
        See ABC
        """       
        if not self.is_allowed(col):
            raise ValueError(f"Move is not allowed, out of bounds")

        row = self.max_heights[col]
        self.set_piece(row, col, player)
        self.max_heights[col] += 1

        if self.winner_loc(row, col):
            self.winner = player
    
    def winner_loc(self, row: int, col: int):
        """
        Helper that returns a boolean of the location contains a winner
        """
        # Get player's color of the origin piece
        origin_piece = self.piece_loc(row, col)
        if origin_piece is None:
            return False

        directions = [(1, 0), (0, 1), (1, 1), (1, -1),
                      (-1, 0), (0, -1), (-1, -1), (-1, 1)]

        for r_offset, c_offset in directions:
            # Count original player's piece
            total_count = 1
            # Count adjacent pieces from the same player
            total_count += self.consecutive(row, col, r_offset, c_offset)
            if total_count >= self._n:
                return True

        return False

    def consecutive(self, row, col, r_offset: int, c_offset: int) -> int:
        """
        Helper that traverses consecutive pieces to determine the winner
        """
        origin_piece = self.piece_loc(row, col)
        count = 0
        r, c = row + r_offset, col + c_offset
        while (0 <= r < self._num_rows
            and 0 <= c < self._num_cols
            and self.piece_loc(r, c) == origin_piece):
            count += 1
            r += r_offset
            c += c_offset
        return count

    def is_winner(self, col: int, player: Player):
        """
        See ABC
        """
        if not self.is_allowed(col):
            return False
        row = self.max_heights[col]
        self.set_piece(row, col, player)
        winner = self.winner_loc(row, col)
        self.set_piece(row, col, None)

        return winner

    def new_game(self):
        """
        See ABC
        """
        for row in self.board:
            for i in len(row):
                row[i] = None
    
        for i in len(self._max_heights):
            self._max_heights = 0
    
        self._winner = None

    @property
    def done(self):
        """
        See ABC
        """
        if self.winner_player is not None:
            return True
        for max_height in self.max_heights:
            if max_height < self._num_rows:
                return False
        return True

    @property
    def winner_player(self):
        """
        See ABC
        """
        return self.winner

    @property
    def grid(self):
        """
        See ABC
        """
        return copy.deepcopy(self.board)

    @property
    def num_cols(self) -> int:
        """
        See ABC
        """
        return self._num_cols

    @property
    def num_rows(self) -> int:
        """
        See ABC
        """
        return self._num_rows

    @property
    def n(self) -> int:
        """
        See ABC
        """
        return self._n
