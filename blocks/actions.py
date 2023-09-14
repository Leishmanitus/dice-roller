
# from blocks.item_configs import ItemConfigs
from blocks.dice import Dice
# from blocks.weapon import Weapon

class Actions:
	'''handles all possible actions an adventurer can make'''
	def __init__(self, weapon, state):
		self.weapon = weapon
		self.state = state

	def attack_roll(self)->str:
		'''checks two_handed bool from .ini file to determine the damage roll used'''
		return self.weapon.damage_dice.roll()

	def roll_to_hit(self, state:str='Normal')->str:
		'''simulates rolling to hit with the chosen weapon'''
		first = int(Dice(20).roll()[6:8])
		if state != 'Normal':
			second = int(Dice(20).roll()[6:8])
			if state == 'Advantageous':
				return f'Advantage! -2d20- {first} {second} -Max-{max(first,second)}'
			if state == 'Disadvantageous':
				return f'Disadvantage! -2d20- {first} {second} -Min-{min(first,second)}'
		return f'1d20- {first} -Total-{first}'
	
	def make_attack(self):
		'''combines attack roll and roll to hit for smoother experience'''
		return f'{self.roll_to_hit()}\n{self.attack_roll()}'

	def check_for_crit(self, roll)->bool:
		'''parses a string to find a 20'''
		return '20' in roll
