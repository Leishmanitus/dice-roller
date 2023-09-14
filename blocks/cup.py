
from blocks.dice import Dice

class Cup(list):
	'''Designed to handle many Dice objects. Use add_to and remove_from to manage stack.'''
	__cup_count: int = 0

#creation and deletion events
	def __init__(self):
		self.__cup_count += 1
	def __del__(self):
		self.__cup_count -= 1

#getters and boolean checks
	def check_count(self):
		'''Just to check the private attribute cup_count'''
		return self.__cup_count

	def is_empty(self)->bool:
		'''Checks if the dice stack is empty'''
		return len(self) == 0

	def dice_test(self, dice:Dice)->bool:
		'''returns true if requested dice object in the stack'''
		for die in self:
			if die == dice:
				return True
		return False

#methods
	def add_to(self, *others):
		'''Add a Dice instance to the stack and combine duplicates'''
		for other in others:
			if isinstance(other, Dice):
				if self.is_empty():
					self.append(other)
					self.clear_empties()
				elif self.dice_test(other):
					self[self.index(other)] += other
					self.clear_empties()
				else:
					self.append(other)
					self.clear_empties()
		

	def remove_from(self, other:Dice):
		'''Removes a Dice from the end'''
		if isinstance(other, Dice):
			if self.is_empty():
				return
			if self.dice_test(other):
				self[self.index(other)] -= other
				self.clear_empties()
			else:
				self[0] -= 1

	def clear_empties(self):
		'''Cycles through the stack and deletes the 0dX dice'''
		for die in self:
			if die.check_mod():
				del self[self.index(die)]

#roll types
	def roll_all(self) -> str:
		'''Cycles through all Dice objects in list and calls their roll method.'''
		if self.is_empty():
			return 'No dice!'
		result = ''.join(f'{die.roll()}\n' for die in self if isinstance(die, Dice))
		return result

	def roll_4d6_drop_lowest(self):
		'''returns a list of numbers to be
		used as new stats for a DnD character
		using the 4d6 drop the lowest rule'''
		for _ in range(6):
			high_3 = Dice(6,4).roll_list()
			high_3.pop(high_3.index(min(high_3)))
			self.append(sum(high_3))
		return self
