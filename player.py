import asyncio, asyncpg
from .Class import load_class, Class
from .item import load_item, Equipment

class Player:
	
	
	__slots__ = (
		'member', 'pool',
		'level', 'class_', 'max_health', 'max_mana',
		'str_', 'dex', 'int_', 'wis', 'luk', 'cha',
		'_weapon', 'shield', 'hat'
	)
	
	SETTERS = ('class_', '_weapon')
	
	EXTERNAL = ('member', 'pool')
	
	EQUIPS = ('_weapon', 'shield', 'hat')
	
	# RW = 20
	# F = 5
	# ST = 7

	# def __init__(self, member, str_, dex, int_, luk, cha):
		# self.pool = person.pool
		# self.member = person
		
		# stats = ['str', 'dex', 'int_', 'luk', 'cha', 
		# self.rw = self.RW
		# self.str_ = str_
		# self.dex = dex
		# self.int_ = int_
		# self.luk = luk
		# self.cha = cha
		# self.att = self.str_ # + self.level
		# self.weapon = None
		# self.shield = None
		# self.fl = math.floor(self.F + (1.2 * dex))
		# self.st = math.floor(self.ST + (1.2 * int_))
		
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
		class_ = await self.member.getRPGStats('class')
		
		await self.set_class(class_[0])
		
		if equips:
			for equip in equips:
				await self.set_equip(equips[equip])
		
		return self
	
	async def equip(self, item, item_id):
		await self.member.setRPGEquipment(item_id, item.type)
		
	async def choose_class(self, name):
		_class = Class(name, self.level)
		await self.member.setRPGClass(_class)
		
		return _class
	
	async def set_class(self, class_):
		if class_ != 0:
			self._class = Class(load_class(class_)['name'].lower(), self.level)
		else:
			self._class = Class('Peasant', self.level)
	
	async def set_equip(self, item):
		equip = Equipment(dict(item[1]))
		
		{
			'1': setattr(self, 'weapon', equip),
			'2': setattr(self, 'shield', equip),
			'3': setattr(self, 'hat', equip),
		}.get(str(equip.type))
		
		print(self.weapon)
		
		self.str_ += equip.str_	
		self.dex += equip.dex	
		self.int_ += equip.int_
		self.cha += equip.cha
	
	async def get_equips(self):
		equips = await self.member.getRPGEquipment(wearing = True)
		
		return [Equipment(dict(equips[equip][1])) for equip in equips]
	
	def take_damage(self, damage):
		self.rw = self.rw - damage
		
	@property
	def _class(self):
		return self.class_
		
	@_class.setter
	def _class(self, val):
		self.class_ = val
	
	@property
	def weapon(self):
		return self._weapon
	
	@weapon.setter
	def weapon(self, val):
		self._weapon = val
		
	@property
	def att(self):
		pass