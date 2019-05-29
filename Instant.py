from Card import Card

'''
Instants
Instants are spells that can be cast at any time, even during your opponent’s turn or during combat. Like sorceries, 
instants have a one-time effect, and then you put them into your graveyard.
'''


class Instant(Card):

    name = ""
    summon_costs = {"uncolored": 0, "white": 0, "black": 0, "blue": 0, "red": 0, "green": 0}

    def __init__(self, name, summon_costs):
        self.name = name
        self.summon_costs = summon_costs
