#!/usr/local/bin/ python3
"""Main even programm."""
from brain_games.game_engine import run_game
from brain_games.games import even


def main():
    """Run a user even game."""
    run_game(even)


if __name__ == '__main__':
    main()
