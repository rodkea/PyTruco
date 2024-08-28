import unittest
from truco.decks import DeckType, SpanishDeck, Card


class TestSpanishDeck(unittest.TestCase):
        
  def test_full_deck_initialization(self):
    deck = SpanishDeck(deck_type=DeckType.FULL)
    self.assertEqual(len(deck._cards), 48)  # 12 ranks * 4 suits
    
    # Checks if all cards are presents in the deck
    ranks = SpanishDeck.all_ranks
    suits = SpanishDeck.suits
    expected_cards = [Card(rank, suit) for suit in suits for rank in ranks]
      
    for card in expected_cards:
        self.assertIn(card, deck._cards)
  
  def test_reduced_deck_initialization(self):
    deck = SpanishDeck(deck_type=DeckType.REDUCED)
    self.assertEqual(len(deck._cards), 40)  # 10 ranks * 4 suits
    
    # Checks if all cards are presents in the deck
    ranks = SpanishDeck.reduced_ranks
    suits = SpanishDeck.suits
    expected_cards = [Card(rank, suit) for suit in suits for rank in ranks]
    
    for card in expected_cards:
        self.assertIn(card, deck._cards)
  
  def test_invalid_deck_type(self):
    with self.assertRaises(ValueError):
        SpanishDeck(deck_type='invalid')
  
  def test_pop_cards(self):
    # Checks that the deck if empty after poping all the cards from reduced deck
    deck = SpanishDeck(deck_type=DeckType.REDUCED)
    for _ in range(40):
      deck.pop()
    self.assertEqual(len(deck), 0)
    # Checks that raise IndexError on poping empty deck
    deck = SpanishDeck(deck_type=DeckType.REDUCED)
    for _ in range(40):
      deck.pop()
    with self.assertRaises(IndexError):
      deck.pop()
    # Checks that the deck if empty after poping all the cards from full deck
    deck = SpanishDeck(deck_type=DeckType.FULL)
    for _ in range(48):
      deck.pop()
    self.assertEqual(len(deck), 0)
    # Checks that raise IndexError on poping empty deck
    deck = SpanishDeck(deck_type=DeckType.FULL)
    for _ in range(48):
      deck.pop()
    with self.assertRaises(IndexError):
      deck.pop()
    
    
    
if __name__ == '__main__':
  unittest.main()