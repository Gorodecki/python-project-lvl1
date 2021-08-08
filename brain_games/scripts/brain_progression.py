#!/usr/local/bin/ python3
"""Main calc programm."""
from brain_games.games import progression
from brain_games.play_game import run_game


def main():
    """Run a user calc game."""
    run_game(progression)


if __name__ == '__main__':
    main()
