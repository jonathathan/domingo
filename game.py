import cards

class GamePhase(object):
  ACTION, BUY, CELLAR, MILITIA, MINE, REMODEL, WORKSHOP = range(7)

class ObservableState(object):
  def __init__(self, phase, deck, discard, hand, store, actions, buys, cards, gold)
    self.phase = phase
    self.deck = deck
    self.discard = discard
    self.hand = hand
    self.store = store
    self.actions = actions
    self.buys = buys
    self.cards = cards
    self.gold = gold

class Game(object):
  def __init__(self, agent, bgent):
    self.agent = agent
    self.bgent = bgent
    self.agent_deck = []
    self.agent_discard = {cards.Estate: 3, cards.Copper: 7}
    self.agent_hand = {}
    self.bgent_deck = []
    self.bgent_discard = {cards.Estate: 3, cards.Copper: 7}
    self.bgent_hand = {}
    self.store = {
        cards.Estate: 12,
        cards.Duchy: 12,
        cards.Province: 12,
        cards.Copper: 60,
        cards.Silver: 40,
        cards.Gold: 30,
        # cards.Cellar: 10 (because fuck Cellars)
        cards.Market: 10,
        cards.Militia: 10,
        cards.Mine: 10,
        cards.Moat: 10,
        cards.Remodel: 10,
        cards.Smithy: 10,
        cards.Village: 10,
        cards.Woodcutter: 10,
        cards.Workshop: 10,
    }
    self.agent_turn = True
    self.phase = GamePhase.ACTION

  def play():
    while self.store[cards.Province] > 0: #TODO: other end-game condition
      player = agent if self.agent_turn else bgent
      move = player.play_turn(self.get_observable_state(player))

  def get_observable_state(player):
    if player == self.agent:
      pass
