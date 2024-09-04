import unittest
from truco import Card, Suit, Rank, RankReduced


class TestCard(unittest.TestCase):
  
  def test_card_initialization(self):
    """Test that a Card can be correctly initialized with valid rank and suit."""
    card = Card(Rank.ONE, Suit.BASTO)
    self.assertEqual(card.rank, 1)
    self.assertEqual(card.suit, 'basto')
        
  def test_card_equality(self):
    """Test that two Cards with the same rank and suit are considered equal."""
    card1 = Card(Rank.TWO, Suit.COPA)
    card2 = Card(Rank.TWO, Suit.COPA)
    card3 = Card(Rank.THREE, Suit.ESPADA)
    self.assertEqual(card1, card2)
    self.assertNotEqual(card1, card3)
  
  def test_invalid_rank_type(self):
    """Test that initializing a Card with an invalid rank type raises a TypeError."""
    with self.assertRaises(TypeError):
        Card('TEN', Suit.BASTO)
  
  def test_invalid_suit_type(self):
    """Test that initializing a Card with an invalid suit type raises a TypeError."""
    with self.assertRaises(TypeError):
        Card(Rank.TEN, 'basto')

  def test_rank_reduced(self):
    """Test that a Card can be initialized with RankReduced and correctly returns rank and suit."""
    card = Card(RankReduced.TEN, Suit.COPA)
    self.assertEqual(card.rank, 10)
    self.assertEqual(card.suit, 'copa')

  def test_invalid_rank_type_in_rank_reduced(self):
    """Test that initializing a Card with an invalid rank type from RankReduced raises a TypeError."""
    with self.assertRaises(TypeError):
        Card('TEN', Suit.BASTO)

  def test_invalid_suit_type_in_rank_reduced(self):
    """Test that initializing a Card with an invalid suit type from RankReduced raises a TypeError."""
    with self.assertRaises(TypeError):
        Card(Rank.TEN, 'basto')
      