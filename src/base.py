"""
Abstract Base Class for Connect N
"""
from abc import ABC, abstractmethod
from enum import Enum

class Player(Enum):
    """
    Connect N supports 2 players
    """
    RED: int = 1
    YELLOW: int = 2

class ConnectNBase(ABC):
    """
    Base class with key methods
    """
    _num_rows: int
    _num_cols: int
    _n: int

    def __init__(self, num_rows: int, num_cols: int, n: int):
        if num_rows < n or num_cols < n:
            raise ValueError(f"{n} columns maximum to play Connect {n}")

        self._num_rows = num_rows
        self._num_cols = num_cols
        self._n = n

    @abstractmethod
    def piece_loc(self, row: int, col: int, player: Player):
        """
        Returns the player, if any, at a specified location on the board
        """
        raise NotImplementedError

    @abstractmethod
    def execute_move(self, col: int, player: Player):
        """
        Places a piece on the board and checks if it is a winner
        """
        raise NotImplementedError

    @abstractmethod
    def is_allowed(self, col: int, player: Player):
        """
        Checks if a move is legal
        """
        raise NotImplementedError

    @abstractmethod
    def is_winner(self, col: int, player: Player):
        """
        Returns a boolean if the player is the winner
        """
        raise NotImplementedError

    @abstractmethod
    def new_game(self):
        """
        Erases the board
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def done(self) -> bool:
        """
        Checks if there is a winner or if the board is full
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def winner_player(self) -> Player:
        """
        Returns the winning player
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def grid(self):
        """
        Copies the grid for hypothetical manipulations
        """
        raise NotImplementedError

    @property
    def num_cols(self) -> int:
        """
        Getter for number of columns
        """
        return self._num_cols

    @property
    def num_rows(self) -> int:
        """
        Getter for number of rows
        """
        return self._num_rows

    @property
    def n(self) -> int:
        """
        Getter for N in ConnectN (how many in a row to win)
        """
        return self._n
