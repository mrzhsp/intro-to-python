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
