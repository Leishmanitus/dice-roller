
from dataclasses import dataclass

@dataclass
class AbilityScore:
	'''A character ability score is formed with given input'''
	def __init__(self, name:str, value:int=10):
			self.name = name
			self.score = value
			self.modifier = (self.score - 10)//2

	def __str__(self):
		return self.name

	def update_modifier(self):
		'''setter for modifier'''
		self.modifier = (self.score - 10)//2
