# region Calculate the gravitational force between Earth and Venus
G = 6.67e-11  # This is the Gravitational constant

mass_1 = 6e24  # Mass of earth in kg
mass_2 = 4.9e24  # Mass of Venus in kg
distance = 4.1e10  # Distance between Earth & Venus in m

force = (G * mass_1 * mass_2) / distance ** 2
print(force)
# endregion

# region Names that we cannot use in Python
"""
Flase - class - finally - is - return - None - continue - for - lambda - try 
- True - def - from - nonlocal - while - and - del - global - not - with - as - 
elif - if - or - yield - assert - else - import - pass - break - except - in 
- raise
"""
# We cannot also use Built-in-Functions as names. The list is available here:
# https://docs.python.org/3.6/library/functions.html
# endregion

# region Sing Happy Birthday
name = input("Please enter your name")
print("Happy birthday to you")
print("Happy birthday to you")
print("Happy birthday dear " + name)
print("Happy birthday to you")
# endregion

# region Manipulate Strings
greeting = "Hello there"
greeting.capitalize()
greeting.title()
greeting.count("l")  # count the number of a certain letter
greeting.count("h")
greeting.count("H")
greeting.lower().count("h")  # First turn everything to lower, then count
greeting.find(" ")  # Find the location/index of the letter
greeting.find("x")  # This returns -1 which means there is no "x".
# endregion

# region Adding strings and stuff together
animal = "cow"
animal_sound = "mow"
"The " + animal + " says " + animal_sound.upper()

# We can do this in another way. The format use the values to put in {}.
"The {} says {}".format(animal, animal_sound.upper())
"The {0} says {1}".format(animal, animal_sound)
"The {a} says {b}".format(a=animal, b=animal_sound)
f"The {animal} says {animal_sound.upper()}"  # This is even easier!
# In this mode, anything in the "" will be treated as strings. Things in {}
#   will reference a variable that already exists.
# endregion

# region Problem Solving like a Programmer
#   Step 1: Understand the problem
#   Step 2: Break it down into smaller problems
#   Step 3: Write it down using computer logic
#           If, Else, Not, Or, And
#   Step 4: Translate to code
# endregion

# region True/False statements
fruit1 = "apples"
fruit2 = "oranges"
fruit1 == fruit2
fruit1 != fruit2
fruit1.isnumeric()
fruit1.isalpha()
1 < 2 and 1 < 3
1 < 2 or 1 / 0 == 0
'n' in "Nasa"
'n' in "navegante"
# endregion

# region Conditional "if" statements
hungry = False
water_temp = -1

if hungry:
    print("Go eat something")
    print("Maybe a banana")
elif water_temp < 0:
    print("Maybe a cup of warm tea!")
else:
    print("Then get away from the fridge!")
print("Continue with your life")

water_temp = 0

if water_temp < 0:
    print("It's too cold")
elif water_temp > 100:
    print("It's too warm")
else:
    print("It's ok to drink water")

"""
This code should get the user to guess a random number between 1 and 10.
If the user is right, congratulate them.
If they're wrong, say if the answer is higher or lower.
Then say what the answer was.
"""
import random

answer = random.randint(1, 10)

guess = int(input("I'm thinking of a number between 1 and 10: "))

# If the number is correct, tell the user
if guess == answer:
    print("Congratulations! you guessed it right.")
# Otherwise, tell them if the answer is higher or lower than their guess
elif guess < answer:
    print("The answer is higher than {}.".format(guess))
else:
    print("The answer is lower than {}.".format(guess))
print('The number was {}.'.format(answer))
# endregion

# region Playing with While Loops
"""
One important aspect of looping is the order of elements we want to happen. 
For example, it is important to see when we want to add an item and then print.
"""

x = 0
while x < 20:
    x = x + 1
    if x % 2 == 1:
        continue
        # With this condition and continue, it will skip the remaining parts.
        # Go back to the loop and continue.
    print(x)
    if x == 8:
        break
print("Stopped looping")

# endregion

# region Create and Manipulate lists
cities = ['Melbourne', 'Vienna', 'Vancouver', 'Toronto', 'Calgary']
print(cities)
print(f'The top {len(cities)} most livable cities:')
print(cities[0])
print(cities[-1])  # This would give Vancouver again because it can count
# backwards.
print(cities[1:4])  # The important point is that this function does not
# include the 4th element. So it does not give the Calgary!!!
print(cities[:3])
print(cities[3:])
print(cities[::1])  # This will give the elements with 1 distance.
print(cities[::2])  # This wil give every two elements.
print(cities[::-1])  # It can also go in reverse.
cities.append('Rotterdam')  # This will add an item to the list.
cities.remove('Rotterdam')
cities.pop()  # This will remove the last item from the list.
cities.sort()  # Sort alphatecially.
# Press command and click on a function.
help(cities)
cities[1] = 'Osaka'
cities.insert(0, 'Amsterdam')
cities.insert(0, True)
cities.insert(0, [1, 2, 3])  # We can add anything to the list.
# endregion

# region Loop over Lists with For Loops
cities = ['Melbourne', 'Vienna', 'Vancouver', 'Toronto', 'Calgary']

for city in cities:
    print(city)
# range(): creates a list of numbers from a starting point to an end point
# with pre-defined increments.

for number in range(5):
    print(number)

for number in range(5, 10):
    print(number)

for number in range(5, 100, 2):
    print(number)

word = input('Type a word: ')
num_vowels = 0
for letter in word.lower():
    if letter in ['a', 'e', 'i', 'o', 'u']:
        num_vowels += 1
print(f'There are {num_vowels} vowels in {word}')
# endregion







