
'''Used to access .ini files to retreive information
used by the adventurer class to determine dice outcomes'''

# import os
from configparser import ConfigParser

class ItemConfigs:
	'''Takes a filename argument to access and change values'''
	def __init__(self, filename:str):
		self.filename = filename
		self.config = ConfigParser()
		self.config.read(filename)

#getter methods
	def get_item(self, item:str)->str:
		'''returns a string representing the requested item name on file'''
		if item in self.get_items_list():
			return self.get_items_list()[self.get_items_list().index(item)]
		return 'Does not exist'

	def get_items_list(self)->list:
		'''returns a list of options and their values'''
		temp: list = []
		for item in self.config.keys():
			temp.append(item)
		return temp

	def get_properties_list(self, section:str)->list:
		'''returns a list of all the properties of an item'''
		temp: list = []
		for option in self.config[section]:
			temp.append(option)
		return temp
	
	def get_property(self, section:str, option:str)->str:
		'''Returns a single option from a section'''
		return self.config[section][option]

#setter methods
	def set_item(self, section:str='item')->None:
		'''add a new item name with no properties'''
		if section not in self.config.keys():
			self.config.add_section(section)
			self.update_file()
			return print('Section Added')
		else:
			return print('Already Exists')

	def set_property(self, section:str, option:str, value:str)->None:
		'''Sets a new value to selected option'''
		self.config.set(section, option, value)
		self.update_file()

#deleter methods
	def delete_item(self, section:str)->None:
		'''Selected item is removed from the file'''
		self.config.remove_section(section)
		self.update_file()
	
	def delete_property(self, section:str, option:str)->None:
		'''Deletes a selected option'''
		self.config.remove_option(section, option)
		self.update_file()

#save the file
	def update_file(self)->None:
		'''Uses filename variable to save current instances data'''
		with open(self.filename, 'w') as file:
			self.config.write(file)

#format the file to default parameters
	
