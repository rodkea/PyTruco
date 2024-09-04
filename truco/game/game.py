from .team import Team
from collections import deque


class Round:
  pass 

class Game:
  
  def __init__(self, team_1: Team, team_2: Team):
    if len(team_1) != len(team_2):
        raise ValueError("Both teams must have the same number of players.")
    self._team_1 = team_1
    self._team_2 = team_2
    
    
  def __repr__(self) -> str:
    return f"Game(({self._team_1}), ({self._team_2}))"
    
  def _create_play_order(self) -> deque:
    order = deque()
    for player_1, player_2 in zip(self._team_1, self._team_2):
          order.append(player_1)
          order.append(player_2)
    return order
      
  def start_game(self):
    # SHUFLE TEAMS MEMBERS
    self._team_1.shuffle()
    self._team_2.shuffle()
    # CREATE ORDER
    self._order = self._create_play_order()
    while self._team_1.points < 30 or self._team_2 < 30:
      Round()
      
    

    