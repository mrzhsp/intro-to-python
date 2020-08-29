words = ['account', 'addition', 'adjustment', 'advertisement', 'agreement',
         'amount', 'amusement', 'animal', 'answer', 'apparatus', 'approval',
         'argument', 'attack', 'attempt', 'attention', 'attraction',
         'authority', 'balance', 'behavior', 'belief', 'breath', 'brother',
         'building', 'business', 'butter', 'canvas', 'chance', 'change',
         'comfort', 'committee', 'company', 'comparison', 'competition',
         'condition', 'connection', 'control', 'copper', 'cotton', 'country',
         'credit', 'current', 'damage', 'danger', 'daughter', 'decision',
         'degree', 'design', 'desire', 'destruction', 'detail', 'development',
         'digestion', 'direction', 'discovery', 'discussion', 'disease',
         'disgust', 'distance', 'distribution', 'division', 'driving',
         'education', 'effect', 'example', 'exchange', 'existence', 'expansion',
         'experience', 'expert', 'family', 'father', 'feeling', 'fiction',
         'flight', 'flower', 'friend', 'government', 'growth', 'harbor',
         'harmony', 'hearing', 'history', 'impulse', 'increase', 'industry',
         'insect', 'instrument', 'insurance', 'interest', 'invention',
         'journey', 'knowledge', 'language', 'learning', 'leather', 'letter',
         'liquid', 'machine', 'manager', 'market', 'measure', 'meeting',
         'memory', 'middle', 'minute', 'morning', 'mother', 'motion',
         'mountain', 'nation', 'number', 'observation', 'operation', 'opinion',
         'organisation', 'ornament', 'payment', 'person', 'pleasure', 'poison',
         'polish', 'porter', 'position', 'powder', 'process', 'produce',
         'profit', 'property', 'protest', 'punishment', 'purpose', 'quality',
         'question', 'reaction', 'reading', 'reason', 'record', 'regret',
         'relation', 'religion', 'representative', 'request', 'respect',
         'reward', 'rhythm', 'science', 'secretary', 'selection', 'servant',
         'silver', 'sister', 'sneeze', 'society', 'statement', 'stitch',
         'stretch', 'structure', 'substance', 'suggestion', 'summer', 'support',
         'surprise', 'system', 'teaching', 'tendency', 'theory', 'thought',
         'thunder', 'transport', 'trouble', 'vessel', 'weather', 'weight',
         'winter', 'writing']
hard_words = ['Awkward', 'Bagpipes', 'Banjo', 'Bungler', 'Croquet', 'Crypt',
              'Dwarves', 'Fervid', 'Fishhook', 'Fjord', 'Gazebo', 'Gypsy',
              'Haiku', 'Haphazard', 'Hyphen', 'Ivory', 'Jazzy', 'Jiffy', 'Jinx',
              'Jukebox', 'Kayak', 'Kiosk', 'Klutz', 'Memento', 'Mystify',
              'Numbskull', 'Ostracize', 'Oxygen', 'Pajama', 'Phlegm', 'Pixel',
              'Polka', 'Quad', 'Quip', 'Rhythmic', 'Rogue', 'Sphinx', 'Squawk',
              'Swivel', 'Toady', 'Twelfth', 'Unzip', 'Waxy', 'Wildebeest',
              'Yacht', 'Zealous', 'Zigzag', 'Zippy', 'Zombie']

"""
Word guessing game (hangman)
Choose a word for the user to guess.
The user can have 6 wrong guesses before they lose the game.
After each guess, display the correct guesses, the wrong guesses,
and the number of wrong guesses left.
If the user doesn't win, tell them the answer.
"""
import random


# region My Code.
# def word_game():
#     answer = random.choice(words)
#     print('I am thinking of a word.')
#     # I need to tell the player that how many character there is in this
#     # word. Also, I have to tell the player of the index of positions,
#     # which is one less than the number of letters in python.
#     print(f'This word has {len(answer)} letters in it, with positions of 0 to '
#           f'{len(answer) - 1}')
#
#     num_guesses = 6
#     for num_guess in range(num_guesses):
#         print(f'You have {num_guesses} guesses left')
#         # The input is given.
#         guess_letter = input('Guess 1 letter from "a" to "z": ')
#         # The number of guesses will be adjusted after each play.
#         num_guesses -= 1
#
#         # This chunk of code is for counting the number of repetitive letters
#         # if any.
#         if guess_letter in answer:
#             count = 0
#             for letter in answer:
#                 if letter == guess_letter:
#                     count = count + 1
#             print(f'Yep, there is {count} "{guess_letter}" in this word, '
#                   f'in positions:')
#             # This code is for reporting the indexes in which the guessed
#             # letter exists. If it is repetitive, it will give the position
#             # of all indexes.
#             print([pos for pos, char in enumerate(answer) if char ==
#                    guess_letter])
#             # Here, the player has the opportunity to guess the whole word.
#             guess_word = input('Now you can guess the word: ')
#
#             # This chunk is for determining if the guess of the word is
#             # correct.
#             if guess_word == answer:
#                 print('congratulation! You won.')
#                 return
#             elif num_guesses == 0:
#                 break
#             else:
#                 print('Nope. You guessed incorrectly.')
#         # This is the remaining logic, if the player guessed the letter
#         # incorrectly.
#         else:
#             print(f'There is no "{guess_letter}" in this word. Guess another '
#                   f'letter.')
#     # This will give the ending of the game, if the player makes all guesses
#     # incorrectly.
#     print("You lost. The correct word was {}.".format(answer))
#     return
# word_game()
# endregion

# region Correct Answer
def word_game1():
    # Pick a random word (test word is "hello")
    answer = random.choice(words)
    num_wrong_guesses_left = 6
    guessed_letters = []

    while num_wrong_guesses_left > 0:
        # Display to user "_ _ _ _ _".
        #    If we run it, we will see that there is an extra space at the end.
        #    To remove the extra space, we can use "display_word.strip()". This
        #    command will remove extra spaces in the beginning and the end of
        #    the word.
        display_word = ''
        for letter in answer:
            # We want to put the correct letters in place of "_". We can do
            # it by displaying the correct guess on the answer! Since this is
            # a loop, it goes over all letters in the answer. If the letter
            # is already guessed, it will show it. Else, it will replace it
            # with "_".
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += '_'
            display_word += ' '
        print(display_word.strip())
        # Display the number of wrong guess they have left (6)
        print(f'{num_wrong_guesses_left} wrong guesses left')
        print(f'you have guessed: "{guessed_letters}"')

        # Guess a letter
        guess = input('Guess a letter: ')
        guessed_letters.append(guess)

        # If letter is in word
        if guess in answer:
            print('Correct! :)')
        else:
            print("Nope! :(")
            num_wrong_guesses_left -= 1

        # Check if they won
        won = True
        for letter in answer:
            if letter not in guessed_letters:
                won = False
                break
        if won:
            print('You won!')
            return
    print("You lost!")
    print(f'The answer was {answer}')

        # You lost, exit


word_game1()
# endregion
