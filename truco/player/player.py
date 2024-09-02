from decks import Card

class EmptyHandError(Exception):
  """
  Exception raised when an operation is attempted with an empty hand.
  """
  def __init__(self, message="The hand is empty."):
      self.message = message
      super().__init__(self.message)

class Hand:
  """
  Represents a player's hand of cards.

  Attributes:
    max_cards (int): The maximum number of cards that can be held in hand.
  """
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
    """
    Adds a card to the hand if the maximum number of cards has not been reached.

    Args:
      card (Card): The card to add to the hand.

    Raises:
      ValueError: If adding the card would exceed the maximum number of cards.
    """    
    if len(self) < self._max_cards:
      self._cards.append(card)
    else:
      raise ValueError(f"Cannot add more than {self._max_cards} cards to hand.")
    
  def play_card(self, card: Card):
    """
    Removes a card from the hand and returns it.

    Args:
      card (Card): The card to remove from the hand.

    Returns:
      Card: The removed card.

    Raises:
      ValueError: If the card is not in the hand.
    """
    if card in self._cards:
      self._cards.remove(card)
      return card
    else:
      raise ValueError(f"Card {card} not in hand.")
      
  @property
  def cards(self):
    return tuple(card for card in self._cards)

class Player:
  """
  Represents a player in the game.

  Attributes:
    name (str): The name of the player.
    hand (Hand): The hand of cards held by the player.
  """
  def __init__(self, name: str) -> None:
    self._name = name
    self._hand = Hand()
    
  def draw_card(self, card: Card):    
    self._hand.add_card(card)
    
  def play_card(self, card: Card) -> Card:
    if self._hand: #Checks if hand is not empty
      return self._hand.play_card(card)
    raise EmptyHandError
    
    
  @property
  def hand(self):
    return self._hand.cards
      
  

    
  @property
  def name(self):
    return self._name
  
