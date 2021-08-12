"""Question collection interface for brain-games."""
from operator import add, mul, sub
from random import choice, randint

GREETING = 'What is the result of the expression?'


def generate_question_and_answer() -> tuple:
    """Generate question and answer for game.

    Returns:
        question (str): Question for every game.
        correct_answer (str): Answer for every game
    """
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    operator = choice('-+*')

    if operator == '+':
        correct_answer = add(number1, number2)
    elif operator == '-':
        correct_answer = sub(number1, number2)
    elif operator == '*':
        correct_answer = mul(number1, number2)

    question = '{0} {1} {2}'.format(number1, operator, number2)
    correct_answer = str(correct_answer)

    return question, correct_answer
