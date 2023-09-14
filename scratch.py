
# from blocks.dice import Dice
# from blocks.cup import Cup
from blocks.weapon import Weapon
from blocks.character import Character

steve = Character('Steve')
steve.change_weapon('battleaxe')
print(steve,steve.actions.make_attack(),sep='\n')
weapon = Weapon()
print(weapon.config[weapon.name]['mod'][0])
