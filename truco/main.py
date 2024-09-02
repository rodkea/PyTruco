from decks import SpanishDeck, DeckType, Card
from player import Player, Hand
if __name__ == '__main__':
  deck = SpanishDeck(DeckType.REDUCED)
  deck.shuffle()
  player_1 = Player("Player 1")
  player_2 = Player("Player 2")
  player_1.draw_card(deck.pop())
  player_1.draw_card(deck.pop())
  player_1.draw_card(deck.pop())
  if player_1.hand:
    print("NO EMPTY")
  else:
    print("EMPTY")
    
  
  