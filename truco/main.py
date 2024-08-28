from decks import SpanishDeck, DeckType
from player import Player, Hand
if __name__ == '__main__':
  deck = SpanishDeck(DeckType.REDUCED)
  hand = Hand()
  hand.add_card(deck.pop())
  hand.add_card(deck.pop())
  hand.add_card(deck.pop())
  