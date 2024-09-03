from .team import Team
class Game:
  
  def __init__(self, team_1: Team, team_2: Team):
        if len(team_1) != len(team_2):
            raise ValueError("Both teams must have the same number of players.")
        self._team_1 = team_1
        self._team_2 = team_2 
  
  def __repr__(self) -> str:
    return f"Game(({self._team_1}), ({self._team_2}))"
    