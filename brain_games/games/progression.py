"""Question collection interface for brain-games."""
from random import randint

GREETING = 'What number is missing in the progression?'
PROGRESSION_LENGHT = 10


def generate_question_and_answer() -> tuple[str, str]:
    """Generate question and answer for game.

    Returns:
        question (str): Question for every game.
        correct_answer (str): Answer for every game
    """
    start_num = randint(1, 100)
    step = randint(1, 10)
    last_num = PROGRESSION_LENGHT * step + start_num

    progression = list(range(start_num, last_num, step))

    random_choice = randint(0, PROGRESSION_LENGHT - 1)  # get ind from 0 to 9
    correct_answer = str(progression[random_choice])
    # mask one number
    progression[random_choice] = '..'
    question = ' '.join(str(number) for number in progression)

    return question, correct_answer
