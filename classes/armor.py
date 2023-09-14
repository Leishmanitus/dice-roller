
from .item_configs import ItemConfigs
from dataclasses import dataclass

@dataclass
class Armor:
	'''grabs an armor item from an .ini file'''
	configs = ItemConfigs('./classes/data/armors.ini')
	def __init__(self,
	name:str='unarmored',
	mod:int=0,
	prof:int=2):
		self.name = name
		self.armor_resist = int(
			self.configs.get_property('leather','armor-resist')) + mod
		self.armor_class = 8 + mod + prof

	def __str__(self) -> str:
		return self.name
