from Card import Card

'''
Lands
You’ll use lands to generate mana, the game’s primary resource, which is used to cast spells and activate abilities. 
Each basic land makes one mana of a particular color. Plains make white mana , Islands make blue mana , Swamps make 
black mana , Mountains make red mana , and Forests make green mana .
'''


class Land(Card):
    name = "land"
    mana = {"uncolored": 0, "white": 0, "black": 0, "blue": 0, "red": 0, "green": 0}

    def __init__(self, uncolored_mana=0, white_mana=0, black_mana=0, blue_mana=0, red_mana=0, green_mana=0):
        self.mana["uncolored"] = uncolored_mana
        self.mana["white"] = white_mana
        self.mana["black"] = black_mana
        self.mana["blue"] = blue_mana
        self.mana["red"] = red_mana
        self.mana["green"] = green_mana

    def get_mana(self):
        return self.mana
