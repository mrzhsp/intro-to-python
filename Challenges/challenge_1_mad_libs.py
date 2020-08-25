# Write a story with some words missing
story = """
Roses are {}
Violets are {}
Sugar is {}
And so are you
"""

# Ask the user to provide the missing words
color = input("What color are roses? ")
color2 = input("What color are violets? ")
adjective = input("What do you think about sugar? ")

# Display the final story
print(story.format(color, color2, adjective))

# Or, if in the strings, the keywords are still present, we can use the
#  command below. the orange words should match the keywords in the {} in the
#  story.
story = """
Roses are {color}
Violets are {color2}
Sugar is {adjective}
And so are you
"""
print(story.format(color=color, color2=color2, adjective=adjective))

# Or, even easier, to use f strings. the difference here is to ask for the
# inputs before. So the user should be asked about the inputs before the story
# is defined.
story = f"""
Roses are {color}
Violets are {color2}
Sugar is {adjective}
And so are you
"""
print(story)
