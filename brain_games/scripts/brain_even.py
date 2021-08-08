#!/usr/local/bin/ python3
"""Main even programm."""
from brain_games.games import even
from brain_games.play_game import run_game


def main():
    """Run a user even game."""
    run_game(even)


if __name__ == '__main__':
    main()
