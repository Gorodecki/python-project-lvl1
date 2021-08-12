#!/usr/local/bin/ python3
"""Main calc programm."""
from brain_games.game_engine import run_game
from brain_games.games import progression


def main():
    """Run a user calc game."""
    run_game(progression)


if __name__ == '__main__':
    main()
