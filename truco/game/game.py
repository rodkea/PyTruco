from typing import List
from player import Player

class Team:
  """
  Represents a team in the game.

  Attributes:
    team_name (str): The name of the team.
    players (List[Player]): The list of players in the team.
    max_length (int): The maximum allowed length for the team name. Default is 30.
  """
  
  def __init__(self, team_name: str, max_length: int = 30):
    self._team_name = team_name
    self._players: List[Player] = []
    self._max_length = max_length
    self._points = 0
  
  def __repr__(self) -> str:
    return f"Team({self.team_name}, {self._max_length})"
  
  def __getitem__(self, position):
    return self._players[position]
    
  def __len__(self) -> int:
    return len(self._players)
  
  @property
  def team_name(self) -> str:
    return self._team_name
  
  @property
  def max_length(self) -> int:
    return self._max_length
  
  @property
  def points(self) -> int:
    return self._points
  
  def change_team_name(self, name : str):
    """
    Changes the name of the team if the new name meets the length requirement.

    Args:
        name (str): The new name for the team.

    Raises:
        ValueError: If the name is longer than 30 characters.
    """ 
    if name and len(name) <= self._max_length:
      self._team_name = name
    raise ValueError(f"The team name must be {self._max_length} characters or fewer.")
  
  def add_player(self, player: Player):
    if len(self) <3:
      self._players.append(player)
  
  def add_point(self, points: int):
    self._points += points
    

class Game:
  pass