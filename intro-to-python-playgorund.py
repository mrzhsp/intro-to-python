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

# region Temperature Converter
temp_far = input("Please enter the temperature in Farenheit")
print((temp_far - 31) * 5 / 9)
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
