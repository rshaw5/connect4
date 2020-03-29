import numpy as np
import sys

class gameVariables:
    def __init__(self):
        self.board = create_board()
        self.gameOver = False
        self.turnNumber = 1
        self.currentPlayer = 1

def create_board():
    board = np.zeros((6,7))
    return board

def prompt_player(player):
    print(f"Player {player}, make your selection (1-7):")

def game_loop_step(gameVariables):
    if gameVariables.gameOver:
        sys.exit(0)

    prompt_player(gameVariables.currentPlayer)
    gameVariables.currentPlayer = (gameVariables.turnNumber % 2) + 1
    gameVariables.turnNumber += 1

def main():
    game = gameVariables()

if __name__ == '__main__':
    main()