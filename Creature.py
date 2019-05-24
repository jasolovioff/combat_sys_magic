from Card import Card


class Creature(Card):
    toughness = 0
    power = 0
    # uncolored, white, black, blue, red, green
    summon_costs = {"uncolored": 0, "white": 0, "black": 0, "blue": 0, "red": 0, "green": 0}
    name = ""

    def __init__(self, toughness, power, summon_costs, name):
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
