from enum import Enum
from collections import namedtuple
import random

class DeckType(Enum):
  REDUCED = 0
  FULL = 1

Card = namedtuple('Card', ['rank', 'suit'])

class SpanishDeck:
  
  all_ranks= [str(n) for n in range(1, 13)]
  reduced_ranks = [str(n) for n in range(1, 8)] + [str(n) for n in range(10, 13)]
  suits = 'basto copa espada oro'.split()
  
  def __init__(self, deck_type : DeckType = DeckType.FULL):
    self._deck_type = deck_type
    if deck_type == DeckType.FULL:
      ranks = self.all_ranks
    elif deck_type == DeckType.REDUCED:
      ranks = self.reduced_ranks  
    else:
      raise ValueError("Unrecognized deck type.")
    self._cards = [Card(rank, suit) for suit in self.suits 
                                    for rank in ranks]
  
  def __len__(self):
    return len(self._cards)
  
  def __getitem__(self, position):
    return self._cards[position]
   
  def __repr__(self) -> str:
    return f"SpanishDeck(deck_type={self.type})"
  
  @property
  def type(self):
    return self._deck_type
    
  def pop(self):
    if len(self) > 0:
      return self._cards.pop()
    raise IndexError("pop from empty deck")
  
  def shuffle(self):
    random.shuffle(self._cards)
  