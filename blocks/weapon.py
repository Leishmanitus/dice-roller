
from os import path
from dataclasses import dataclass
from blocks.item_configs import ItemConfigs
from blocks.dice import Dice

@dataclass
class Weapon:
	'''creates an object representing a weapon'''
	config = ItemConfigs('./blocks/data/weapons.ini').config
	def __init__(self, attribute:int=0, name:str='fist'):
		self.name = name
		self.mod = attribute
		self.damage_dice = Dice(self.find_damage())

	def __str__(self) -> str:
		return self.name

	def find_damage(self)->int:
		'''parses .ini to find weapons damage'''
		if self.config[self.name]['two-handed']:
			return int(self.config[self.name]['damage2'])
		return int(self.config[self.name]['damage1'])

	def find_handling(self)->str:
		'''returns wether one handed or two handed weapon'''
		if self.config[self.name]['two-handed']:
			return 'two-handed'
		return 'one-handed'

#checks for a weapons.ini file
#if none exists it creates a new file
	def restore_default_weapons(self):
		'''If the weapons.ini file does not exist then a new one will be created'''
		if not path.exists('./blocks/data/weapons.ini'):
			self.config.add_section('dagger')
			self.config['dagger'] = {
				'light': 'True',
				'heavy': 'False',
				'thrown': 'True',
				'finesse': 'True',
				'versatile': 'False',
				'two-handed': 'False',
				'proficiency': 'simple',
				'hit': '1d20',
				'damage1': '1d4',
				'damage2': '1d4',
				'range': '20/60ft'
			}
			self.config.add_section('shortsword')
			self.config['shortsword'] = {
				'light': 'True',
				'heavy': 'False',
				'thrown': 'False',
				'finesse': 'True',
				'versatile': 'False',
				'two-handed': 'False',
				'proficiency': 'martial',
				'hit': '1d20',
				'damage1': '1d6',
				'damage2': '1d6',
				'range': 'None'
			}
			self.config.add_section('longsword')
			self.config['longsword'] = {
				'light': 'False',
				'heavy': 'False',
				'thrown': 'False',
				'finesse': 'False',
				'versatile': 'True',
				'two-handed': 'False',
				'proficiency': 'martial',
				'hit': '1d20',
				'damage1': '1d8',
				'damage2': '1d10',
				'range': 'None'
			}
			self.config.add_section('greatsword')
			self.config['greatsword'] = {
				'light': 'False',
				'heavy': 'True',
				'thrown': 'False',
				'finesse': 'False',
				'versatile': 'False',
				'two-handed': 'True',
				'proficiency': 'martial',
				'hit': '1d20',
				'damage1': '2d6',
				'damage2': '2d6',
				'range': 'None'
			}
			self.config.add_section('handaxe')
			self.config['handaxe'] = {
				'light': 'True',
				'heavy': 'False',
				'thrown': 'True',
				'finesse': 'False',
				'versatile': 'False',
				'two-handed': 'False',
				'proficiency': 'simple',
				'hit': '1d20',
				'damage1': '1d6',
				'damage2': '1d6',
				'range': '20/60ft'
			}
			self.config.add_section('battleaxe')
			self.config['battleaxe'] = {
				'light': 'False',
				'heavy': 'False',
				'thrown': 'False',
				'finesse': 'False',
				'versatile': 'True',
				'two-handed': 'False',
				'proficiency': 'martial',
				'hit': '1d20',
				'damage1': '1d8',
				'damage2': '1d10',
				'range': 'None'
			}
			self.config.add_section('greataxe')
			self.config['greataxe'] = {
				'light': 'False',
				'heavy': 'True',
				'thrown': 'False',
				'finesse': 'False',
				'versatile': 'False',
				'two-handed': 'True',
				'proficiency': 'martial',
				'hit': '1d20',
				'damage1': '1d12',
				'damage2': '1d12',
				'range': 'None'
			}
			self.config.add_section('light hammer')
			self.config['light hammer'] = {
				'light': 'True',
				'heavy': 'False',
				'thrown': 'True',
				'finesse': 'False',
				'versatile': 'False',
				'two-handed': 'False',
				'proficiency': 'simple',
				'hit': '1d20',
				'damage1': '1d4',
				'damage2': '1d4',
				'range': '20/60ft'
			}
			self.config.add_section('warhammer')
			self.config['warhammer'] = {
				'light': 'False',
				'heavy': 'False',
				'thrown': 'False',
				'finesse': 'False',
				'versatile': 'True',
				'two-handed': 'False',
				'proficiency': 'martial',
				'hit': '1d20',
				'damage1': '1d8',
				'damage2': '1d10',
				'range': 'None'
			}
			self.config.add_section('maul')
			self.config['maul'] = {
				'light': 'False',
				'heavy': 'True',
				'thrown': 'False',
				'finesse': 'False',
				'versatile': 'False',
				'two-handed': 'True',
				'proficiency': 'martial',
				'hit': '1d20',
				'damage1': '2d6',
				'damage2': '2d6',
				'range': 'None'
			}
			self.config.add_section('club')
			self.config['club'] = {
				'light': 'True',
				'heavy': 'False',
				'thrown': 'False',
				'finesse': 'False',
				'versatile': 'False',
				'two-handed': 'False',
				'proficiency': 'simple',
				'hit': '1d20',
				'damage1': '1d4',
				'damage2': '1d4',
				'range': 'None'
			}
			self.config.add_section('quarterstaff')
			self.config['quarterstaff'] = {
				'light': 'False',
				'heavy': 'False',
				'thrown': 'False',
				'finesse': 'False',
				'versatile': 'True',
				'two-handed': 'False',
				'proficiency': 'simple',
				'hit': '1d20',
				'damage1': '1d6',
				'damage2': '1d8',
				'range': 'None'
			}
			self.config.add_section('greatclub')
			self.config['greatclub'] = {
				'light': 'False',
				'heavy': 'True',
				'thrown': 'False',
				'finesse': 'False',
				'versatile': 'False',
				'two-handed': 'True',
				'proficiency': 'simple',
				'hit': '1d20',
				'damage1': '1d8',
				'damage2': '1d8',
				'range': 'None'
			}
			self.config.add_section('sickle')
			self.config['sickle'] = {
				'light': 'True',
				'heavy': 'False',
				'thrown': 'False',
				'finesse': 'False',
				'versatile': 'False',
				'two-handed': 'False',
				'proficiency': 'simple',
				'hit': '1d20',
				'damage1': '1d4',
				'damage2': '1d4',
				'range': 'None'
			}
			self.config.add_section('scimitar')
			self.config['scimitar'] = {
				'light': 'True',
				'heavy': 'False',
				'thrown': 'False',
				'finesse': 'True',
				'versatile': 'False',
				'two-handed': 'False',
				'proficiency': 'martial',
				'hit': '1d20',
				'damage1': '1d6',
				'damage2': '1d6',
				'range': 'None'
			}
			self.config.add_section('rapier')
			self.config['rapier'] = {
				'light': 'False',
				'heavy': 'False',
				'thrown': 'False',
				'finesse': 'True',
				'versatile': 'False',
				'two-handed': 'False',
				'proficiency': 'martial',
				'hit': '1d20',
				'damage1': '1d8',
				'damage2': '1d8',
				'range': 'None'
			}
			self.config.add_section('spear')
			self.config['spear'] = {
				'light': 'False',
				'heavy': 'False',
				'thrown': 'True',
				'finesse': 'False',
				'versatile': 'True',
				'two-handed': 'False',
				'proficiency': 'simple',
				'hit': '1d20',
				'damage1': '1d6',
				'damage2': '1d8',
				'range': '20/60ft'
			}
			self.config.add_section('javelin')
			self.config['javelin'] = {
				'light': 'False',
				'heavy': 'False',
				'thrown': 'True',
				'finesse': 'False',
				'versatile': 'False',
				'two-handed': 'False',
				'proficiency': 'simple',
				'hit': '1d20',
				'damage1': '1d6',
				'damage2': '1d6',
				'range': '30/120ft'
			}
			self.config.add_section('flail')
			self.config['flail'] = {
				'light': 'False',
				'heavy': 'False',
				'thrown': 'False',
				'finesse': 'False',
				'versatile': 'False',
				'two-handed': 'False',
				'proficiency': 'martial',
				'hit': '1d20',
				'damage1': '1d8',
				'damage2': '1d8',
				'range': 'None'
			}
			self.config.add_section('morningstar')
			self.config['morningstar'] = {
				'light': 'False',
				'heavy': 'False',
				'thrown': 'False',
				'finesse': 'False',
				'versatile': 'False',
				'two-handed': 'False',
				'proficiency': 'martial',
				'hit': '1d20',
				'damage1': '1d8',
				'damage2': '1d8',
				'range': 'None'
			}
			self.config.add_section('mace')
			self.config['mace'] = {
				'light': 'False',
				'heavy': 'False',
				'thrown': 'False',
				'finesse': 'False',
				'versatile': 'False',
				'two-handed': 'False',
				'proficiency': 'simple',
				'hit': '1d20',
				'damage1': '1d6',
				'damage2': '1d6',
				'range': 'None'
			}
			with open('./blocks/data/weapons.ini', 'w') as file:
				self.config.write(file)
