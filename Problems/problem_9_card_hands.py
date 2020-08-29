"""
Deal a hand of 5 cards
"""
import random
suits = ['♠︎', '♣︎', '♥︎', '♦︎']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# First define the list of cards that we want.
cards = []
# This is the first loop for suits to be added to values.
for suit in suits:
    # This is the second loop for going through values.
    for value in values:
        # Here, use "append" to add the suits to values. It ends up
        # with 52 cards.
        cards.append(suit + value)
print(cards)
# print(len(cards))

# Here I added a twist. This will provide 5 deals with 5 cards in each deal.
num_deal = 0
for num_deal in range(5):
    hand = []
    for n in range(5):
        # By a random choice, choose 5 cards.
        card = random.choice(cards)
        # Remove the chosen card from the set.
        cards.remove(card)
        # Add the card to the list.
        hand.append(card)
    print(f'This is your deal 1: "{hand}"')
    num_deal += 1

# I have found something more interesting. If we want to see what is going to
# happen in each step of card giving of each deal we can use this code below:
num_deal = 0
for num_deal in range(5):
    hand = []
    for n in range(5):
        card = random.choice(cards)
        cards.remove(card)
        hand.append(card)
        print(f'This is your deal 1: "{hand}"')
    num_deal += 1

