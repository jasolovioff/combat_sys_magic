from Card import Card

'''
Artifacts
Artifacts represent machines or magical objects. Like creatures, you can cast an artifact as a spell during your main 
phase, and it remains on the battlefield unless it’s destroyed, sacrificed, exiled, or otherwise removed. Most artifacts
are colorless, which means you can cast them with any color of mana.
'''


class Artifact(Card):

    name = ""
    toughness = None
    power = None
    summon_costs = {"uncolored": 0, "white": 0, "black": 0, "blue": 0, "red": 0, "green": 0}

    def __init__(self, name, summon_costs, toughness=None, power=None):
        self.name = name
        self.toughness = toughness
        self.power = power
        self.summon_costs = summon_costs
