# Actions cards:
#
# Cellar: Trade discard for +1 card (0+ times)
# Militia: Choose from hand
# Mine: Choose treasure from hand
# Remodel: Choose from hand, choose from store
# Workshop: Choose from store
#
# Regular Play:
# - play actions (choose action from hand)
# - purchase (choose from store)

class Card(object):
  def __init__(self, cost, plus_actions, plus_buys, plus_cards, plus_gold, plus_victory):
    self.cost = cost
    self.plus_actions = plus_actions
    self.plus_buys = plus_buys
    self.plus_cards = plus_cards
    self.plus_gold = plus_gold
    self.plus_victory = plus_victory

#
# Action Cards
#

class ActionCard(object):
  pass

class Cellar(ActionCard):
  def __init__(self):
    super(Cellar, self).__init__(2, 1, 0, 0, 0, 0)

class Market(ActionCard):
  def __init__(self):
    super(Market, self).__init__(5, 1, 1, 1, 1, 0)

class Militia(ActionCard):
  def __init__(self):
    super(Militia, self).__init__(4, 0, 0, 0, 2, 0)

class Mine(ActionCard):
  def __init__(self):
    super(Mine, self).__init__(5, 0, 0, 0, 0, 0)

class Moat(ActionCard):
  def __init__(self):
    super(Moat, self).__init__(2, 0, 0, 2, 0, 0)

class Remodel(ActionCard):
  def __init__(self):
    super(Remodel, self).__init__(4, 0, 0, 0, 0, 0)

class Smithy(ActionCard):
  def __init__(self):
    super(Smithy, self).__init__(4, 0, 0, 3, 0, 0)

class Village(ActionCard):
  def __init__(self):
    super(Village, self).__init__(3, 2, 0, 1, 0, 0)

class Woodcutter(ActionCard):
  def __init__(self):
    super(Woodcutter, self).__init__(3, 0, 1, 0, 2, 0)

class Workshop(ActionCard):
  def __init__(self):
    super(Workshop, self).__init__(3, 0, 0, 0, 0, 0)

#
# Treasure Cards
#

class TreasureCard(Card):
  def __init__(self, cost, gold):
    super(TreasureCard, self).__init__(cost, 0, 0, 0, gold, 0)

class Copper(TreasureCard):
  def __init__(self):
    super(Copper, self).__init__(0, 1)

class Silver(TreasureCard):
  def __init__(self):
    super(Silver, self).__init__(3, 2)

class Gold(TreasureCard):
  def __init__(self):
    super(Gold, self).__init__(6, 3)

#
# Victory Cards
#

class VictoryCard(Card):
  def __init__(self, cost, points):
    super(VictoryCard, self).__init__(cost, 0, 0, 0, 0, points)

class Estate(VictoryCard):
  def __init__(self):
    super(Estate, self).__init__(2, 1)

class Duchy(VictoryCard):
  def __init__(self):
    super(Duchy, self).__init__(5, 3)

class Province(VictoryCard):
  def __init__(self):
    super(Province, self).__init__(8, 6)

