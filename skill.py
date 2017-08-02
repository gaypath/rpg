import json, math, os, re

def load_skill(id):
	with open("rpg/skills/{}.json".format(str(id)), "r") as f:
		skill = json.loads(f.read())
	
	return skill

class Skill:
	def __init__(self, skill_id):
		skill_load = load_skill(skill_id)
		self.id = skill_id
		self.name = skill_load['name']
		self.desc = skill_load.get('desc', None)
		self.type = skill_load.get('type', None)
		self.stat = skill_load.get('stat', None)
		self.req_level = skill_load.get('req_level', 1)
		
		if self.type == 1:
			self.use_skill(skill_load)
		elif self.type == 2:
			self.use_skill(skill_load)
		elif self.type == 3:
			self.passive_skill(skill_load)
	
	def use_skill(self, skill_load):
		pattern = re.compile(r'<roll:(?P<roll>\dd\d{1,2})>?<(?P<mods>.+)>')
		
		self.levels = {}
		
		for key in skill_load['levels'].keys():
			match = pattern.match(skill_load['levels'][key])
			self.levels[key] = match.groupdict()
		
		self.cost = skill_load['cost']
	
	# def use(self, player):
		# pass
	
	# def effect_skill(self, skill_load):
		# return
		
	def passive_skill(self, skill_load):
		pass
		
# Skill(102)