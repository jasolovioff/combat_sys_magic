from Card import Card

'''
Enchantments
Enchantments have persistent magical effects that affect the game as long as they’re on the battlefield. Like 
creatures, you can cast an enchantment as a spell during your main phase, and it remains on the battlefield unless 
it’s destroyed, sacrificed, exiled, or otherwise removed.
'''


class Enchantment(Card):

    name = ""
    summon_costs = {"uncolored": 0, "white": 0, "black": 0, "blue": 0, "red": 0, "green": 0}

    def __init__(self, name, summon_costs):
        self.name = name
        self.summon_costs = summon_costs
