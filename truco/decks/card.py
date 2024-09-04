from enum import Enum

class Rank(Enum):
  """
  Enum to represent the ranks of a card in a spanish deck.

  Members:
  - ONE: Represents rank 1.
  - TWO: Represents rank 2.
  - THREE: Represents rank 3.
  - FOUR: Represents rank 4.
  - FIVE: Represents rank 5.
  - SIX: Represents rank 6.
  - SEVEN: Represents rank 7.
  - TEN: Represents rank 10.
  - ELEVEN: Represents rank 11.
  - TWELVE: Represents rank 12.
  """
  ONE     = 1
  TWO     = 2
  THREE   = 3
  FOUR    = 4
  FIVE    = 5
  SIX     = 6
  SEVEN   = 7
  EIGHT   = 8
  NINE    = 9
  TEN     = 10
  ELEVEN  = 11
  TWELVE  = 12

class RankReduced(Enum):
  """
  Enum to represent the ranks of a card in a spanish deck with some ranks omitted.

  Members:
  - ONE: Represents rank 1.
  - TWO: Represents rank 2.
  - THREE: Represents rank 3.
  - FOUR: Represents rank 4.
  - FIVE: Represents rank 5.
  - SIX: Represents rank 6.
  - SEVEN: Represents rank 7.
  - TEN: Represents rank 10.
  - ELEVEN: Represents rank 11.
  - TWELVE: Represents rank 12.
  """
  ONE     = 1
  TWO     = 2
  THREE   = 3
  FOUR    = 4
  FIVE    = 5
  SIX     = 6
  SEVEN   = 7
  TEN     = 10
  ELEVEN  = 11
  TWELVE  = 12

class Suit(Enum):
  """
  Enum to represent the suits of a card in a spanish deck.

  Members:
  - BASTO: Represents the 'basto' suit.
  - COPA: Represents the 'copa' suit.
  - ESPADA: Represents the 'espada' suit.
  - ORO: Represents the 'oro' suit.
  """
  BASTO  = 'basto'
  COPA   = 'copa'
  ESPADA = 'espada'
  ORO    = 'oro'
  
class Card:  
  """
  Class to represent a playing card with a rank and a suit.

  Attributes:
  - rank (Rank): The rank of the card.
  - suit (Suit): The suit of the card.  
  """
  
  def __init__(self, rank: Rank, suit: Suit) -> None:
    
    if not isinstance(rank, Rank | RankReduced):
      raise TypeError(f"Invalid type for rank: {type(rank).__name__}. Must be an instance of Rank.")
    if not isinstance(suit, Suit):
      raise TypeError(f"Invalid type for suit: {type(suit).__name__}. Must be an instance of Suit.")
    self._rank: Rank = rank
    self._suit: Suit = suit
  
  def __eq__(self, other: object) -> bool:
    if not isinstance(other, Card):
      return False
    return self._rank == other._rank and self._suit == other._suit
    
  def __repr__(self):
    return f"Card(rank={self._rank}, suit={self._suit})"
  
  @property
  def rank(self):
     return self._rank.value
  
  @property
  def suit(self):
    return self._suit.value