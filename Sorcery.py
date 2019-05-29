from Card import Card

'''
Sorceries are spells that you can cast only during a main phase of your turn. They have a one-time effect. You do what 
the spell says, and then put the card into your graveyard.
'''


class Sorcery(Card):

    name = ""
    summon_costs = {"uncolored": 0, "white": 0, "black": 0, "blue": 0, "red": 0, "green": 0}

    def __init__(self, name, summon_costs):
        self.name = name
        self.summon_costs = summon_costs
