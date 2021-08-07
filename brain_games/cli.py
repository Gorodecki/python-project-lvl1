"""Command line interface for brain-games."""


import prompt


def welcome_user() -> str:
    """Question username.

    Returns:
        name (str): username
    """
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print('Hello, {0}!'.format(name))
    return name
