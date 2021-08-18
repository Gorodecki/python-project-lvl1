#!/usr/local/bin/ python3
"""Main even programm."""
from brain_games.game_engine import run
from brain_games.games import prime


def main():
    """Run a user even game."""
    run(prime)


if __name__ == '__main__':
    main()
