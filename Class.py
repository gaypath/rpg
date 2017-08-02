import json
import random
import os
from .skill import Skill

def get_class_id(name):
	return {
		"rogue": 1,
	}.get(name, 0)

def load_class(id):
	with open('rpg/classes/{}.json'.format(str(id)), 'r') as f:
		clss = json.loads(f.read())
	
	return clss

class Class(object):

	__slots__ = ('id', 'load', 'level', 'name', 'mana_var', 'starting_ap', '_class_skills', 'modifiers')
	
	def __init__(self, name, level):
		self.id = get_class_id(name)
		
		if self.id and self.id != 0:
			self.load = load_class(self.id)
			self.level = level
			self.name = self.load['name']
			self.mana_var = self.load.get('mana', 1)
			self.modifiers = self.load.get('modifiers', None)
			self.starting_ap = self.load['start_ap']
			self.class_skills = self.get_class_skills()
		else:
			self.level = level
			self.name = name
			self.class_skills = []
	
	@property
	def class_skills(self):
		return self._class_skills
		
	@class_skills.setter
	def class_skills(self, val):
		self._class_skills = val
			
	def get_class_skills(self):
		skills = [x for x in os.listdir('./rpg/skills') if os.path.isfile(os.path.join('./rpg/skills', x)) and x[0] == str(self.id)]
		
		s = []
		
		for skill in skills:
			skill_id = skill[0:3]
			s.append(Skill(skill_id))
			
		return s
	
	@property
	def mana(self):
		mana = 1
		
		for i in range(self.level):
			mana += (10 + (self.mana_var * (i + 1) ** 3) * .3) / (self.mana_var * ((i*2.3) + 1))
		
		return mana
	
	@property
	def hit_die(self):
		if self.level == 1:
			return self.load['hit_die'][0] * self.load['hit_die'][1]
		else:
			hd = 0
			for i in range(self.load['hit_die'][0]):
				hd += random.randint(1, self.load['hit_die'][1])
				
			return hd
	
			