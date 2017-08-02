import asyncio, asyncpg
import random
from .Class import load_class, Class
from .item import load_item, Equipment

class Player:
	
	__slots__ = (
		'member', 'pool',
		'level', 'class_',
		'_skills', 'ability_points',
		'max_health', 'max_mana', 'health', '_att', '_def',
		'str_', 'dex', 'int_', 'wis', 'luk', 'cha',
		'_weapon', 'shield', 'hat'
	)
	
	SETTERS = ('class_', '_weapon', '_att', '_skills', '_def')
	
	EXTERNAL = ('member', 'pool')
	
	EQUIPS = ('_weapon', 'shield', 'hat')
		
	@classmethod
	async def load(cls, member):
		self = Player()
		
		self.member = member
		self.pool = member.pool
		self.level = member.localLevel
		
		for slot in self.__slots__:
			if slot not in self.EXTERNAL and slot not in self.EQUIPS and slot not in self.SETTERS:
				data = await self.member.getRPGStats(slot)
				
				setattr(self, slot, data[0])
		
		equips = await self.member.getRPGEquipment(wearing = True)
		self.weapon = None
		
		class_ = await self.member.getRPGStats('class')
		self._att = 0
		await self.set_class(class_[0])
		
		skills = await self.member.getRPGSkills()
		
		if self._class.name != 'Peasant':
			s = {str(skill[1]) : skill for skill in skills}
			cs = []
			
			if s:
				for skill in self._class.class_skills:
					if self.level >= skill.req_level:
						cs.append(s[str(skill.id)])
			
			self.skills = cs
		
		if equips:
			for equip in equips:
				await self.set_equip(equips[equip])
		
		return self
	
	async def equip(self, item, item_id):
		if self.weapon and item.type == 4:
		
			if self.weapon.equip_type in ['2h Weapon', 'Ranged']:
				return False
		
		await self.member.setRPGEquipment(item_id, item.type)
		
		return True 
		
	async def choose_class(self, name):
		_class = Class(name, self.level)
		
		if _class.name != 'Peasant':
			await self.member.setRPGClass(_class)
			
			return _class
	
	async def set_class(self, class_):
		if class_ != 0:
			self._class = Class(load_class(class_)['name'].lower(), self.level)
			
			if self._class.modifiers:
				for modifier in self._class.modifiers:
					if modifier == 'att':
						self.att = self._class.modifiers[modifier]
					elif modifier == 'def_':
						self.def_ = self._class.modifiers[modifier]
					else:
						mod = getattr(self, modifier)
						setattr(self, modifier, mod + self._class.modifiers[modifier])
		
		else:
			self._class = Class('Peasant', self.level)
	
	async def set_equip(self, item):
		equip = Equipment(dict(item[1]))
		
		{
			'1': setattr(self, 'weapon', equip),
			'2': setattr(self, 'weapon', equip),
			'3': setattr(self, 'weapon', equip),
			'4': setattr(self, 'shield', equip),
			'5': setattr(self, 'hat', equip),
		}.get(str(equip.type))
		
		print(self.weapon)
		
		self._att += equip.att
		self.str_ += equip.str_	
		self.dex += equip.dex	
		self.int_ += equip.int_
		self.cha += equip.cha
	
	async def get_equips(self):
		equips = await self.member.getRPGEquipment(wearing = True)
		
		return [Equipment(dict(equips[equip][1])) for equip in equips]
	
	def get_stats(self, *args):
		return [getattr(self, arg) for arg in args]
	
	def get_skill_levels(self):
		return {str(skill[1]): skill[2] for skill in self.skills}
	
	def take_damage(self, damage):
		self.rw = self.rw - damage
	
	def raise_skill(self, skill):
		pass
	
	def cast_combat_skill(self, skill, target):
		if skill.type == 1:
			skill_level = self.get_skill_levels()[str(skill.id)]
			pattern = skill.levels[str(skill_level)]
			
			roll = pattern['roll'].split('d')
			damage, modifier = 0, 0
			
			for i in range(int(roll[0])):
				damage += random.randint(1, int(roll[1]))
			
			for mod in pattern['mods'].split(':'):
				if mod == 'att':
					modifier += self.att
				else:
					modifier += getattr(self, mod)
			
			return damage + modifier
	
	@property
	def _class(self):
		return self.class_
		
	@_class.setter
	def _class(self, val):
		self.class_ = val
	
	@property
	def skills(self):
		return self._skills
		
	@skills.setter
	def skills(self, val):
		self._skills = val
	
	@property
	def weapon(self):
		return self._weapon
	
	@weapon.setter
	def weapon(self, val):
		self._weapon = val
		
	@property
	def att(self):
		return self._att + self.str_
	
	@att.setter
	def att(self, val):
		self._att = val
		
	@property
	def def_(self):
		return self._def + self.dex
	
	@def_.setter
	def def_(self, val):
		self._def = val