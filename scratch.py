
# from classes import Dice
# from classes import Cup
from classes import Weapon
from classes import Character

steve = Character('Steve')
steve.change_weapon('battleaxe')
print(steve,steve.actions.make_attack(),sep='\n')
weapon = Weapon()
print(weapon.config[weapon.name]['mod'][0])
