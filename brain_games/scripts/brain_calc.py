#!/usr/local/bin/ python3
"""Main calc programm."""
from brain_games.game_engine import run
from brain_games.games import calc


def main():
    """Run a user calc game."""
    run(calc)


if __name__ == '__main__':
    main()
