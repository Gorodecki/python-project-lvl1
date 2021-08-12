"""Question collection interface for brain-games."""
from random import randint

GREETING = 'Answer "yes" if number even otherwise answer "no".'


def even_or_odd(number: int) -> bool:
    """Check number even or odd.

    Parameters:
        number (int): number

    Returns:
        bool: True if even; False if odd.
    """
    return number % 2 == 0


def generate_question_and_answer() -> tuple:
    """Generate question and answer for game.

    Returns:
        question (str): Question for every game.
        correct_answer (str): Answer for every game
    """
    number = randint(1, 1000)

    question = str(number)
    correct_answer = 'yes' if even_or_odd(number) else 'no'

    return question, correct_answer
