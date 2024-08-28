from decks import Card

class Hand:
  def __init__(self, max_cards: int = 3):
    self._cards = []
    self._max_cards = max_cards
    
  def __repr__(self) -> str:
    return f"Hand({self.cards})"
  
  def __len__(self):
    return len(self._cards)
  
  def __getitem__(self, position):
    return self._cards[position]
  
  def add_card(self, card: Card):
    if len(self) < self._max_cards:
      self._cards.append(card)
    else:
      raise ValueError(f"Cannot add more than {self._max_cards} cards to hand.")
    
  def play_card(self, card: Card):
    
    if card in self._cards:
      self.cards.remove(card)
      return card
    else:
      raise ValueError(f"Card {card} not in hand.")
      
  @property
  def cards(self):
    return self._cards

class Player:
  
  def __init__(self, name: str) -> None:
    self._name = name

    
  @property
  def name(self):
    return self._name
  
