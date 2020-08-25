"""
Number guessing game
The number to guess will be from 1 to 20 (inclusive).
The user will have 4 guesses to guess the number correctly.
After each wrong guess, the user will be told whether to
guess higher or lower next time.
If the user doesn't win, tell them the number.
"""
import random


# region My code
# def run_game():
#     answer = random.randint(1, 20)
#
#     print("I'm thinking of a number between 1 and 20")
#
#     guess = int(input("Guess a number: "))
#     if guess == answer:
#         print("Congratulations! you guessed it right.")
#     # Otherwise, tell them if the answer is higher or lower than their guess
#     elif guess < answer:
#         print("The answer is higher than {}.".format(guess))
#         print("You can guess again")
#         guess = int(input("Guess a number: "))
#         if guess == answer:
#             print("Congratulations! you guessed it right.")
#         elif guess < answer:
#             print("The answer is higher than {}.".format(guess))
#             print("You can guess again")
#             guess = int(input("Guess a number: "))
#         else:
#             print("The answer is lower than {}.".format(guess))
#             print("You can guess again")
#             guess = int(input("Guess a number: "))
#     else:
#         print("The answer is lower than {}.".format(guess))
#         print("You can guess again")
#         guess = int(input("Guess a number: "))
#         if guess == answer:
#             print("Congratulations! you guessed it right.")
#         elif guess < answer:
#             print("The answer is higher than {}.".format(guess))
#             print("You can guess again")
#             guess = int(input("Guess a number: "))
#         else:
#             print("The answer is lower than {}.".format(guess))
#             print("You can guess again")
#             guess = int(input("Guess a number: "))
#     print('The number was {}.'.format(answer))
# endregion

# region Correct Answer
def run_game():
    answer = random.randint(1, 20)

    print("I'm thinking of a number between 1 and 20.")

    guess1 = int(input("Guess a number: "))

    if guess1 == answer:
        print("Congratulations! You guessed correctly.")
        return
    elif guess1 < answer:
        print("Guess higher!")
        print("You can guess again.")
    else:
        print("Guess lower!")
        print("You can guess again.")

    guess2 = int(input("Guess a number: "))

    if guess2 == answer:
        print("Congratulations! You guessed correctly.")
        return
    elif guess2 < answer:
        print("Guess higher!")
        print("You can guess again.")
    else:
        print("Guess lower!")
        print("You can guess again.")

    guess3 = int(input("Guess a number: "))

    if guess3 == answer:
        print("Congratulations! You guessed correctly.")
        return
    elif guess3 < answer:
        print("Guess higher!")
    else:
        print("Guess lower!")
    print("You lost. The number was {}.".format(answer))
    return


# endregion

run_game()
