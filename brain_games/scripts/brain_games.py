#!/usr/local/bin/python3.9
"""Main programm."""


from brain_games.cli import welcome_user


def main():
    """Make a user game intreface."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
