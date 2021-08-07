#!/usr/local/bin/python3.9
"""Main even programm."""


from brain_games.cli import welcome_user
from brain_games.question import even_games


def main():
    """Make a user even game intreface."""
    name = welcome_user()  # get username
    even_games(name)  # ask question


if __name__ == '__main__':
    main()
