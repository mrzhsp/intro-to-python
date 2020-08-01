"""
Fill out the functions to calculate the area and circumference of a circle.
Print the result to the user.
"""
import math


def area(r):
    return math.pi * r ** 2


def circumference(r):
    return 2 * math.pi * r


radius = float(input("Circle radius: "))

print('Area: ')  # <-- Call the area function and print the result
print(area(radius))
print('Circumference: ')  # <-- Call the circumference function and print
print(circumference(radius))
