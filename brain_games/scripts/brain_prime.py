#!/usr/local/bin/ python3
"""Main even programm."""
from brain_games.games import prime
from brain_games.play_game import run_game


def main():
    """Run a user even game."""
    run_game(prime)


if __name__ == '__main__':
    main()
