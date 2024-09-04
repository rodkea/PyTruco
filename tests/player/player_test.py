import unittest
from truco import  Card, Suit, Rank, Hand, EmptyHandError, Player


class TestHand(unittest.TestCase):
    def setUp(self):
        """Create a hand with a maximum of 3 cards for testing."""
        self.hand = Hand(max_cards=3)
        self.card1 = Card(Rank.ONE, Suit.BASTO)
        self.card2 = Card(Rank.TWO, Suit.COPA)
    
    def test_initial_hand(self):
        """Test that a newly created hand is empty."""
        self.assertEqual(len(self.hand), 0)
    
    def test_add_card(self):
        """Test adding a card to the hand."""
        self.hand.add_card(self.card1)
        self.assertEqual(len(self.hand), 1)
        self.assertIn(self.card1, self.hand.cards)
    
    def test_add_card_exceed_max(self):
        """Test that adding more cards than the maximum allowed raises a ValueError."""
        self.hand.add_card(self.card1)
        self.hand.add_card(self.card2)
        self.hand.add_card(self.card1)  # Adding the same card again for testing
        with self.assertRaises(ValueError):
            self.hand.add_card(self.card2)
    
    def test_clear_hand(self):
        """Test clearing the hand."""
        self.hand.add_card(self.card1)
        self.hand.clear()
        self.assertEqual(len(self.hand), 0)
    
    def test_play_card(self):
        """Test playing a card from the hand."""
        self.hand.add_card(self.card1)
        card_played = self.hand.play_card(self.card1)
        self.assertEqual(card_played, self.card1)
        self.assertEqual(len(self.hand), 0)
    
    def test_play_card_not_in_hand(self):
        """Test that playing a card not in the hand raises a ValueError."""
        with self.assertRaises(ValueError):
            self.hand.play_card(self.card1)
            
class TestPlayer(unittest.TestCase):
    def setUp(self):
        """Create a player and some cards for testing."""
        self.player = Player(name="Test Player")
        self.card1 = Card(Rank.ONE, Suit.BASTO)
        self.card2 = Card(Rank.TWO, Suit.COPA)
    
    def test_draw_card(self):
        """Test drawing a card and adding it to the player's hand."""
        self.player.draw_card(self.card1)
        self.assertIn(self.card1, self.player.hand)
    
    def test_play_card(self):
        """Test playing a card from the player's hand."""
        self.player.draw_card(self.card1)
        card_played = self.player.play_card(self.card1)
        self.assertEqual(card_played, self.card1)
        self.assertNotIn(self.card1, self.player.hand)
    
    def test_play_card_empty_hand(self):
        """Test that playing a card from an empty hand raises EmptyHandError."""
        with self.assertRaises(EmptyHandError):
            self.player.play_card(self.card1)
    
    def test_clear_hand(self):
        """Test clearing the player's hand."""
        self.player.draw_card(self.card1)
        self.player.clear_hand()
        self.assertEqual(len(self.player.hand), 0)