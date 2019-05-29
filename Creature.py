from Card import Card

'''
Creatures
Creatures fight for you: they can attack during the combat phase of your turn and block during the combat phase of an 
opponent’s turn. You can cast a creature as a spell during your main phase, and it remains on the battlefield as a 
permanent. Creatures enter the battlefield with "summoning sickness," which means that a creature you control can’t 
attack (or use an ability that has  in its cost) until it starts your turn under your control. You can block with a 
creature no matter how long it’s been on the battlefield.
'''


class Creature(Card):
    toughness = 0
    power = 0
    # uncolored, white, black, blue, red, green
    summon_costs = {"uncolored": 0, "white": 0, "black": 0, "blue": 0, "red": 0, "green": 0}
    name = ""

    def __init__(self, name, toughness, power, summon_costs):
        self.toughness = toughness
        self.power = power
        self.summon_costs = summon_costs
        self.name = name

    def get_toughness(self):
        return self.toughness

    def get_power(self):
        return self.power

    def get_summon_costs(self):
        return self.summon_costs
