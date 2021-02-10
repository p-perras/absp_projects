#! python3
# myMultiplicationQuiz.py
# ABSP - Chapter 8

import pyinputplus as pyip
import random
import time


def multplication_quiz(questions):
    """
    Poses a number of multiplication problems to the user.

    Args:
        questions (int): Number of questions to pose.
    """
    correct_anwsers = 0

    for question_number in range(1, questions):
        # Pick two random numbers
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        prompt = f'Question #{question_number}: {num1} x {num2} = '

        try:
            # Right answers are handled by allowRegexes.
            # Wrong answers are handled by blockRegexes, with a custom message.
            pyip.inputStr(prompt, 
            allowRegexes=[f'^{num1 * num2}$'], 
            blockRegexes=[('.*', 'Incorrect')], 
            timeout=8, limit=3)
        except pyip.TimeoutException:
            print('Out of Time!')
        except pyip.RetryLimitException:
            print('Out of tries!')
        else:
            # This block runs if no exceptions were raised in the try block.
            print('Correct!')
            correct_anwsers += 1
            # Brief pause to let the user read the message
            time.sleep(1) 
    print(f'Your Score is {correct_anwsers} / {questions}')


if __name__ == '__main__':

    numOfQuestions = 5
    multplication_quiz(numOfQuestions)