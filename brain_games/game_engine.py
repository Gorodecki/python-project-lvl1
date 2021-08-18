"""Main interface for all game."""
import prompt

ROUNDS_COUNT = 3  # number of correct answers to finish the game


def run(game):
    """Logical for all games.

    Args:
        game (str): type of games
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    print(game.GREETING)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.generate_question_and_answer()

        print('Question: {0}'.format(question))
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
        else:
            print("'{0}' is wrong answer ;(.".format(answer), end=' ')
            print("Correct answer was '{0}'.".format(correct_answer))
            print("Let\'s try again, {0}!".format(user_name))
            return

    print('Congratulations, {0}!'.format(user_name))
