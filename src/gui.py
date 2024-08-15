"""
Code to write a GUI using PyGame
"""
import os
import sys
from typing import Union

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import click

from connectn import ConnectNBase, ConnectN, Player
from bot import Bot

DEFAULT_SIDE = 75
SMALL_SIDE = 40


class GUIPlayer:
    """
    Class for the players' GUI elements
    """

    name: str
    connectn: ConnectNBase
    player: Player

    def __init__(self, n: int, player_type: str, connectn: ConnectNBase,
                 player: Player, opponent: Player):
        self.name = f"Player {n}"
        self.connectn = connectn
        self.player = player
        if player_type == "human":
            self.name = f"Player {n}"
            self.bot = None
        elif player_type == "bot":
            self.name = f"Bot {n}"
            self.bot = Bot(connectn, player, opponent)
        self.connectm = connectn
        self.player = player


def draw_board(surface: pygame.surface.Surface, connectn: ConnectNBase):
    """
    Draws the board on the screen
    """
    grid = connectn.grid
    nrows = connectn.num_rows
    ncols = connectn.num_cols

    width, height = surface.get_size()

    surface.fill((64, 128, 255))

    # Row height and column width
    rh = height // nrows
    cw = width // ncols

    # Borders around each cell
    for row in range(nrows):
        for col in range(ncols):
            rect = (col * cw, row * rh, cw, rh)
            pygame.draw.rect(surface, color=(32, 32, 192),
                             rect=rect, width=2)

    # Circles
    for i, r in enumerate(grid):
        for j, piece_color in enumerate(r):
            if piece_color is None:
                color = (255, 255, 255)
            elif piece_color == Player.RED:
                color = (255, 0, 0)
            elif piece_color == Player.YELLOW:
                color = (255, 255, 0)

            center = (j * cw + cw // 2, i * rh + rh // 2)
            radius = rh // 2 - 8
            pygame.draw.circle(surface, color=color,
                               center=center, radius=radius)


def play_connect_4(connectn: ConnectNBase, players: dict[Player, GUIPlayer],
                   bot_delay: float):
    """
    Opens a PyGame window
    """
    if connectn.num_rows * connectn.num_cols <= 42:
        side = DEFAULT_SIDE
    else:
        side = SMALL_SIDE

    width = side * connectn.num_cols
    height = side * connectn.num_rows

    # Initialize Pygame
    pygame.init()
    pygame.display.set_caption("Connect Four")
    surface = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    # YELLOW starts
    current = players[Player.YELLOW]

    while not connectn.done:
        events = pygame.event.get()
        column = None
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if current.bot is None: 
                if event.type == pygame.KEYUP and connectn.num_cols <= 10:
                    key = event.unicode
                    v = None
                    if key in "123456789":
                        v = int(key) - 1
                    elif key == "0":
                        v = 9

                    if v is not None and connectn.is_allowed(v):
                        column = v
                elif event.type == pygame.MOUSEBUTTONUP:
                    x = event.pos[0]
                    column = x // side

        if current.bot is not None:
            pygame.time.wait(int(bot_delay * 1000))
            column = current.bot.suggest_move()

        if column is not None:
            connectn.execute_move(column, current.player)
            if current.player == Player.YELLOW:
                current = players[Player.RED]
            elif current.player == Player.RED:
                current = players[Player.YELLOW]

        draw_board(surface, connectn)
        pygame.display.update()
        clock.tick(24)

    winner = connectn.winner_player
    if winner is not None:
        print(f"The winner is {players[winner].name}!")
    else:
        print("It's a tie!")

# Command-line interface

@click.command(name="connect4-gui")
@click.option('--rows', type=click.INT, default=6)
@click.option('--cols', type=click.INT, default=7)
@click.option('--n', type=click.INT, default=4)
@click.option('--player1',
              type=click.Choice(['human', 'bot'], case_sensitive=False),
              default="human")
@click.option('--player2',
              type=click.Choice(['human', 'bot'], case_sensitive=False),
              default="human")
@click.option('--bot-delay', type=click.FLOAT, default=0.5)
def cmd(rows: int, cols: int, n: int, player1: str, player2: str, bot_delay: float) -> None:
    connectn = ConnectN(rows, cols, n)

    gui_player1 = GUIPlayer(1, player1, connectn, Player.YELLOW, Player.RED)
    gui_player2 = GUIPlayer(2, player2, connectn, Player.RED, Player.YELLOW)

    players = {Player.YELLOW: gui_player1, Player.RED: gui_player2}

    play_connect_4(connectn, players, bot_delay)

if __name__ == "__main__":
    cmd()
