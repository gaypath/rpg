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

class Class:
	def __init__(self, name, level):
		self.id = get_class_id(name)
		
		if self.id and self.id != 0:
			self.load = load_class(self.id)
			self.level = level
			self.name = self.load['name']
			self.starting_ap = self.load['start_ap']
		else:
			self.level = level
			self.name = name
			
		self.skills = self.get_skills()
	
	@property
	def skills(self):
		return self._skills
		
	@skills.setter
	def skills(self, val):
		self._skills = val
			
	def get_skills(self):
		s = []
		skills = [x for x in os.listdir('./rpg/skills') if os.path.isfile(os.path.join('./rpg/skills', x)) and x[0] == str(self.id)]
		for skill in skills:
			skill_id = skill[0:3]
			s.append(Skill(skill_id))
			
		return s
	
	@property
	def hit_die(self):
		if self.level == 1:
			return self.load['hit_die'][0] * self.load['hit_die'][1]
		else:
			hd = 0
			for i in range(self.load['hit_die'][0]):
				hd += random.randint(1, self.load['hit_die'][1])
				
			return hd
	
			