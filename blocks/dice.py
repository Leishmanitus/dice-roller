
'''Dice objects represent a multi-sided dice.
Functionality includes: making a roll, combining dice objects,
comparing dice objects'''

import random

class Dice:
	'''Represents a user defined amount of dice of a user specified size.'''
	__die_count: int = 0

#construction and deletion events
	def __init__(self, size:int=6, mod:int=1):
		'''Sets the size and name upon object creation.'''
		if self.__die_count < 10:
			self.size = size
			self.mod = mod
			self.name = f"{self.mod}d{self.size}"
			self.__die_count += self.mod

	def __del__(self):
		'''die count decreases by mod variable upon object deletion'''
		self.__die_count -= self.mod

#arithmetic operators
	def _common_arithmetic(self, other:object or int, operator:callable)->object:
		'''takes other as dice object or int to perform arithmetic
		with self through lambda function'''
		if isinstance(other, int):
			res = operator(self.mod, other)
		elif isinstance(other, Dice) and self == other:
			res = operator(self.mod, other.mod)
		else:
			raise ValueError('Not same size')
		temp = Dice(self.size, res)
		return temp

	def __add__(self, other:object or int)->object:
		return self._common_arithmetic(other, lambda x,y:x+y)

	def __sub__(self, other:object or int)->object:
		return self._common_arithmetic(other, lambda x,y:x-y)

	def __mul__(self, other:object or int)->object:
		return self._common_arithmetic(other, lambda x,y:x*y)

	def __floordiv__(self, other:object or int)->object:
		return self._common_arithmetic(other, lambda x,y:x//y)

	def __truediv__(self, other:object or int)->object:
		return self._common_arithmetic(other, lambda x,y:x//y)

#boolean operators
	def _common_comparison(self, other: object or int, operator: callable)->object:
		'''takes other as a dice object or int to compare
		with self through lambda function'''
		if isinstance(other, int):
			return operator(self, self.size, other)
		if isinstance(other, Dice):
			return operator(self, self.size, other.size)
		raise ValueError('Not a valid unit')

	def __eq__(self, other:object or int):
		return self._common_comparison(other, lambda x,y:x == y)

	def __ne__(self, other:object or int):
		return self._common_comparison(other, lambda x,y:x != y)

	def __lt__(self, other:object or int)->bool:
		return self._common_comparison(other, lambda x,y:x < y)

	def __gt__(self, other:object or int)->bool:
		return self._common_comparison(other, lambda x,y:x > y)

	def __le__(self, other:object or int)->bool:
		return self._common_comparison(other, lambda x,y:x <= y)

	def __ge__(self, other:object or int)->bool:
		return self._common_comparison(other, lambda x,y:x >= y)

	def __contains__(self, other:object or int)->bool:
		return self._common_comparison(other, lambda x,y:x in y)
	
	def __max__(self, other:object or int)->int:
		return self._common_arithmetic(other, lambda x,y:x if x>y else y)
		
	def __min__(self, other:object or int)->int:
		return self._common_arithmetic(other, lambda x,y:x if x<y else y)

#methods
	def check_mod(self)->bool:
		'''object destroyed on 0 mod'''
		return self.mod <= 0

	def check_count(self)->int:
		'''returns the count of Dice instances'''
		return self.__die_count

	def update_name(self):
		'''updates the name with current mod and size'''
		self.name = f'{self.mod}d{self.size}'

	def roll(self)->str:
		'''Returns a string representing a self.mod
		amount of rolls of self.size value of dice'''
		single = f'{self.name}- '
		total = 0
		for _ in range(self.mod):
			roll = random.randint(1, self.size)
			single += f'{roll} '
			total += roll
		final = single + f'-Total-{total}'
		return final
	
	def roll_list(self)->list:
		'''The same as roll except returns a list'''
		results = []
		for _ in range(self.mod):
			results.append(random.randint(1, self, self.size))
		return results
