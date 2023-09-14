
from .item_configs import ItemConfigs
from .dice import Dice
from .actions import Actions
from .weapon import Weapon
from .armor import Armor
# from .shield import Shield
from .abilityscore import AbilityScore

class Character:
	'''creates a new character for a DnD style game'''
	config = ItemConfigs('./classes/data/weapons.ini')
	experience_guide = {
		1:[0,2], 2:[300,2], 3:[900,2], 4:[2700,2],
		5:[6500,3], 6:[14000,3], 7:[23000,3],
		8:[34000,3], 9:[48000,4],10:[64000,4],
		11:[85000,4], 12:[100000,4],
		13:[120000,5], 14:[140000,5],
		15:[165000,5], 16:[195000,5],
		17:[225000,6], 18:[265000,6],
		19:[305000,6], 20:[355000,6]
	}
	stats = {
		'strength':AbilityScore('strength', 10),
		'dexterity':AbilityScore('dexterity', 10),
		'constitution':AbilityScore('constitution', 10),
		'intelligence':AbilityScore('intelligence', 10),
		'wisdom':AbilityScore('wisdom', 10),
		'charisma':AbilityScore('charisma', 10)
	}
	
	def __init__(self, name:str, level:int=1):
		self.name = name
		self.level = level
		self.experience = 0
		self.equipment = {
			'weapon': Weapon(),
			'armor': Armor(
			mod=self.stats['constitution'].modifier,
			prof=self.experience_guide[self.level][1]),
			'shield': None
		}
		self.advantage = False
		self.disadvantage = False
		self.actions = Actions(self.equipment['weapon'], self.advantage_state)

	def __str__(self):
		return self.name

#character attribute properties
	@property
	def strength(self)->object:
		'''return ability score object assigned at
		stats slot'''
		return self.stats['strength']
	@property
	def dexterity(self)->object:
		'''return ability score object assigned at
		stats slot'''
		return self.stats['dexterity']
	@property
	def constitution(self)->object:
		'''return ability score object assigned at
		stats slot'''
		return self.stats['constitution']
	@property
	def inteligence(self)->object:
		'''return ability score object assigned at
		stats slot'''
		return self.stats['inteligence']
	@property
	def wisdom(self)->object:
		'''return ability score object assigned at
		stats slot'''
		return self.stats['wisdom']
	@property
	def charisma(self)->object:
		'''return ability score object assigned at
		stats slot'''
		return self.stats['charisma']

#equipment properties
	@property
	def weapon(self)->object:
		'''return Weapon object assigned at
		weapon equipment slot'''
		return self.equipment['weapon']
	@weapon.setter
	def weapon(self, other:object):
		'''takes a Weapon object as argument'''
		self.equipment['weapon'] = other
		self.actions = Actions(self.equipment['weapon'], self.advantage_state)

	@property
	def armor(self)->object:
		'''return Armor object assigned at
		equipment slot'''
		return self.equipment['armor']
	@armor.setter
	def armor(self, other:object):
		'''takes a Armor object as argument and
		reassignes equipment slot'''
		self.equipment['armor'] = other

	@property
	def shield(self)->object:
		'''return Shield object assigned at
		equipment slot'''
		return self.equipment['shield']
	@shield.setter
	def shield(self, other:object):
		'''takes a Shield object as argument and
		reassignes equipment slot'''
		self.equipment['shield'] = other

	def reset_stats(self):
		'''reset all stats to 10'''
		for key in self.stats.items():
			self.stats[key].score = 10

	def reduce_level(self, value:int=1):
		'''lower level by 1 and match experience to guide'''
		if self.level <= 1:
			self.experience = 0
		else:
			self.level -= value
			self.experience = self.experience_guide[self.level][0]

	def raise_level(self,value:int=1):
		'''raise level by 1 and match experience to guide'''
		if self.level >= 20:
			self.experience = 355000
		else:
			self.level += value
			self.experience = self.experience_guide[self.level][0]

#advantage conditionals
	@property
	def advantage_state(self)->str:
		'''advantageous = max(2d20),
		disadvantageous = min(2d20),
		normal = 1d20'''
		if not self.advantage and self.disadvantage:
			return 'Disadvantageous'
		if self.advantage and not self.disadvantage:
			return 'Advantageous'
		return 'Normal'

	def switch_advantage(self):
		'''switches boolean state of advantage attribute'''
		self.advantage = not self.advantage

	def switch_disadvantage(self):
		'''switches boolean state of disadvantage attribute'''
		self.disadvantage = not self.disadvantage

	def change_weapon(self, other):
		'''create a new weapon object in equipment'''
		self.weapon = Weapon(self.strength.modifier, other)

	def use_action(self):
		'''returns action object to use methods'''
		return self.actions
