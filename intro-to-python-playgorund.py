"""
Calculate the gravitational force between Earth and Venus
"""
# region Calculate the gravitational force between Earth and Venus
G = 6.67e-11  # This is the Gravitational constant

mass_1 = 6e24  # Mass of earth in kg
mass_2 = 4.9e24  # Mass of Venus in kg
distance = 4.1e10  # Distance between Earth & Venus in m

force = (G * mass_1 * mass_2) / distance ** 2
print(force)
# endregion


