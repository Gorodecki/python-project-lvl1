"""Question collection interface for brain-games."""

import random

import prompt


def even_or_odd(number: int) -> bool:
    """Check number even or odd.

    Parameters:
        number (int): number

    Returns:
        bool: True if even; False if odd.
    """
    return bool(number % 2 == 0)


def ask_even_number() -> bool:
    """Ask yes/no question about even number.

    Returns:
        bool: True if correct answer; False - wrong answer.
    """
    number = random.randint(1, 1000)
    answer = prompt.string('Question: {0}\nYour answer: '.format(number))
    if (answer == 'yes') and (even_or_odd(number)):
        return True
    elif (answer == 'no') and (not even_or_odd(number)):
        return True

    return False


def even_games(name: str):
    """Logical even-odd function.

    Args:
        name (str): username
    """
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    for _ in range(3):
        answer = ask_even_number()
        if answer:
            print('Correct!')
        else:
            print("'yes' is wrong answer; (. Correct answer was 'no'.")
            print("Let's try again, {0}!".format(name))
            break
    else:
        print('Congratulations, {0}!'.format(name))
