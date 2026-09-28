# ------------------------------------------------------
# Practical No: 5 (b)
# Aim: To create a deck of cards and shuffle it using Python.
# ------------------------------------------------------

# Theory:
# A standard deck of playing cards has 52 cards: 4 suits (Hearts,
# Diamonds, Clubs, Spades) each having 13 ranks (2 to 10, Jack, Queen,
# King, Ace). The random module's shuffle() function is used to
# rearrange the cards randomly, giving every card an equal chance of
# appearing in any position.

# Algorithm:
# 1. Start
# 2. Create a list of all 52 cards using the 4 suits and 13 ranks
# 3. Print the first few cards of the ordered deck
# 4. Shuffle the deck using random.shuffle()
# 5. Print the first few cards of the shuffled deck and deal a hand
# 6. Stop

# Python Program:

import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

deck = []
for suit in suits:
    for rank in ranks:
        deck.append(rank + " of " + suit)

print("Total cards in deck:", len(deck))
print("First 5 cards (ordered):", deck[0:5])

random.shuffle(deck)
print("First 5 cards (shuffled):", deck[0:5])

player_hand = deck[0:5]
print("Cards dealt to player:", player_hand)

# Sample Input / Output:
# Total cards in deck: 52
# First 5 cards (ordered): ['2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts']
# First 5 cards (shuffled): ['King of Clubs', '7 of Spades', 'Ace of Hearts', '10 of Diamonds', '4 of Clubs']
# Cards dealt to player: ['King of Clubs', '7 of Spades', 'Ace of Hearts', '10 of Diamonds', '4 of Clubs']

# Result:
# The program to create and shuffle a deck of cards was executed
# successfully and the output was verified.
# (Note: shuffled output will vary on every run.)

# Viva Questions:
# 1. How many cards are there in a standard deck?
# 2. Which Python module provides the shuffle() function?
# 3. Why does the shuffled output change every time the program runs?
# 4. How would you deal a hand of cards to more than one player?
# 5. What is the difference between random.shuffle() and random.sample()?
