"""Question collection interface for brain-games."""
from random import randint

INFORMATION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_prime(num: int) -> bool:
    """Check number prime.

    Parameters:
        num (int): number

    Returns:
        bool: True if prime; False if otherwise.
    """
    return num > 1 and all(num % phi for phi in range(2, int(num**0.5) + 1))


def generate_question_and_answer():
    """Generate question and answer for game.

    Returns:
        question (str): Question for every game.
        correct_answer (str): Answer for every game
    """
    number = randint(1, 1000)

    question = str(number)
    correct_answer = 'yes' if check_prime(number) else 'no'

    return question, correct_answer
