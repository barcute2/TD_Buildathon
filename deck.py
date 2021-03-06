
from random import shuffle

class Deck(object):
	"""docstring for Deck"""
	def __init__(self):
		super(Deck, self).__init__()
		self.deck = []

# Adds a card into the deck
	def add_card(card):
		self.deck.append(card)

# Draws card from deck and returns it
	def draw_card():
		return self.deck.pop()

# Shuffles the positions of all the cards in the deck
	def shuffle():
		shuffle(self.deck)

		