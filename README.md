# Connect 4
This project implements Connect 4 logic and develops a GUI with PyGame. It supports Connect N for any integer N and has an integrated bot to play with.

## How to play
Please make sure to have PyGame installed. If it is not already, type `pip install pygame` into the terminal.

The default is two players playing Connect 4. The standard board is the same as the physical game, 7 columns x 6 rows. From the terminal command line, to play, after downloading the code, run `python3 src/gui.py`.

The game is set up as Connect N, meaning that players could play Connect 5 or Connect 10. If you'd like to play, say, Connect 7, you can run `python3 src/gui.py --n=7`. To change the number of rows or columns add `--rows=X` or `cols=Y`.

#### Bot
If you'd like to play against the bot, you can choose for either player 1 or player 2 to be the bot. In the command line, `python3 src/gui.py --player2=bot` makes the red player a bot. This bot first checks if it has any winning moves. If not, then it sees if it can block the opponent from winning. Otherwise, it plays a move at random.
