import json, math, os, re

def load_skill(id):
	with open("rpg/skills/{}.json".format(str(id)), "r") as f:
		skill = json.loads(f.read())
	
	return skill

class Skill:
	def __init__(self, skill_id):
		skill_load = load_skill(skill_id)
		
		self.name = skill_load['name']
		self.desc = skill_load['desc']
		self.type = skill_load['type']
		self.stat = skill_load['stat']
		
		if self.type == 1:
			self.combat_skill(skill_load)
		elif self.type == 2:
			self.effect_skill(skill_load)
		elif self.type == 3:
			self.passive_skill(skill_load)
	
	def combat_skill(self, skill_load):
		damage_calc = re.compile(r'<roll:(?P<roll>\dd\d{1,2})>?<(?P<mods>.+)>')
		
		self.levels = {}
		
		for key in skill_load['levels'].keys():
			match = damage_calc.match(skill_load['levels'][key])
			self.levels[key] = match.groupdict()
		
		self.cost = skill_load['cost']
		
	def effect_skill(self, skill_load):
		return
		
	def passive_skill(self, skill_load):
		pass
		
# Skill(102)