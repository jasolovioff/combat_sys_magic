from Creature import Creature
from Land import Land

gnome = Creature(5, 5,{"uncolored": 0, "white": 0, "black": 0, "blue": 0, "red": 0, "green": 0},"El Gnomo")

print(gnome.get_toughness())

mountain = Land(red_mana=10)

print("mana de la montaña:")
print(mountain.get_mana())
