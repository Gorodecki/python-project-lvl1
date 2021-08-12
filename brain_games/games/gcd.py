"""Question collection interface for brain-games."""
from random import randint

GREETING = 'Find the greatest common divisor of given numbers.'


def gcd(one: int, two: int) -> int:
    """Find gcd.

    Args:
        one (int): first number
        two (int): second number

    Returns:
        int: result
    """
    while two:
        one, two = two, one % two
    return one


def generate_question_and_answer() -> tuple:
    """Generate question and answer for game.

    Returns:
        question (str): Question for every game.
        correct_answer (str): Answer for every game
    """
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    correct_answer = gcd(number1, number2)

    question = '{0} {1}'.format(number1, number2)
    correct_answer = str(correct_answer)

    return question, correct_answer
