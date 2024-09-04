from decks import SpanishDeck, DeckType, Card
from player import Player, Hand
from game import Game, Team
from random import shuffle

if __name__ == '__main__':
  deck = SpanishDeck(DeckType.REDUCED)
  deck.shuffle()
  player_1 = Player("Player 1")
  player_2 = Player("Player 2")
  player_3 = Player("Player 3")
  team_1 = Team("Team 1")
  team_1.add_player(player_1)
  team_1.add_player(player_2)
  team_1.add_player(player_3)
  team_1.shuffle()
  team_2 = Team("Team 2")
  team_2.add_player(Player("Player 4"))
  
  print(team_1)
  print(team_2)
 
    
  
  